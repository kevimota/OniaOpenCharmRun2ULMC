from CRABClient.UserUtilities import config

config = config()
config.General.requestName = 'GEN-SIM_Production_UpsilonDzeroMuMu_GS_UERJ'
config.General.workArea = 'crab_projects'
config.JobType.pluginName = 'PrivateMC' 
config.JobType.psetName = 'UpsilonToMuMuDzero_13TeV_GS_cfg.py'
config.Data.publishDBS = 'phys03'
config.Data.splitting = 'EventBased' #'EventBased'  #'FileBased'
config.Data.unitsPerJob = 2000
NJOBS = 25  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kmotaama/'
config.General.transferOutputs = True
config.Data.publication = True
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'
config.Data.outputDatasetTag = 'GEN-SIM_Production_UpsilonDzeroMuMu_GS_UERJ'
#config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_BR_UERJ']
config.Site.storageSite = 'T2_BR_UERJ'
