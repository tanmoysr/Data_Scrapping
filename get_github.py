import re
import requests
import json


def get_github_repo_info(repo_url, user_token=None):
    api_url = f"https://api.github.com/repos/{repo_url[len('https://github.com/'):]}"
    if user_token == None:
        response = requests.get(api_url)
    else:
        GITHUB_API_TOKEN = user_token
        GITHUB_HEADERS = {
            'Authorization': "token " + GITHUB_API_TOKEN,
        }
        response = requests.get(api_url, headers=GITHUB_HEADERS)

    if response.status_code == 200:
        repo_data = response.json()
        stars = repo_data.get('stargazers_count', 0)
        watchers = repo_data.get('subscribers_count', 0)
        forks = repo_data.get('forks_count', 0)
        if user_token == None:
            contributors_response = requests.get(f"{api_url}/contributors")
        else:
            contributors_response = requests.get(f"{api_url}/contributors", headers=GITHUB_HEADERS)
        if contributors_response.status_code == 200:
            contributors = len(contributors_response.json())
        else:
            contributors = 0

        if user_token == None:
            languages_response = requests.get(f"{api_url}/languages")
        else:
            languages_response = requests.get(f"{api_url}/languages", headers=GITHUB_HEADERS)
        if languages_response.status_code == 200:
            languages = list(languages_response.json().keys())
        else:
            languages = []

        return {
            'url': repo_url,
            'stars': stars,
            'watchers': watchers,
            'forks': forks,
            'contributors': contributors,
            'languages': languages
        }

    else:
        print(f"Error fetching data for {repo_url}: {response.status_code}")
        return None


if __name__ == "__main__":
    all_repo = set()

    with open('GitHub/1000_lines.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == '\n' or len(line) == 0:
                continue
            splits = line.split(' ')

            if len(splits) == 2:
                repo = splits[0][:-1]
                sid = splits[1]
                # double check
                match = re.findall('https://github\.com/[^"].+', repo)
                if len(match) == 0:
                    continue
                all_repo.add(repo)

            elif len(splits) == 3:
                package = splits[1][:-1]
                repo = splits[2]
                # double check
                match = re.findall('https://github\.com/[^"].+', repo)
                if len(match) == 0:
                    continue
                all_repo.add(repo)

    print(len(all_repo))

    # initialize github repo-id graph
    repo_gid_graph = {}
    with open('GitHub/repo_gid.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")
            repo_gid_graph[line[0]] = line[1]
    token = input("Enter your API key: ")
    static_features = {}
    for repo in all_repo:
        static_features[repo_gid_graph[repo]] = get_github_repo_info(repo, token)
        print(repo)

    with open("CINA data/github/static_features22.json", "w") as outfile:
        json.dump(static_features, outfile, indent=4)
    print(static_features)
