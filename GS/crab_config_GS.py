from CRABClient.UserUtilities import config
import getpass

config = config()
config.General.requestName = 'GS_DATASET_YEAR_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC' 
config.JobType.psetName = 'config/CONFIG'

config.Data.publication = False
#config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'
config.Data.outputDatasetTag = 'DATASET_YEAR'
config.Data.splitting = 'EventBased' 
config.Data.unitsPerJob = EVENTSJOB
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/uerj/' + getpass.getuser() + '/'

#config.Site.whitelist = ['T2_BR_UERJ']
#config.Site.storageSite = 'T2_BR_UERJ'
config.Site.storageSite = 'T2_US_Caltech'
