# MC Onia + Open Charm

Repository for Private MC generation for Onia + Open Charm Analysis using Run 2 UL with HLT simulation up to MINIAOD using CRAB3. 

Can be adapted for any Run 2 UL MC production

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

## Running private MC production with CRAB3

First, you should use the release CMSSW_10_6_12. To set the environment:
``` 
. quick_setup.sh 
```

### GEN-SIM step

For GS step enter the GS directory

```
cd $CMSSW_BASE/GS
```

In the directory config you should put all the config files you want to submit. The cmsDriver commands section shows how to create the fragments for each step (here only GS is needed)

The code in will create and submit a crab config file for each file in config directory using the crab_config_GS.py as a template.

To submit:

```
python submit_GS.py
```

To check the status of your jobs and to resubmit the failed ones:

```
python resubmit_GS.py
```

### DR step

Switch to DR folder:

```
cd $CMSSW_BASE/DR
```

For DR step it will use the ```DR_cfg.py``` as pset for the jobs. 

The files created in the previous step should be listed in a ```dataset_name.txt``` file for the submition. There should be one txt file per dataset.

For submission:

```
python submit_DR.py
```

To check the status of your jobs and to resubmit the failed ones:

```
python resubmit_DR.py
```

### HLT step

For HLT step you have to switch to CMSSW_9_4_14_UL_patch1 release. In this release you need to run the ``` quick_setup.sh ``` script again.

Switch to HLT folder:

```
cd $CMSSW_BASE/HLT
```

The rest is similar to DR step. Put one txt file per dataset in paths folder and run the python scripts.

For submission:

```
python submit_HLT.py
```

To check the status of your jobs and to resubmit the failed ones:

```
python resubmit_HLT.py
```

### AOD step

Switch back to CMSSW_10_6_12 release and run the ``` quick_setup.sh ``` script.

Switch to AOD folder:
```
cd $CMSSW_BASE/AOD
```

Again, put one txt file per dataset in paths folder and run the python scripts.

For submission:

```
python submit_AOD.py
```

To check the status of your jobs and to resubmit the failed ones:

```
python resubmit_AOD.py
```

### MINIAOD step

In CMSSW_10_6_12 release.

Switch to MINIAOD folder:

```
cd $CMSSW_BASE/MINIAOD
```

Same as before, one dataset per file and for submission:

```
python submit_MINIAOD.py
```

And to check the status of your jobs and to resubmit the failed ones:

```
python resubmit_MINIAOD.py
```

## cmsDriver commands

### Data 2017

* GEN,SIM step:
```
cmsDriver.py Configuration/GenProduction/python/fragment_cfi.py --fileout file:GS.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 106X_mc2017_realistic_v9 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --customise Configuration/DataProcessing/Utils.addMonitoring --geometry DB:Extended --era Run2_2017 --python_filename configname_GS_cfg.py -n 5000 --no_exec
```

* DIGI2RAW:
```
cmsDriver.py --filein file:GS.root --fileout file:DR.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL17_106X_mc2017_realistic_v6-v3/PREMIX" --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI --conditions 106X_mc2017_realistic_v9 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2  --geometry DB:Extended --datamix PreMix --era Run2_2017 --python_filename DR_cfg.py -n -1 --no_exec
```

* HLT (on CMSSW_9_4_14_UL_patch1):
```
cmsDriver.py --filein file:DR.root --fileout file:HLT.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v15 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2e34v40 --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename configname_HLT_cfg.py -n -1 --no_exec
```

* AODSIM step:
```
cmsDriver.py --filein file:HLT.root --fileout file:AOD.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 106X_mc2017_realistic_v9 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename configname_AOD_cfg.py -n -1 --no_exec
```

* MiniAOD step:
```
cmsDriver.py --filein file:AOD.root --fileout file:MiniAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 106X_mc2017_realistic_v9 --step PAT --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename configname_MiniAOD_cfg.py -n -1 --no_exec
```

One should change the fragment_cfi.py name with the fragment name.

One should change configname to the name of the config you want.

The options --filein and --fileout sets the input and output name of the cfg.

The option --nThreads can be changed if one wants to use more threads (runs faster), but for CRAB you should especify the number of threads in crab cfg file.

If needed one can fuse the GS and DR, as well as AOD and MINIAOD steps.