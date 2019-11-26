# RecoBTag-PerformanceMeasurements

## Software setup

```
cmsrel CMSSW_11_0_0_pre7
cd CMSSW_11_0_0_pre7/src
cmsenv

git cms-init

git cms-addpkg RecoBTag
git cms-addpkg PhysicsTools/PatAlgos
git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
git clone https://github.com/SWuchterl/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements
cd RecoBTag/PerformanceMeasurements/
git checkout -b PhaseIIOffline origin/PhaseIIOffline

scram b -j8

to run: goto RecoBTag/PerformanceMeasurements/test/
source runMINIAOD.sh

```

The ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```, to run it for the 2018 Ultimate SF campaign:

```
cmsRun runBTagAnalyzer_cfg.py defaults=2018_Ultimate runOnData=(True or False, depending on your needs)
```

When running on data please note the different global tag between runs A-C and run D in ```RecoBTag/PerformanceMeasurements/python/defaults/2018_Ultimate.py```

To run the tests for integrating changes run:

```
cd RecoBTag/PerformanceMeasurements/test/
./run_tests.sh
```
The content of the output ntuple is by default empty and has to be configured according to your needs. The ```store*Variables``` options have been removed.
The new variable configuration can be customized in the file ```RecoBTag/PerformanceMeasurements/python/varGroups_cfi.py```.
New variables need also to be added (apart from adding them in the code) in ```RecoBTag/PerformanceMeasurements/python/variables_cfi.py```


For running on the HLT one needs to use RAW and there are very few options availbe here is the command I have working:

```
cmsRun ./runHLTBTagAnalyzer_cfg.py runOnData=True groups="HLTEventInfo,HLTJetInfo,HLTTagVar,HLTJetTrack,HLTJetSV,HLTCSVTagVar"
```
