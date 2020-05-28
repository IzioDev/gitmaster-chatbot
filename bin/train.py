import subprocess

subprocess.run("cd ../ && rasa train", shell=True, check=True)
