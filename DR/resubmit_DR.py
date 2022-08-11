#!/usr/bin/env python 

import subprocess, os, time, re

regex = '[0-9]*\.[0-9]*%'

run = True
report = False

st = ['running', 'transferring', 'unsubmitted', 'idle', 'toRetry']

#folders = ['MuOniaRun2017UL', 'MuOniaRun2018UL']
folders = ['crab_projects',]
#folders = ['UpsilonToMuMuDstarToD0pi_MC',]

#exclude = ['crab_MuOniaRun2017B_AOD', 'crab_MuOniaRun2017C_AOD', 'crab_MuOniaRun2017D_AOD']
exclude = []

check = [{project:True for project in subprocess.check_output("ls " + f + "/", shell=True).decode("utf-8").splitlines() if project not in exclude} for f in folders]

while run:
    print('========== Checking jobs status ==========')
    for i0, folder in enumerate(folders):
        for project in check[i0]:
            failed = False
            if not check[i0][project]: continue
            status = subprocess.check_output('crab status -d ' + folder + '/' + project, shell=True)
            status = status.splitlines()
            
            print('========== Job '+ project +' status ==========')

            for line in status:
                if 'failed' in line:
                    found = re.findall(regex, line)
                    if len(found) > 0:
                        print(line)
                        print('========== Resubmiting failed jobs ==========')
                        os.system('crab resubmit -d ' + folder + '/' + project)
                        failed = True
                if 'finished' in line:
                    print(line)
                    if '100.0%' in line:
                        check[i0][project] = False
        
                for s in st:
                    if s in line:
                        print(line)
                        check[i0][project] = True
            if failed: check[i0][project] = True
        
    sum_checks = 0
    for i0 in check:
        for i1 in i0:
            sum_checks += i0[i1]
    print(sum_checks)

    if sum_checks == 0:
        run = False
        break
    print('')
    time.sleep(10*60)


if report:
    for i0, folder in enumerate(folders):
        for project in check[i0]:
            os.system('crab report -d ' + folder + '/' + project)


