from CRABClient.UserUtilities import config

config = config()
config.General.requestName = 'DR_Production_UpsilonDzeroMuMu_GS'
config.General.workArea = 'crab_projects'
config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'UpsilonToMuMuDzero_13TeV_DR_cfg.py'
#config.Data.inputDataset = '/CRAB_PrivateMC/kmotaama-GEN-SIM_Production_UpsilonDzeroMuMu_GS_UERJ-d6d16d213e813b053e18abec29d7e943/USER'
config.Data.outputDatasetTag = 'DR_Production_UpsilonDzeroMuMu_GS'
config.Data.userInputFiles = open('file.txt').readlines()
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 25  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kmotaama/'
config.General.transferOutputs = True
config.Data.publication = True
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2500
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'
#config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_BR_UERJ']
config.Site.storageSite = 'T2_BR_UERJ'
