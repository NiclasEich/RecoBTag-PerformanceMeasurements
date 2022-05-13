# RecoBTag-PerformanceMeasurements

## Basics & software setup

```bash
# setting up the latest release
cmsrel CMSSW_12_3_2_patch1
cd CMSSW_12_3_2_patch1/src
cmsenv

export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg RecoBTag/Combined

# clone our version of JMET tools
git clone https://github.com/SWuchterl/JMETriggerAnalysis.git -o SWuchterl -b run3

# clone this repository
git clone -b Run3_ForJIRA_12_3_2 --recursive https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

cd $CMSSW_BASE/src/

wget https://raw.githubusercontent.com/silviodonato/cms-tsg/forceNewJEC/forceNewJEC.py RecoBTag/PerformanceMeasurements/python/

scram b -j12

```

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
