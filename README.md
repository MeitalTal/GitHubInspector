# GitHub Inspector

A Python tool to inspect your GitHub repositories via the GitHub REST API.  
It provides detailed information about your repositories, including open pull requests, recent commits, and open issues — all from the command line.

## Features
- List all repositories for the authenticated user
- View open pull requests per repository
- View latest commits (customizable limit)
- View open and closed issues (excluding pull requests)
- Clean, modular codebase using `requests` and `dotenv`
- Simple console output, easy to extend or integrate into CI/CD pipelines

## Requirements
- Python 3.7+
- GitHub Personal Access Token

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/github-inspector.git
   cd github-inspector
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. Update the .env file with your GitHub token

## Usage
Run the tool using:
```bash
python main.py
```
It will:
- Loop through all your repositories
- Print repository metadata
- Show open pull requests
- Show latest commits (default: last 5)
- Show issues (excluding PRs)

## File Structure
```bash
github_inspector/
├── main.py                # Entry point
├── github_api.py          # Handles GitHub API requests
├── utils.py               # Formatting and output helpers
├── .env                   # Your GitHub token
├── requirements.txt       # Python dependencies
```