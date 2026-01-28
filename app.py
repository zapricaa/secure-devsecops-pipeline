import subprocess

def run_command(cmd):
    subprocess.run(cmd.split(), shell=False)

run_command("dir")