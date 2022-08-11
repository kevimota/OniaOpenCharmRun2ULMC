import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
from os import listdir

process = cms.Process("Test")

files = FileUtils.loadListFromFile("FILENAME")
 
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
       fileName = cms.string('OUTNAME.root'),                                                                 
)

process.p = cms.Path(process.genTuple)
