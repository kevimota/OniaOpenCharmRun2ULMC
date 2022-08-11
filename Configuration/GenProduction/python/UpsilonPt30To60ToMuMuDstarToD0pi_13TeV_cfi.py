import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                             EvtGen130 = cms.untracked.PSet(
                                decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                                particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),         
                                convertPythiaCodes = cms.untracked.bool(False),
                                list_forced_decays = cms.vstring('MyD0', 'Myanti-D0'), 
                                operates_on_particles = cms.vint32(421, -421, 413, -413, 553, 100553, 200553),
                                user_decay_embedded= cms.vstring(
"""
Alias      MyD0   D0
Alias      Myanti-D0   anti-D0
ChargeConj Myanti-D0   MyD0
#
Decay MyD0
1.000   K-  pi+         PHSP;
Enddecay
CDecay Myanti-D0
#
End
"""
                                ),
                             ),
                             parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CP5SettingsBlock,
                             processParameters = cms.vstring(
                                'HardQCD:hardccbar = on',
                                'HardQCD:gg2gg = on',
                                'HardQCD:qg2qg = on',
                                'PartonLevel:MPI = on',
                                'SecondHard:Bottomonium = on',
                                'Bottomonium:states(3S1)               = 553,100553,200553',
                                'Bottomonium:O(3S1)[3S1(1)]            = 9.28,4.63,3.54',
                                'Bottomonium:O(3S1)[3S1(8)]            = 0.61,2.22,1.32',
                                'Bottomonium:O(3S1)[1S0(8)]            = 13.60,0.62,1.45',
                                'Bottomonium:O(3S1)[3P0(8)]            = -0.93,0.13,-0.27',
                                'Bottomonium:gg2bbbar(3S1)[3S1(1)]g    = on,on,on',
                                'Bottomonium:gg2bbbar(3S1)[3S1(1)]gm   = on,on,on',
                                'Bottomonium:gg2bbbar(3S1)[3S1(8)]g    = on,on,on',
                                'Bottomonium:qg2bbbar(3S1)[3S1(8)]q    = on,on,on',
                                'Bottomonium:qqbar2bbbar(3S1)[3S1(8)]g = on,on,on',
                                'Bottomonium:gg2bbbar(3S1)[1S0(8)]g    = on,on,on',
                                'Bottomonium:qg2bbbar(3S1)[1S0(8)]q    = on,on,on',
                                'Bottomonium:qqbar2bbbar(3S1)[1S0(8)]g = on,on,on',
                                'Bottomonium:gg2bbbar(3S1)[3PJ(8)]g    = on,on,on',
                                'Bottomonium:qg2bbbar(3S1)[3PJ(8)]q    = on,on,on',
                                'Bottomonium:qqbar2bbbar(3S1)[3PJ(8)]g = on,on,on',
                                'Bottomonium:states(3PJ)               = 10551,110551,210551',
                                'Bottomonium:O(3PJ)[3P0(1)]            = 0.34,0.34,0.34',
                                'Bottomonium:O(3PJ)[3S1(8)]            = 0.94,1.09,0.69',
                                'Bottomonium:gg2bbbar(3PJ)[3PJ(1)]g    = on,on,on',
                                'Bottomonium:qg2bbbar(3PJ)[3PJ(1)]q    = on,on,on',
                                'Bottomonium:qqbar2bbbar(3PJ)[3PJ(1)]g = on,on,on',
                                'Bottomonium:gg2bbbar(3PJ)[3S1(8)]g    = on,on,on',
                                'Bottomonium:qg2bbbar(3PJ)[3S1(8)]q    = on,on,on',
                                'Bottomonium:qqbar2bbbar(3PJ)[3S1(8)]g = on,on,on',
                                'SecondHard:generate = on',
                                'PhaseSpace:pTHatMin = 23.0',
                                'PhaseSpace:pTHatMinSecond = 4.',
                                'PhaseSpace:pTHatMinDiverge = 0.5',
                             ),
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                'pythia8CP5Settings',
                                'processParameters',
                             )
                         ),

)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########

oniafilter = cms.EDFilter("MCMultiParticleFilter",
    Status = cms.vint32(2, 2, 2),
    ParticleID = cms.vint32(553, 100553, 200553),
    PtMin = cms.vdouble(29.5, 29.5, 29.5),
    PtMax = cms.vdouble(60.5, 60.5, 60.5),
    NumRequired = cms.int32(1),
    EtaMax = cms.vdouble(2.5,2.5,2.5),
    EtaMin = cms.vdouble(-2.5,-2.5,-2.5),
    AcceptMore = cms.bool(True)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(3.0, 3.0),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(5.0),
    MaxInvMass = cms.untracked.double(20.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

DstarFilter = cms.EDFilter("PythiaMomDauFilter",
    ChargeConjugation = cms.untracked.bool(True),
    DaughterID = cms.untracked.int32(421),
    DaughterIDs = cms.untracked.vint32(421, 211),
    DescendantsIDs = cms.untracked.vint32(-321, 211),
    MaxEta = cms.untracked.double(2.5),
    MinEta = cms.untracked.double(-2.5),
    MinPt = cms.untracked.double(0.0),
    MomMinPt = cms.untracked.double(2.0),
    MomMinEta = cms.untracked.double(-2.5),
    MomMaxEta = cms.untracked.double(2.5),
    NumberDaughters = cms.untracked.int32(2),
    NumberDescendants = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(413)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*DstarFilter*mumugenfilter)