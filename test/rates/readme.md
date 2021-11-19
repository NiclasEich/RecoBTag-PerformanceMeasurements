Quick set of instructions for HLT-rate estimates on 2018 pp data.

Ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SteamHLTRatesCalculation

```
cd rates/

# test locally
cmsRun hltResults_cfg.py maxEvents=500 reco=HLT_Run3TRK output=tmp.root

# create area(s) with batch-job submission
./makeEDMFiles_hltTriggerResults_210611.sh tmpout

# submit jobs to the batch system
bmonitor -i tmpout -r

# when EDM outputs are available, write raw and pure counts of HLT paths to .json file
./triggerResultsCounts.py \
  -i tmpout/job_*/out_*.root \
  -o rates.json \
  -l data/json_323775.txt \
  -p MYHLT -v 10

# print to stdout the rates of selected trigger paths
./triggerRates.py \
  -p 1100 -t 'HLT_*' \
  -i rates.json
```
