# RecoBTag-PerformanceMeasurements

## Table of Contents  
[Basics & software setup](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/tree/Run3_ForJIRA#basics--software-setup)  
[Instructions to run nTuplizers](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/tree/Run3_ForJIRA#instructions-to-run-ntuplizers)  
[General information](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/tree/Run3_ForJIRA#general-information)  
[How to get the latest HLT configuration](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/tree/Run3_ForJIRA#how-to-get-the-latest-hlt-configuration-grun--on-lxplus-only)  
[Where to find the Run 3 reconstruction customization functions](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/tree/Run3_ForJIRA#where-to-find-the-run-3-reconstruction-customization-functions)  

## Basics & software setup

```bash
# setting up the latest release
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_12_3_0_pre2
cd CMSSW_12_3_0_pre2/src
cmsenv

export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg RecoBTag/Combined

git cms-merge-topic silviodonato:customizeHLTforRun3_v2

# clone our version of JMET tools
git clone https://github.com/SWuchterl/JMETriggerAnalysis.git -o SWuchterl -b run3

# make folder for external data (PFHadron calibrations and JEC)
mkdir -p ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data

# PFHC: preliminary HLT-PFHC for Run-3
cp /afs/cern.ch/work/m/missirol/public/run3/PFHC/PFHC_Run3Winter20_HLT_v01.db ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db

# JESC: preliminary HLT-JESCs for Run-3 (PF/PUPPI/CALO)
cp /afs/cern.ch/work/m/missirol/public/run3/JESC/Run3Winter20_V2_MC/Run3Winter20_V2_MC.db ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db

# clone this repository
git clone -b Run3_ForJIRA --recursive https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

# use the newest temporary DeepJet retraining
mkdir -p RecoBTag/Combined/data/DeepFlavour_HLT_12X
cp RecoBTag/PerformanceMeasurements/test/modelFiles/DeepJet_model_ntuples220104_run_04.onnx RecoBTag/Combined/data/DeepFlavour_HLT_12X/model.onnx

# fix muon data input files
cd HLTrigger/Configuration/python/Run3
cp $RecoBTag/PerformanceMeasurements/test/downloadCustomizationFunctions.sh .
./downloadCustomizationFunctions.sh
cd $CMSSW_BASE/src/RecoMuon/TrackerSeedGenerator/data
git clone -b dev https://github.com/wonpoint4/RecoMuon-TrackerSeedGenerator.git TempNewMuonData
mv  TempNewMuonData/* .
mv TempNewMuonData/OIseeding/* OIseeding
rm -rf TempNewMuonData/

cd $CMSSW_BASE/src/

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
--max-events 10 --eras Run3 \
> tmp.py
```
```bash
edmConfigDump tmp.py > HLT_dev_CMSSW_12_3_0_GRun_configDump_MC.py
```
For data:
```bash
hltGetConfiguration /dev/CMSSW_12_2_0/GRun \
--full \
--offline \
--unprescale \
--data \
--process HLT2 \
--globaltag auto:run3_hlt \
--max-events 10 --eras Run2_2018 \
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
--customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
--timing --eras Run2_2018 \
> tmp_data_timing.py
```
```bash
edmConfigDump tmp_data_timing.py > HLT_dev_CMSSW_12_3_0_GRun_configDump_Data_timing.py
```


## Where to find the Run 3 reconstruction customization functions
- Run3TRK:
For the tracking POG single iteration tracking seeded by Patatrack pixeltracks (Triplets+Quadruplets): [here](python/Configs/customizeHLTforRun3Tracking.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L210-L216) and [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L237-L245)

- DeepJet:
For the application of DeepJet to all pF btagging paths: [here](python/customise_TRK_deepjet.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L320-L328)

- noCalo+ROI:
For the ROI TRK+PF approach and removal of calo btagging: [here](python/customise_TRK_replacement.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L331-L340)

- noCalo+global:
For the central/global TRK+PF and removal of calo btagging: [here](python/Configs/customise_TRK.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L237-L245)

- newROICalo+ROI:
For the ROI TRK+PF approach and addition of new ROI calo btagging: [here](python/customise_TRK_replacement_calo.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L342-L352)

- newROICalo+global:
For the central/global TRK+PF and addition of new ROI calo btagging: [here](python/customise_TRK_replacement_global_calo.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L354-L364)

- newGlobalCalo+global:
For the central/global TRK+PF and addition of new central/global TRK calo btagging: [here](python/customise_TRK_replacement_globalGlobal_calo.py)
An example on how to apply it on top of the GRun menu is [here](https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements/blob/Run3_ForJIRA/test/runHLTPaths_cfg.py#L366-L376)
