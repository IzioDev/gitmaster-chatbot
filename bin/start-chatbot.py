import subprocess

subprocess.run("cd ../ && rasa shell --endpoints endpoints.yml --debug", shell=True, check=True)
