import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_repositories():
    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.ok else []

def get_pull_requests(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.ok else []

def get_commits(owner, repo, limit=5):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={limit}"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.ok else []

def get_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=HEADERS)
    if not response.ok:
        return []
    return [issue for issue in response.json() if "pull_request" not in issue]
