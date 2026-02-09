"""
GitHub statistics fetcher using GraphQL API.
Fetches user stats, repository data, and contribution information.
"""

import requests
import json
from pathlib import Path
from typing import Dict, Any, List
import time


class GitHubStats:
    """Fetch GitHub statistics via GraphQL API."""

    def __init__(self, username: str, token: str):
        """Initialize with GitHub username and personal access token."""
        self.username = username
        self.token = token
        self.api_url = "https://api.github.com/graphql"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.cache_path = Path(__file__).parent / "cache.json"
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict[str, Any]:
        """Load cache from file."""
        if self.cache_path.exists():
            try:
                with open(self.cache_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def _save_cache(self):
        """Save cache to file."""
        with open(self.cache_path, 'w') as f:
            json.dump(self.cache, f, indent=2)

    def _execute_query(self, query: str, variables: Dict = None) -> Dict[str, Any]:
        """Execute GraphQL query."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(f"GraphQL query failed: {response.status_code} - {response.text}")

        data = response.json()
        if "errors" in data:
            raise Exception(f"GraphQL errors: {data['errors']}")

        return data["data"]

    def fetch_user_stats(self) -> Dict[str, Any]:
        """Fetch comprehensive user statistics."""
        query = """
        query($username: String!) {
          user(login: $username) {
            name
            bio
            company
            location
            email
            createdAt
            followers {
              totalCount
            }
            following {
              totalCount
            }
            repositories(ownerAffiliations: OWNER, privacy: PUBLIC) {
              totalCount
            }
            contributionsCollection {
              totalCommitContributions
              totalIssueContributions
              totalPullRequestContributions
              totalPullRequestReviewContributions
              contributionCalendar {
                totalContributions
              }
            }
          }
        }
        """

        data = self._execute_query(query, {"username": self.username})
        user = data["user"]

        # Calculate total contributions
        contributions = user["contributionsCollection"]
        total_contributions = contributions["contributionCalendar"]["totalContributions"]
        total_commits = contributions["totalCommitContributions"]

        # Fetch repository statistics
        repos_data = self._fetch_repository_stats()

        stats = {
            "name": user["name"] or self.username,
            "bio": user["bio"] or "",
            "company": user["company"] or "",
            "location": user["location"] or "",
            "email": user["email"] or "",
            "followers": user["followers"]["totalCount"],
            "following": user["following"]["totalCount"],
            "repositories": user["repositories"]["totalCount"],
            "total_commits": total_commits,
            "total_contributions": total_contributions,
            "total_stars": repos_data["total_stars"],
            "total_forks": repos_data["total_forks"],
            "languages": repos_data["languages"],
            "lines_of_code": self._calculate_lines_of_code()
        }

        return stats

    def _fetch_repository_stats(self) -> Dict[str, Any]:
        """Fetch repository statistics including stars, forks, and languages."""
        query = """
        query($username: String!, $cursor: String) {
          user(login: $username) {
            repositories(
              first: 100,
              after: $cursor,
              ownerAffiliations: OWNER,
              privacy: PUBLIC,
              orderBy: {field: UPDATED_AT, direction: DESC}
            ) {
              totalCount
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                name
                stargazerCount
                forkCount
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                  edges {
                    size
                    node {
                      name
                      color
                    }
                  }
                }
              }
            }
          }
        }
        """

        total_stars = 0
        total_forks = 0
        language_sizes = {}
        has_next_page = True
        cursor = None

        while has_next_page:
            variables = {"username": self.username, "cursor": cursor}
            data = self._execute_query(query, variables)

            repos = data["user"]["repositories"]
            has_next_page = repos["pageInfo"]["hasNextPage"]
            cursor = repos["pageInfo"]["endCursor"]

            for repo in repos["nodes"]:
                total_stars += repo["stargazerCount"]
                total_forks += repo["forkCount"]

                # Aggregate language statistics
                for lang_edge in repo["languages"]["edges"]:
                    lang_name = lang_edge["node"]["name"]
                    lang_size = lang_edge["size"]

                    if lang_name in language_sizes:
                        language_sizes[lang_name] += lang_size
                    else:
                        language_sizes[lang_name] = lang_size

        # Sort languages by size
        sorted_languages = sorted(
            language_sizes.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return {
            "total_stars": total_stars,
            "total_forks": total_forks,
            "languages": [lang for lang, _ in sorted_languages[:10]]
        }

    def _calculate_lines_of_code(self) -> int:
        """Calculate total lines of code across all repositories."""
        cache_key = f"loc_{self.username}_{int(time.time() / 86400)}"  # Daily cache

        if cache_key in self.cache:
            return self.cache[cache_key]

        # Fetch repository list
        query = """
        query($username: String!, $cursor: String) {
          user(login: $username) {
            repositories(
              first: 100,
              after: $cursor,
              ownerAffiliations: OWNER,
              privacy: PUBLIC
            ) {
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                name
                defaultBranchRef {
                  name
                }
              }
            }
          }
        }
        """

        repos = []
        has_next_page = True
        cursor = None

        while has_next_page:
            variables = {"username": self.username, "cursor": cursor}
            data = self._execute_query(query, variables)

            repo_data = data["user"]["repositories"]
            has_next_page = repo_data["pageInfo"]["hasNextPage"]
            cursor = repo_data["pageInfo"]["endCursor"]

            for repo in repo_data["nodes"]:
                if repo["defaultBranchRef"]:
                    repos.append(repo["name"])

        # Use REST API to fetch LOC for each repository
        total_loc = 0
        rest_headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

        for repo_name in repos[:20]:  # Limit to 20 repos to avoid rate limits
            try:
                url = f"https://api.github.com/repos/{self.username}/{repo_name}/stats/code_frequency"
                response = requests.get(url, headers=rest_headers, timeout=10)

                if response.status_code == 200:
                    code_freq = response.json()
                    if code_freq:
                        # Sum additions and deletions
                        for week in code_freq:
                            total_loc += abs(week[1])  # Additions
                elif response.status_code == 202:
                    # Data is being computed, wait and retry
                    time.sleep(2)
                    response = requests.get(url, headers=rest_headers, timeout=10)
                    if response.status_code == 200:
                        code_freq = response.json()
                        if code_freq:
                            for week in code_freq:
                                total_loc += abs(week[1])
            except Exception as e:
                print(f"Warning: Failed to fetch LOC for {repo_name}: {e}")
                continue

        # Cache the result
        self.cache[cache_key] = total_loc
        self._save_cache()

        return total_loc

    def format_number(self, num: int) -> str:
        """Format large numbers with K/M suffix."""
        if num >= 1_000_000:
            return f"{num / 1_000_000:.1f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.1f}K"
        else:
            return str(num)


if __name__ == "__main__":
    # Test the module
    from config import Config

    stats = GitHubStats(Config.GITHUB_USERNAME, Config.GITHUB_TOKEN)
    user_stats = stats.fetch_user_stats()

    print("GitHub Statistics:")
    print(f"Name: {user_stats['name']}")
    print(f"Repositories: {user_stats['repositories']}")
    print(f"Stars: {user_stats['total_stars']}")
    print(f"Commits: {user_stats['total_commits']}")
    print(f"Contributions: {user_stats['total_contributions']}")
    print(f"Followers: {user_stats['followers']}")
    print(f"Following: {user_stats['following']}")
    print(f"Lines of Code: {stats.format_number(user_stats['lines_of_code'])}")
    print(f"Top Languages: {', '.join(user_stats['languages'][:5])}")
