#!/bin/bash

OUTCFG="${CMSSW_BASE}"/src/RecoBTag/PerformanceMeasurements/python/Configs/HLT_dev_CMSSW_12_0_2_GRun_V6_Data_NoOutput_configDump.py

inputFiles=(
  # run=323775, ls=[53,62]
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D5D2CF9C-2557-4243-B42E-4345100839DA.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/FBF117EE-5699-F147-BBFC-07815D5A2582.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B26AAAB6-F701-0C44-860E-CAB8EDC85876.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D20C7DA2-996F-B54E-AAE0-DA110878E4BA.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B14F28B7-490B-DA4E-8EA4-AF1B0C07756C.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/A27DFA33-8FCB-BE42-A2D2-1A396EEE2B6E.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/AC589D97-A8ED-2B4C-B961-5595C88A8CEF.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/FB01AEC2-BEB9-E14D-8F7A-512995B8ADD1.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C707212D-9264-0F43-9937-A0053CBFEDDE.root
  /eos/cms/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/65EA98C3-88C1-5A43-8152-824F3169174E.root
)

printf -v inputFilesStr '%s,' "${inputFiles[@]}"

# hltGetConfiguration /dev/CMSSW_12_2_0_pre2/GRun --full --offline --no-output --data --process MYHLT --type GRun \
#  --prescale 2.0e34+ZB+HLTPhysics --globaltag auto:run3_hlt_GRun --input "${inputFilesStr%,}" --max-events -1 --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input \
#  > tmpRates.py
hltGetConfiguration /dev/CMSSW_12_2_0_pre2/GRun --full --offline --no-output --data --process HLT2 --type GRun \
 --prescale 2.0e34+ZB+HLTPhysics --globaltag auto:run3_hlt --max-events -1 --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input --eras Run2_2018 \
 > tmpRates.py

 # a. comment out the following lines:

# _customInfo = {}
# _customInfo['menuType'  ]= "GRun"
# _customInfo['globalTags']= {}
# _customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
# _customInfo['globalTags'][False] = "auto:run2_mc_GRun"
# _customInfo['inputFiles']={}
# _customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
# _customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
# _customInfo['maxEvents' ]=  100
# _customInfo['globalTag' ]= "auto:run2_hlt_GRun"
# _customInfo['inputFile' ]=  ['file:RelVal_Raw_GRun_DATA.root']
# _customInfo['realData'  ]=  True
# from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
# process = customizeHLTforAll(process,"GRun",_customInfo)

# then call

# edmConfigDump .tmp.py > "${OUTCFG}"
# rm -f .tmp.py

# cat >> "${OUTCFG}" <<@EOF

# from HLTrigger.Configuration.customizeHLTforCMSSW import customiseFor2018Input
# customiseFor2018Input(process)
# @EOF
