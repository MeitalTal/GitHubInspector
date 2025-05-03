def print_header(title):
    print(f"\n{'='*10} {title} {'='*10}")

def print_subheader(title):
    print(f"\n-- {title} --")

def print_repo_info(repo):
    print_header(repo['name'])
    print(f"Visibility: {'Private' if repo['private'] else 'Public'}")
    print(f"Description: {repo.get('description') or 'No description'}")
    print(f"Default Branch: {repo['default_branch']}")

def print_pull_requests(prs):
    print_subheader("Pull Requests")
    if not prs:
        print("No open pull requests.")
    for pr in prs:
        print(f"• {pr['title']} by {pr['user']['login']} ({pr['created_at']})")

def print_commits(commits):
    print_subheader("Last Commits")
    for commit in commits:
        print(f"• {commit['commit']['message']} by {commit['commit']['author']['name']} at {commit['commit']['author']['date']}")

def print_issues(issues):
    print_subheader("Issues")
    if not issues:
        print("No issues found.")
    for issue in issues:
        print(f"• {issue['title']} [{issue['state']}]")
