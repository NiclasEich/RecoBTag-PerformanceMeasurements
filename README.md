# RecoBTag-PerformanceMeasurements

## Software setup

```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_12_0_2_patch1
cd CMSSW_12_0_2_patch1/src
cmsenv

export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg HLTrigger/Configuration
git cms-addpkg CommonTools/RecoAlgos
git cms-addpkg RecoBTag/FeatureTools

git cherry-pick 89bfe7ede75fd673a1dfc906d91f351d69c6d822
git cherry-pick cf180d9be688925a29c7684db1fd88d9d5e6b7e7
git cherry-pick e682e2bda7cead0dc9394d8c992545d85c3c2c4c



#####git cms-merge-topic SWuchterl:devel_1120_pre6_TRKPlusBTV
git clone https://github.com/SWuchterl/JMETriggerAnalysis.git -o SWuchterl -b run3

# external data
mkdir -p ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data

# PFHC: preliminary HLT-PFHC for Run-3
cp /afs/cern.ch/work/m/missirol/public/run3/PFHC/PFHC_Run3Winter20_HLT_v01.db ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db

# JESC: preliminary HLT-JESCs for Run-3
cp /afs/cern.ch/work/m/missirol/public/run3/JESC/Run3Winter20_V2_MC/Run3Winter20_V2_MC.db ${CMSSW_BASE}/src/JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db

git clone -b cleanup-devel --recursive https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

find HLTrigger/Configuration/python/customizeHLTforPatatrack.py -type f -exec sed -i 's/process.hltSiPixelClustersLegacy = process.hltSiPixelClusters.clone()/process.hltSiPixelClustersLegacy = process.hltSiPixelClusters.clone(src = "hltSiPixelDigisLegacy")/g' {} \;

scram b -j12

```

## Instructions to run
### Offline

The Offline ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```, to run it with the latest defaults

```
cmsRun runBTagAnalyzer_cfg.py defaults=Run3 runOnData=(True or False, depending on your needs) maxEvents=10
```

### Online

The Offline ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```, to run it with the latest defaults

```
cmsRun runHLTBTagAnalyzer_cfg.py defaults=Run3 runOnData=(True or False, depending on your needs) maxEvents=10
```

## General information

The content of the output ntuple is by default empty and has to be configured according to your needs. The ```store*Variables``` options have been removed.
The new variable configuration can be customized in the file ```RecoBTag/PerformanceMeasurements/python/varGroups_cfi.py```.
New variables need also to be added (apart from adding them in the code) in ```RecoBTag/PerformanceMeasurements/python/variables_cfi.py```


## How to get the latest HLT configuration
For MC:
```
hltGetConfiguration /dev/CMSSW_12_0_0/GRun/V6 \
--full \
--offline \
--unprescale \
--mc \
--process HLT2 \
--globaltag auto:phase1_2021_realistic \
--max-events 10 \
> tmp.py
```
```
edmConfigDump tmp.py > HLT_dev_CMSSW_12_0_2_GRun_V6_configDump_MC.py
```
For data:
```
hltGetConfiguration /dev/CMSSW_12_0_0/GRun/V6 \
--full \
--offline \
--unprescale \
--data \
--process HLT2 \
--globaltag auto:run3_hlt \
--max-events 10 \
--customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
> tmp_data.py
```
```
edmConfigDump tmp_data.py > HLT_dev_CMSSW_12_0_2_GRun_V6_configDump_Data.py
```
