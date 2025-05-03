from github_api import get_user_repositories, get_pull_requests, get_commits, get_issues
from utils import print_repo_info, print_pull_requests, print_commits, print_issues

def inspect_all_repos():
    repos = get_user_repositories()
    if not repos:
        print("No repositories found or failed to fetch.")
        return

    for repo in repos:
        owner = repo['owner']['login']
        name = repo['name']

        print_repo_info(repo)

        prs = get_pull_requests(owner, name)
        print_pull_requests(prs)

        commits = get_commits(owner, name)
        print_commits(commits)

        issues = get_issues(owner, name)
        print_issues(issues)

        print("=" * 40)

if __name__ == "__main__":
    inspect_all_repos()
