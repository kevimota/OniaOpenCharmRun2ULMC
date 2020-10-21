from CRABClient.UserUtilities import config
import getpass

config = config()
config.General.requestName = 'MINIAOD_DATASET_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'MINIAOD_cfg.py'
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2500

config.Data.outputDatasetTag = 'DATASET'
config.Data.userInputFiles = open('paths/FILE').readlines()
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/' + getpass.getuser() + '/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.Site.whitelist = ['T2_BR_UERJ']
config.Site.storageSite = 'T2_BR_UERJ'
