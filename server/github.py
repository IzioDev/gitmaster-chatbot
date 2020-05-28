# Github interractions :
import os

from github import Github

# Dot env :
from dotenv import load_dotenv

load_dotenv()

github_client = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def search_first_repo_with_name(name="angular"):
    for repo in github_client.search_repositories(name):
        return repo
