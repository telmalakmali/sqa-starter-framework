import os
import requests
from pathlib import Path

# Target repository details
OWNER = "favour-nz"
REPO = "foodme-app"
BRANCH = os.getenv("TARGET_BRANCH", "dev")

# GitHub token (stored securely as a secret)
TOKEN = os.getenv("FOODME_TOKEN")
if not TOKEN:
    raise SystemExit("FOODME_TOKEN is missing")

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# File to store last checked commit
TRACK_FILE = Path("tracking") / f"{REPO}_{BRANCH}.sha"


def github_get(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    if response.status_code >= 400:
        raise RuntimeError(f"GitHub API error {response.status_code}")
    return response.json()


def get_latest_commit_sha():
    data = github_get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/commits/{BRANCH}"
    )
    return data["sha"]


def read_last_checked_sha():
    if not TRACK_FILE.exists():
        return None
    value = TRACK_FILE.read_text().strip()
    if value == "initial" or not value:
        return None
    return value


def save_latest_sha(sha):
    TRACK_FILE.parent.mkdir(exist_ok=True)
    TRACK_FILE.write_text(sha)


def compare_commits(old_sha, new_sha):
    return github_get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/compare/{old_sha}...{new_sha}"
    )


def main():
    print("Checking changes for:", f"{OWNER}/{REPO}")
    print("Branch:", BRANCH)

    latest_sha = get_
