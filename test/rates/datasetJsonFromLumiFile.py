#!/usr/bin/env python3
import json
import argparse
from JMETriggerAnalysis.NTuplizers.utils.common import *

parser = argparse.ArgumentParser(description='Make datafile from lumi file')
parser.add_argument('input_file', metavar='i', type=str, 
                    help='input file')
parser.add_argument('output_file', metavar='o', type=str, 
                    help='output file', default="tmpData.json")
parser.add_argument('--verbosity', '-v', type=int, 
                    help='verbosity', default=1)
args = parser.parse_args()

outputFile = args.output_file 
verbosity = args.verbosity

dset = '/EphemeralHLTPhysics1/Run2018D-v1/RAW'
# run = 323775
# lumiBlocks = [ls for ls in range(52,152) if ls not in [71, 72, 78, 82, 83]]

with open(args.input_file, "r") as input_file:
    inp_json = json.load(input_file)
if len(inp_json.keys()) > 1:
    raise NotImplementedError("This script currently only supports single run lumi files!")
run = list(inp_json.keys())[0]
lumiBlocks = [item for a,b in inp_json[run] for item in list(range(a, b+1))]
print("Running on run #{}".format(run))
print("Luminosity-blockas:")
print(lumiBlocks)


###

dsetDict = {"DAS": dset, 'files': []}

edmFiles = []
for lumiBlock in lumiBlocks:
  edmFilesTmp = get_output('dasgoclient -query "file run='+str(run)+' dataset='+dset+' lumi='+str(lumiBlock)+'"')
  edmFilesTmp = [edmFile.decode('utf-8').replace('\n', '') for edmFile in edmFilesTmp]
  edmFilesTmp = [edmFile for edmFile in edmFilesTmp if edmFile]
  edmFiles += edmFilesTmp

  if verbosity > 0:
    print (edmFilesTmp)

edmFiles = sorted(list(set(edmFiles)))

for edmFile in edmFiles:

  edmFileNEvents = get_output('dasgoclient -query "file='+edmFile+' | grep file.nevents"')
  edmFileNEvents = [nEvt.decode('utf-8').replace('\n', '') for nEvt in edmFileNEvents]
  edmFileNEvents = [nEvt for nEvt in edmFileNEvents if nEvt]

  if len(edmFileNEvents) != 1:
    raise RuntimeError(edmFileNEvents)

  dsetDict['files'] += [{
    'file': edmFile,
    'nevents': int(edmFileNEvents[0]),
    'parentFiles_1': [],
    'parentFiles_2': [],
  }]

  if verbosity > 0:
    print (dsetDict['files'][-1])

json.dump(dsetDict, open(outputFile, 'w'), sort_keys=True, indent=2)
