#CMSW path: /afs/cern.ch/work/m/mabarros/CMSSW_10_2_15_patch1/src/Configuration/GenProduction/python


import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import * # Underlying Event(UE) 
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0), # If 0: particle has no open decay channels
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(7000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                         EvtGen130 = cms.untracked.PSet(
                         #uses latest evt and decay tables from evtgen 1.6
                         decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                         particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
                         convertPythiaCodes = cms.untracked.bool(False),
                         #user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bu_Kstarmumu_Kspi.dec'),
                         #content was dump in the embed string below. This should test this feature.
                         list_forced_decays = cms.vstring('MyJpsi', 'MyLambda_c+', 'MyAnti-Lambda_c-'), 
                         operates_on_particles = cms.vint32(443, 4122, -4122),
                         user_decay_embedded= cms.vstring(
"""
Alias      MyLambda_c+      Lambda_c+
Alias      MyAnti-Lambda_c-      anti-Lambda_c-
ChargeConj MyLambda_c+      MyAnti-Lambda_c- 

Alias      MyJpsi      J/psi

Decay MyJpsi
  1.000        mu+     mu-       PHOTOS   VLL;
Enddecay

Decay MyLambda_c+
  1.000        p+      K-      pi+     PHSP;
Enddecay
CDecay MyAnti-Lambda_c- 

End
"""
                          ),
                ),
                parameterSets = cms.vstring('EvtGen130')
        ),
        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Main:timesAllowErrors = 10000',  
            'HardQCD:hardccbar = on',
            'HardQCD:gg2gg = on',
            'PartonLevel:MPI = on',
            'SecondHard:Charmonium = on',
            'SecondHard:generate = on',
            #'StringFlav:mesonCvector = 1.4',
            'PhaseSpace:pTHatMin = 4.5',
            'PhaseSpace:pTHatMinSecond = 4.5',
            'PhaseSpace:pTHatMinDiverge = 0.1',
            '443:onMode = off',
            #'421:onMode = off',
            #'411:onMode = off',
            #'431:onMode = off',
            '4122:onMode = off'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
###########
# Filters #
###########
# Filter only pp events which produce JPsi
jpsifilter = cms.EDFilter("PythiaFilter", 
    ParticleID = cms.untracked.int32(443),
    MinPt           = cms.untracked.double(0.1),
    MaxPt           = cms.untracked.double(12.),
    MinEta          = cms.untracked.double(2.),
    MaxEta          = cms.untracked.double(5.)
)

lambdaCPlusfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(4122, -4122),
    MinPt           = cms.untracked.vdouble(3., 3.),
    MaxPt           = cms.untracked.vdouble(12., 12.),
    MinEta          = cms.untracked.vdouble(2., 2.),
    MaxEta          = cms.untracked.vdouble(5., 5.)
)

jpsidaufilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    #MotherID        = cms.untracked.int32(541),
    ParticleID      = cms.untracked.int32(443),
    DaughterIDs     = cms.untracked.vint32(13, -13),
    MinPt           = cms.untracked.vdouble(0.5, 0.5),
    MinEta          = cms.untracked.vdouble(2., 2.),
    MaxEta          = cms.untracked.vdouble( 5., 5.)
)
# OBS: The filter is with wrong daughters
""" dSPlusdaufilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(3),
    #MotherID        = cms.untracked.int32(541),
    ParticleID      = cms.untracked.int32(431),
    DaughterIDs     = cms.untracked.vint32(-321, 211, 211),
    MinPt           = cms.untracked.vdouble(0.3, 0.3, 0.3),
    MinEta          = cms.untracked.vdouble(2., 2., 2.),
    MaxEta          = cms.untracked.vdouble( 5., 5., 5.)
)  """

# Filter on final state muons
#mumugenfilter = cms.EDFilter("MCParticlePairFilter",
#                             Status = cms.untracked.vint32(1, 1),
#                             MinPt = cms.untracked.vdouble(4.5, 4.5),
#                             MaxEta = cms.untracked.vdouble(1.4, 1.4),
#                             MinEta = cms.untracked.vdouble(-1.4, -1.4),
#                             ParticleID1 = cms.untracked.vint32(13,-13),
#                             ParticleID2 = cms.untracked.vint32(13,-13)
#                             )

ProductionFilterSequence = cms.Sequence(generator*jpsifilter*lambdaCPlusfilter*jpsidaufilter)#*dPlusfilter*mumugenfilter)
