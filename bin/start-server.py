import subprocess

subprocess.run("rasa run actions --auto-reload", shell=True, check=True)
