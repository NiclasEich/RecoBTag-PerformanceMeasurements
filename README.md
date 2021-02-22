# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_7
* **Step #1** : create local CMSSW area and add the relevant packages.
```shell
scramv1 project CMSSW CMSSW_11_1_7
cd scramv1 project CMSSW CMSSW_11_1_7/src
eval `scramv1 runtime -sh`

git cms-init

# [optional; required only for  NTuple production]
# fix for GenFilters
git cms-merge-topic Sam-Harper:MCStartFilterInputCollFix_1110pre6

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

git cms-merge-topic emilbols:BTV_CMSSW_11_1_X

# [optional; MinBias/QCD Stitching required only for  NTuple production]
mkdir -p HLTrigger
git clone https://github.com/veelken/mcStitching.git HLTrigger/mcStitching

# basic JME setup including customizers
git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2

# BTV setup
git clone -b PhaseIIOnline --depth 1 https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

# Get the latest DeepCSV and DeepJet training files. not pretty, but works:
cd RecoBTag/Combined/data/DeepFlavour_Phase2/
wget -O DeepJet_pv3d_nt.onnx https://github.com/mneukum/cmssw/blob/BTV_CMSSW_11_1_2_with_timing/RecoBTag/Combined/data/DeepFlavour_Phase2/DeepJet_pv3d_nt.onnx?raw=true
mv model.onnx model.onnx.ori
mv DeepJet_pv3d_nt.onnx model.onnx
cd ..
wget -O DeepCSV_pv3d_nt.onnx https://raw.githubusercontent.com/mneukum/cmssw/BTV_CMSSW_11_1_2_with_timing/RecoBTag/Combined/data/DeepCSV_Phase2_pv3d_no_timing.json
mv DeepCSV_PhaseII.json DeepCSV_PhaseII.json.ori
mv DeepCSV_pv3d_nt.onnx DeepCSV_PhaseII.json

cd ../../..

# It is possible that you have to try to compile twice because of the TRK merge topic.
scram b -j10

```



* **Step #2** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
e.g.:
`cmsRun runHLTBTagAnalyzer_PhaseII_cfg.py maxEvents=5 reco=HLT_TRKv06p1_TICL BTVreco=cutsV2`
