import os, subprocess, sys

for project in subprocess.check_output("ls crab_projects/", shell=True).decode("utf-8").splitlines():
    os.system("crab status -d crab_projects/" + project)
    os.system("crab resubmit -d crab_projects/" + project)


