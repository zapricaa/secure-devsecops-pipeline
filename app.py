import subprocess
password = "admin123"

def run_command(cmd):
    subprocess.call(cmd, shell=True)

run_command("dir")