# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_8
* **Step #1** : create local CMSSW area and add the relevant packages.
```shell
scramv1 project CMSSW CMSSW_11_1_8
cd scramv1 project CMSSW CMSSW_11_1_8/src
eval `scramv1 runtime -sh`

git cms-init

# [optional; required only for  NTuple production]
# fix for GenFilters
git cms-merge-topic Sam-Harper:MCStartFilterInputCollFix_1110pre6

# [optional; MinBias/QCD Stitching required only for  NTuple production]
mkdir -p HLTrigger
git clone https://github.com/veelken/mcStitching.git HLTrigger/mcStitching

# basic JME setup including customizers
git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

# BTV setup
git clone -b PhaseIIOnline --depth 1 https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

# It is possible that you have to try to compile twice because of the TRK merge topic.
scram b -j10

```



* **Step #2** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
e.g.:
`cmsRun runHLTBTagAnalyzer_PhaseII_cfg.py maxEvents=5 reco=HLT_TRKv06p1_TICL BTVreco=cutsV2`
