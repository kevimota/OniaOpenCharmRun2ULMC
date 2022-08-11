#!/usr/bin/env python 

import os, subprocess, sys
import datetime

today = datetime.date.today()

njobs = 1000 # Change for the wanted number of jobs
template = "crab_config_DR"

for path in subprocess.check_output("ls paths/", shell=True).decode("utf-8").splitlines():
    if not (path.endswith(".txt")):
        continue
    dataset = path[0: path.find(".")]
    if '2016' in dataset:
        if 'APV' in dataset: year = '2016APV'
        else: year = '2016'
    if '2017' in dataset:
        year = '2017'
    if '2018' in dataset:
        year = '2018'
    with open(template + ".py", 'r') as f:
        new_file = f.read().replace("DATASET", dataset)
        new_file = new_file.replace("DATE", today.strftime("%d-%m-%Y"))
        new_file = new_file.replace("PSET", "DR_" + year + "_cfg.py")
        new_file = new_file.replace("FILE", path)
        new_file = new_file.replace("NJOBS", str(njobs))

        with open(template + "_" + dataset + ".py", 'w') as nf:
            nf.write(new_file)
    os.system("crab submit -c " + template + "_" + dataset + ".py")
    os.rename("paths/" + path, "paths/" + path.replace(".txt", ".started"))
