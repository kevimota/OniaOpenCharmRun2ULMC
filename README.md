# MC Onia + Open Charm

Repository for Private MC generation for Onia + Open Charm Analysis (in construction).

## Setting the environment

### For GS, DR, AOD and MiniAOD

```
export SCRAM_ARCH=slc7_amd64_gcc700

cmsrel CMSSW_10_6_12
cd CMSSW_10_6_12/src
cmsenv

git clone git@github.com:kevimota/OniaOpenCharmRun2ULMC.git .

scram b
```

### For HLT 

```
export SCRAM_ARCH=slc7_amd64_gcc630

cmsrel CMSSW_9_4_14_UL_patch1
cd CMSSW_9_4_14_UL_patch1/src
cmsenv

git clone git@github.com:kevimota/OniaOpenCharmRun2ULMC.git .

scram b
```

## cmsDriver commands

### Data 2017

#### Examples Dzero

* GEN,SIM step:
```
cmsDriver.py Configuration/GenProduction/python/UpsilonToMuMuDzero_13TeV_cfi.py --fileout file:UpsilonToMuMuDzero_13TeV_GS.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 106X_mc2017_realistic_v7 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename UpsilonToMuMuDzero_13TeV_GS_cfg.py -n 5000 --no_exec
```

* DIGI2RAW:
```
cmsDriver.py --filein file:UpsilonToMuMuDzero_13TeV_GS.root --fileout file:UpsilonToMuMuDzero_13TeV_DR.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 1 --geometry DB:Extended --datamix PreMix --era Run2_2017 --python_filename UpsilonToMuMuDzero_13TeV_DR_cfg.py -n -1 --no_exec
```

* HLT (on CMSSW_9_4_14_UL_patch1):
```
cmsDriver.py --filein file:UpsilonToMuMuDzero_13TeV_DR.root --fileout file:UpsilonToMuMuDzero_13TeV_HLT.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v15 --customise_commands process.source.bypassVersionCheck = cms.untracked.bool(True) --step HLT:2e34v40 --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename UpsilonToMuMuDzero_13TeV_HLT_cfg.py -n -1 --no_exec
```

* AODSIM step:
```
cmsDriver.py --filein file:UpsilonToMuMuDzero_13TeV_HLT.root --fileout file:UpsilonToMuMuDzero_13TeV_AOD.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 106X_mc2017_realistic_v6 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename UpsilonToMuMuDzero_13TeV_AOD_cfg.py -n -1 --no_exec
```

* MiniAOD step:
```
cmsDriver.py --filein file:UpsilonToMuMuDzero_13TeV_AOD.root --fileout file:UpsilonToMuMuDzero_13TeV_MiniAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 106X_mc2017_realistic_v6 --step PAT --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename UpsilonToMuMuDzero_13TeV_MiniAOD_cfg.py -n -1 --no_exec
```