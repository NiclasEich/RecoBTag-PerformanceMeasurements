#!/usr/bin/env python3
import json

from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_Data_NoOutput_configDump import cms, process

outputFile = 'triggersForPureRate.json'

triggersForPureRate = []
for streamName in process.streams.parameterNames_():
  if streamName.startswith('Physics'):
    for dsetName in getattr(process.streams, streamName):
      for trigName in getattr(process.datasets, dsetName):
        if trigName.startswith('HLT_'):
          triggersForPureRate.append(trigName)
triggersForPureRate = list(set(triggersForPureRate))

json.dump(sorted(triggersForPureRate), open(outputFile, 'w'), sort_keys=True, indent=2)
