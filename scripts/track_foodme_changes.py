import os
import requests
from pathlib import Path

OWNER = "favour-nz"
REPO = "foodme-app"
BRANCH = os.getenv("TARGET_BRANCH", "dev")

TOKEN = os.getenv("FOODME_TOKEN")
if not TOKEN:
    raise SystemExit("FOODME_TOKEN is missing")

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}

TRACK_FILE = Path("tracking") / f"{REPO}_{BRANCH}.sha"


def github_get(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    if response.status_code >= 400:
        raise RuntimeError(f"GitHub API error {response.status_code}: {response.text}")
    return response.json()


def get_latest_commit_sha():
    data = github_get(f"https://api.github.com/repos/{OWNER}/{REPO}/commits/{BRANCH}")
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
    return github_get(f"https://api.github.com/repos/{OWNER}/{REPO}/compare/{old_sha}...{new_sha}")


def main():
    print("Checking changes for:", f"{OWNER}/{REPO}")
    print("Branch:", BRANCH)

    latest_sha = get_latest_commit_sha()
    last_sha = read_last_checked_sha()

    print("Latest commit:", latest_sha)

    if not last_sha:
        print("First run detected. Saving latest commit and exiting.")
        save_latest_sha(latest_sha)
        return

    if last_sha == latest_sha:
        print("No changes detected since last check.")
        return

    comparison = compare_commits(last_sha, latest_sha)

    print("\n=== CHANGE SUMMARY ===")
    print("Number of new commits:", comparison.get("ahead_by", 0))

    print("\nCommits:")
    for commit in comparison.get("commits", []):
        short_sha = commit["sha"][:7]
        message = commit["commit"]["message"].split("\n")[0]
        author = commit["commit"]["author"]["name"]
        print(f"- {short_sha}: {message} ({author})")

    print("\nFiles changed:")
    for file in comparison.get("files", []):
        print(f"- {file['filename']} ({file['status']})")

    save_latest_sha(latest_sha)
    print("\nLatest commit saved for next run.")


if __name__ == "__main__":
    main()
