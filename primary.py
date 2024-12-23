import argparse
import requests
import json
from datetime import datetime

# Constants - can adjust this however you wish
GITHUB_API_URL = "https://api.github.com"

# Functions
def get_repo_details(owner, repo, token):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching repository details: {response.status_code} {response.text}")

def get_contributors(owner, repo, token):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contributors"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching contributors: {response.status_code} {response.text}")

def get_issues(owner, repo, token, state="open"):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues?state={state}"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching issues: {response.status_code} {response.text}")

def get_languages(owner, repo, token):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/languages"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching languages: {response.status_code} {response.text}")

def save_data_to_file(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

# Main CLI tool
def main():
    parser = argparse.ArgumentParser(description="GitHub Repository Insights CLI Tool")
    parser.add_argument("owner", nargs="?", help="Owner of the repository")
    parser.add_argument("repo", nargs="?", help="Name of the repository")
    parser.add_argument("--token", help="GitHub personal access token for authenticated requests", default=None)
    parser.add_argument("--save", help="File to save the output data", default=None)

    args = parser.parse_args()

    if not args.owner or not args.repo:
        parser.print_help()
        exit(1)

    try:
        output_data = {}

        # Fetch repository details
        repo_details = get_repo_details(args.owner, args.repo, args.token)
        print(f"Repository: {repo_details['full_name']}")
        print(f"Description: {repo_details['description']}")
        print(f"Stars: {repo_details['stargazers_count']}")
        print(f"Forks: {repo_details['forks_count']}")
        print(f"Open Issues: {repo_details['open_issues_count']}")
        print("\n")
        output_data['repository'] = repo_details

        # Fetch contributors
        print("Top Contributors:")
        contributors = get_contributors(args.owner, args.repo, args.token)
        for contributor in contributors[:5]:
            print(f"- {contributor['login']} ({contributor['contributions']} contributions)")
        print("\n")
        output_data['contributors'] = contributors

        # Fetch issues
        print("Open Issues by Label:")
        issues = get_issues(args.owner, args.repo, args.token)
        label_counts = {}
        for issue in issues:
            for label in issue.get('labels', []):
                label_name = label['name']
                label_counts[label_name] = label_counts.get(label_name, 0) + 1
        for label, count in label_counts.items():
            print(f"- {label}: {count}")
        print("\n")
        output_data['issues'] = {'by_label': label_counts}

        # Fetch languages
        print("Languages Used:")
        languages = get_languages(args.owner, args.repo, args.token)
        total_bytes = sum(languages.values())
        language_data = {}
        for lang, bytes_count in languages.items():
            percentage = (bytes_count / total_bytes) * 100
            print(f"- {lang}: {percentage:.2f}%")
            language_data[lang] = percentage
        output_data['languages'] = language_data

        # Save data if requested (not necessary but if you utilize stats and github data its best to save your data on a VM or something similar)
        if args.save:
            save_data_to_file(output_data, args.save)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
