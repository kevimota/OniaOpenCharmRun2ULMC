import os

files = [
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt120ToMuMuDstarToD0pi_2016APV.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt120ToMuMuDstarToD0pi_2016.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt120ToMuMuDstarToD0pi_2017.started",
    "/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt120ToMuMuDstarToD0pi_2018.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt30To60ToMuMuDstarToD0pi_2016APV.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt30To60ToMuMuDstarToD0pi_2016.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt30To60ToMuMuDstarToD0pi_2017.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt30To60ToMuMuDstarToD0pi_2018.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt60To120ToMuMuDstarToD0pi_2016APV.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt60To120ToMuMuDstarToD0pi_2016.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt60To120ToMuMuDstarToD0pi_2017.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt60To120ToMuMuDstarToD0pi_2018.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt9To30ToMuMuDstarToD0pi_2016APV.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt9To30ToMuMuDstarToD0pi_2016.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt9To30ToMuMuDstarToD0pi_2017.started",
    #"/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/DR/paths/UpsilonPt9To30ToMuMuDstarToD0pi_2018.started",
  ]
template = 'python/gentuple_template_from_files.py'

for filename in files:
    outname = filename[filename.rfind("/")+1:filename.rfind(".")]
    run = True
    with open(template, 'r') as f:
        new_file = f.read().replace('FILENAME', filename)
        new_file = new_file.replace('OUTNAME', outname)

        nfilename = 'python/gentuple_' + outname + ".py"
        with open(nfilename, 'w') as nf:
            nf.write(new_file)

    if run: 
        os.system('cmsRun ' + nfilename)
        os.system('rm -rf ' + nfilename)
