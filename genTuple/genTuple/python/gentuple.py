import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from os import listdir

process = cms.Process("Test")

""" process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/m/mabarros/public/MonteCarlo/SPS/CMSSW_10_6_20_patch1/src/test_SPS_13TeV_GS.root')
) """

""" path = [
  '/eos/user/k/kmotaama/CRAB_PrivateMC/UpsilonPt9ToMuMuDstarToD0pi/220608_150442'
  ]
files = ['file:' + path + i for i in listdir(path)]

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(*files)
) """

files = FileUtils.loadListFromFile("/afs/cern.ch/work/k/kmotaama/public/analysis/OniaOpenCharmRun2UL/OniaOpenCharmRun2ULMC/CMSSW_10_6_12/src/UpsilonPt9To30ToMuMuDstarToD0piPtHat9_2018.txt")
 
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(*files[:10])
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.MessageLogger = cms.Service("MessageLogger")

process.genTuple = cms.EDAnalyzer(
    "genTuple", 
    savePdgId = cms.untracked.vint32(23, 553, 100553, 200553, 13, -13, 413, -413, 421, -421, 211, -211, 321, -321),
)

process.TFileService = cms.Service("TFileService",
       fileName = cms.string('UpsilonPt9To30ToMuMuDstarToD0piPtHat9_2018.root'),                                                                 
)

process.p = cms.Path(process.genTuple)
