from FWCore.ParameterSet.VarParsing import VarParsing
import fnmatch

from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_MC import cms, process
from HLTrigger.Configuration.customizeHLTforRun3 import *
process = TRK_newTracking(process)
# process = MUO_newReco(process)
# process = BTV_roiCalo_roiPF_DeepCSV(process)
# process = BTV_roiCalo_roiPF_DeepJet(process)

### Drop EndPaths ###
els = process.__dict__
for el in list(els):
    if  ( ( type(els[el]) == cms.OutputModule) or (type(els[el]) == cms.EndPath)  or el == "PrescaleService" or el == "datasets" or el == "streams" ):
        #print("Deleting %s (%s)"%(el, type(els[el])))
        delattr(process, el)


process.source.fileNames = cms.untracked.vstring(["/store/mc/Run3Winter21DRMiniAOD/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/280001/cfd61936-8bcb-4c9a-ace7-1cf6ee79c09b.root"])
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.source.skipEvents = cms.untracked.uint32(997)
process.options.numberOfThreads = cms.untracked.uint32(1)
process.options.numberOfStreams = cms.untracked.uint32(1)


# # list of patterns to determine paths to keep
# keepPaths = [
#   'MC_*Jets*',
#   'MC_*MET*',
#   'MC_*AK8Calo*',
#   'MC_*DeepCSV*',
#   'MC_*DeepJet*',
#   # 'MC_*DeepCSV*ROI*',
#   # 'MC_*DeepJet*ROI*',
#   'MC_*Matching*',
#   # 'DST_Run3_PFScoutingPixelTracking_v*',
#   # 'HLT_PFJet*_v*',
#   # 'HLT_AK4PFJet*_v*',
#   # 'HLT_AK8PFJet*_v*',
#   # 'HLT_PFHT*_v*',
#   # 'HLT_PFMET*_PFMHT*_v*',
#   # 'HLT_*_*_v*',
# ]

# # list of paths that are kept
# listOfPaths = []
# print ("Keep paths:")
# print ('-'*108)
# # remove selected cms.Path objects from HLT config-dump
# for _modname in sorted(process.paths_()):
#     _keepPath = False
#     for _tmpPatt in keepPaths:
#         _keepPath = fnmatch.fnmatch(_modname, _tmpPatt)
#         if _keepPath: break
#     if _keepPath:
#         print ('{:<99} | {:<4} |'.format(_modname, '+'))
#         listOfPaths.append(_modname)
#         continue
#     _mod = getattr(process, _modname)
#     if type(_mod) == cms.Path:
#         process.__delattr__(_modname)
#         # if options.verbosity > 0:
#         #     print '{:<99} | {:<4} |'.format(_modname, '')
# print ('-'*108)

# remove FastTimerService
if hasattr(process, 'FastTimerService'):
  del process.FastTimerService
# remove MessageLogger
if hasattr(process, 'MessageLogger'):
  del process.MessageLogger
