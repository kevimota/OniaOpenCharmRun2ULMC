#!/usr/bin/env python 

import os, subprocess, sys
import datetime

today = datetime.date.today()

njobs = 1000 # Change for the wanted number of jobs
evtsjob = 100000 # Change for the wanted number of evts per job
template = "crab_config_GS"

for config in subprocess.check_output("ls config/", shell=True).decode("utf-8").splitlines():
    if not config.endswith(".py"):
        continue
    dataset = config[0: config.find("_")]
    if '2016' in config:
        if 'APV' in config: year = '2016APV'
        else: year = '2016'
    if '2017' in config:
        year = '2017'
    if '2018' in config:
        year = '2018'
    with open(template + ".py", 'r') as f:
        new_file = f.read().replace("DATASET", dataset)
        new_file = new_file.replace("DATE", today.strftime("%d-%m-%Y"))
        new_file = new_file.replace("CONFIG", config)
        new_file = new_file.replace("EVENTSJOB", str(evtsjob))
        new_file = new_file.replace("NJOBS", str(njobs))
        new_file = new_file.replace("YEAR", year)

        with open(template + "_" + dataset + "_" + year + ".py", 'w') as nf:
            nf.write(new_file)
    os.system("crab submit -c " + template + "_" + dataset + "_" + year + ".py")
    os.rename("config/" + config, "config/" + config.replace(".py", ".started"))







        
