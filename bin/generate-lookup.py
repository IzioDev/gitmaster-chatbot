from server.github import github_client

filepath = "../data/lookups/repository_names.txt"

# Empty the file
# https://stackoverflow.com/questions/4914277/how-to-empty-a-file-using-python
open(filepath, 'w').close()

repository_count_limit = 1000

repo_lookup_file = open(filepath, "w")

iterations = 0
for repo in github_client.get_repos():
    if iterations >= repository_count_limit:
        break

    repo_lookup_file.write(repo.name + '\n')
    iterations += 1

repo_lookup_file.close()