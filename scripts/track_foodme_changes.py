import os
import requests
from pathlib import Path

# =========================================================
# TARGET REPOSITORY CONFIGURATION
# =========================================================
# OWNER:
# The GitHub username or organisation that owns the target repository.
# This value corresponds to the first part of the GitHub repository URL.
#
# Example repository used in this project:
# https://github.com/favour-nz/foodme-app
#
# In this case:
# OWNER = "favour-nz"
OWNER = "favour-nz"

# REPO:
# The name of the GitHub repository being monitored.
# This corresponds to the second part of the repository URL.
#
# Example:
# https://github.com/favour-nz/foodme-app
# REPO = "foodme-app"
REPO = "foodme-app"

# BRANCH:
# The branch of the repository that will be monitored for changes.
# The default branch used for this project is "dev".
# This can be changed using an environment variable if required.
BRANCH = os.getenv("TARGET_BRANCH", "dev")

# =========================================================
# AUTHENTICATION CONFIGURATION
# =========================================================
# FOODME_TOKEN:
# A GitHub Personal Access Token (classic) stored securely
# as a GitHub Actions repository secret.
#
# This token provides authenticated, read-only access to the
# private repository via the GitHub API.
#
# IMPORTANT:
# - The token value is never stored in the codebase.
# - It is injected securely at runtime through GitHub Actions.
TOKEN = os.getenv("FOODME_TOKEN")
if not TOKEN:
    raise SystemExit("FOODME_TOKEN is missing")

# HTTP headers required for authenticated GitHub API requests
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# =========================================================
# TRACKING FILE CONFIGURATION
# =========================================================
# TRACK_FILE:
# Stores the commit SHA from the last successful check.
# This allows the script to detect new changes between executions.
#
# The file is stored locally within the framework repository
# under the 'tracking' directory.
TRACK_FILE = Path("tracking") / f"{REPO}_{BRANCH}.sha"


# =========================================================
# HELPER FUNCTIONS
# =========================================================
def github_get(url):
    """Send an authenticated GET request to the GitHub API."""
    response = requests.get(url, headers=HEADERS, timeout=30)
    if response.status_code >= 400:
        raise RuntimeError(
            f"GitHub API error {response.status_code}: {response.text}"
        )
    return response.json()


def get_latest_commit_sha():
    """Retrieve the latest commit SHA from the target branch."""
    data = github_get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/commits/{BRANCH}"
    )
    return data["sha"]


def read_last_checked_sha():
    """Read the previously stored commit SHA from the tracking file."""
    if not TRACK_FILE.exists():
        return None

    value = TRACK_FILE.read_text().strip()
    if not value or value == "initial":
        return None

    return value


def save_latest_sha(sha):
    """Save the latest commit SHA for use in future comparisons."""
    TRACK_FILE.parent.mkdir(exist_ok=True)
    TRACK_FILE.write_text(sha)


def compare_commits(old_sha, new_sha):
    """Compare two commits and retrieve change details."""
    return github_get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/compare/{old_sha}...{new_sha}"
    )


# =========================================================
# MAIN EXECUTION LOGIC
# =========================================================
def main():
    print("Checking changes for:", f"{OWNER}/{REPO}")
    print("Branch:", BRANCH)

    latest_sha = get_latest_commit_sha()
    last_sha = read_last_checked_sha()

    print("Latest commit:", latest_sha)

    # First execution: store baseline commit and exit
    if not last_sha:
        print("First run detected. Saving latest commit and exiting.")
        save_latest_sha(latest_sha)
        return

    # No new changes detected
    if last_sha == latest_sha:
        print("No changes detected since last check.")
        return

    # Changes detected: retrieve and display summary
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

    # Update tracking file for the next execution
    save_latest_sha(latest_sha)
    print("\nLatest commit saved for next run.")


if __name__ == "__main__":
    main()
