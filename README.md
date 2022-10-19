# RecoBTag-PerformanceMeasurements

## Basics & software setup

```bash
# setting up the latest release

#!/bin/bash
cmsrel CMSSW_12_4_10

cd CMSSW_12_4_10/src

cmsenv
git-cms-init

git cms-addpkg RecoBTag/Combined
git cms-merge-topic theochatzis:simplifiedMenuMTD_dev2

git clone -b Phase2_12_4_10 --recursive git@github.com:NiclasEich/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

scram b -j12

```

### Getting the Phase 2 menu:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/HighLevelTriggerPhase2SimplifiedMenu
getting the menu:
```
cmsrel CMSSW_12_4_0
cd CMSSW_12_4_0/src
cmsenv
git cms-init

cmsDriver.py Phase2 -s HLT:75e33 --processName=HLTX \
--conditions auto:phase2_realistic_T21 \
--geometry Extended2026D88 \
--era Phase2C17I13M9 \
--eventcontent FEVTDEBUGHLT \
--filein=/store/relval/CMSSW_12_4_0/RelValTTbar_14TeV/GEN-SIM-RECO/124X_mcRun4_realistic_v6_2026D88noPU-v1/10000/7715f6d4-125f-44c0-9676-95c79ddf9598.root \
-n 100 --nThreads 1 --no_exec
```

### Running HLTBTagAnalyzer

```
# this should create the menu
python3 runHLTBTagAnalyzer_cfg.py dumpPython=test_Phase2_with_timing_cfg.py defaults=Run3 runOnData=False reco=Phase2 runPuppiJetVariables=True runCaloJetVariables=False globalTag=123X_mcRun4_realistic_v11 inputFiles=/store/relval/CMSSW_12_4_0/RelValTTbar_14TeV/GEN-SIM-RECO/124X_mcRun4_realistic_v6_2026D88noPU-v1/10000/7715f6d4-125f-44c0-9676-95c79ddf9598.root outFilename=test_timing_tree.root

# this runs the exmaple
cmsRun test_Phase2_with_timing_cfg.py
```

# The REST BELOW IS POTENTIALLY OUTDATED AND OLD!


## Instructions to run nTuplizers
### Offline (BTagAnalyzer)

The Offline ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```, to run it with the latest defaults

```bash
cmsRun runBTagAnalyzer_cfg.py defaults=Run3 runOnData=(True or False, depending on your needs) maxEvents=10
```

### Online (HLTBTagAnalyzer)

The Offline ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```, to run it with the latest defaults

```bash
cmsRun runHLTBTagAnalyzer_cfg.py defaults=Run3 runOnData=(True or False, depending on your needs) maxEvents=10
```

## General information

The content of the output nTuple is by default empty and has to be configured according to your needs. The ```store*Variables``` options have been removed.
The new variable configuration can be customized in the file ```RecoBTag/PerformanceMeasurements/python/varGroups_cfi.py```.
New variables need also to be added (apart from adding them in the code) in ```RecoBTag/PerformanceMeasurements/python/variables_cfi.py```


## How to get the latest HLT configuration (GRun / on lxplus only)
Recent versions are also stored already in [here](python/Configs)
For MC:
```bash
hltGetConfiguration /dev/CMSSW_12_3_0/GRun \
--full \
--offline \
--unprescale \
--mc \
--process HLT2 \
--globaltag auto:phase1_2021_realistic \
--max-events 10 --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2022_v1_0_0_xml \
> tmp.py
```
```bash
edmConfigDump tmp.py > HLT_dev_CMSSW_12_3_2_GRun_configDump_MC.py
```
For data:
```bash
hltGetConfiguration /dev/CMSSW_12_3_0/GRun \
--full \
--offline \
--unprescale \
--data \
--process HLT2 \
--globaltag auto:run3_hlt \
--max-events 10 --eras Run2_2018 \
--l1-emulator uGT --l1 L1Menu_Collisions2022_v1_0_0_xml \
--customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
> tmp_data.py
```
```bash
edmConfigDump tmp_data.py > HLT_dev_CMSSW_12_3_0_GRun_configDump_Data.py
```
For data+timing:
```bash
hltGetConfiguration /dev/CMSSW_12_3_0/GRun \
--full \
--offline \
--unprescale \
--data \
--process HLT2 \
--globaltag auto:run3_hlt \
--max-events 10 \
--l1-emulator uGT --l1 L1Menu_Collisions2022_v1_0_0_xml \
--customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
--timing --eras Run2_2018 \
> tmp_data_timing.py
```
```bash
edmConfigDump tmp_data_timing.py > HLT_dev_CMSSW_12_3_0_GRun_configDump_Data_timing.py
```
