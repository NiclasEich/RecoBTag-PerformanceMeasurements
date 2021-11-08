from FWCore.ParameterSet.VarParsing import VarParsing

import fnmatch
###############################
####### Parameters ############
###############################

options = VarParsing ('analysis')

options.register('runOnData', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('reportEvery', 10,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=1)"
)
options.register('wantSummary', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Print out trigger and timing summary"
)
options.register('dumpPython', None,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'Dump python config, pass SaveName.py'
)
options.register('globalTag', 'DEFAULT',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MC global tag, no default value provided"
)
options.register('runTiming', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'run timing instead of rates'
)
options.register('numThreads', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    'number of threads'
)
options.register('numStreams', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    'number of streams'
)
options.register(
    'reco', 'HLT_GRun',
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  'keyword to define HLT reconstruction'
)
options.register(
    'addDeepJet', True,
  VarParsing.multiplicity.singleton,
  VarParsing.varType.bool,
  'add DeepJet paths to reconstruction'
)
options.register(
    'ptMinThreshold', 0.9,
  VarParsing.multiplicity.singleton,
  VarParsing.varType.float,
  'pt min for tracks - to study'
)
options.setDefault('ptMinThreshold', 0.9)
## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)

options.parseArguments()
globalTag = options.globalTag

update_jmeCalibs = False

pathsWithCaloAndPF = [
    "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",
    "PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v",
    "HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v",
    "HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v",
    "HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v",
    "HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v",
    "HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v",
    "HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v",
    "HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v",
    "HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v",
    "HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v",
    "HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v",
    "HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v",
    "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v"
]
pathsWithCaloAndPFROIForBTag = [p.replace("_v", "ROIForBTag_v") for p in pathsWithCaloAndPF]

pathsWithOnlyCalo = [
    "HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v",
    "HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v",
    "HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v",
    "HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v",
    "HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v",
    "HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v",
    "HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v",
    "HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v",
    "HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v",
    "HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v",
    "HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v",
    "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v",
    "HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v",
    "HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1_v",
    "HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v",
    "HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v"
]

def fixMenu(process):
	if hasattr(process, 'hltEG60R9Id90CaloIdLIsoLDisplacedIdFilter'):
		process.hltEG60R9Id90CaloIdLIsoLDisplacedIdFilter.inputTrack = 'hltMergedTracks'
	if hasattr(process, 'hltIter1ClustersRefRemoval'):
		process.hltIter1ClustersRefRemoval.trajectories = 'hltMergedTracks'
	return process

def prescale_path(path,ps_service):
  for pset in ps_service.prescaleTable:
      if pset.pathName.value() == path.label():
          pset.prescales = [0]*len(pset.prescales)

def deleteCaloOnlyPaths(process):
    deleteCaloProcesses = pathsWithOnlyCalo
    print("Deleting CaloOnly paths")
    for _tmpPathName in deleteCaloProcesses:
        attributes = dir(process)
        for attribute in attributes:
            if _tmpPathName in attribute:
                hit_attr = attribute
                print("Deleting {}".format(hit_attr))
                process.__delattr__(hit_attr)
    return process

def deleteCaloPrestage(process):
    deleteDeepCSVpreselection = pathsWithCaloAndPF
    print("Deleteing deepCSV prestage")
    for _tmpPathName in deleteDeepCSVpreselection:
        attributes = dir(process)
        # have to do a comparison since we do not have the
        # exact version number like DeepCSV_p71_vX
        hit = False
        deepCSVmodules = []
        for attribute in attributes:
            if _tmpPathName in attribute:
                hit_attr = attribute
                hit = True
            try:
                if getattr(process, attribute).parameters_()["JetTags"].value() == 'hltDeepCombinedSecondaryVertexBJetTagsCalo:probb':
                    deepCSVmodules.append( attribute )
            except KeyError:
                pass
            except AttributeError:
                pass
        if hit is True:
            print("Changing path {}".format(_tmpPathName))
            _tmpPath = getattr(process, hit_attr)
            _tmpPath.remove(getattr(process, "HLTBtagDeepCSVSequenceL3"))
            _tmpPath.remove(getattr(process, "HLTFastPrimaryVertexSequence"))
            for deepCSVmodule in deepCSVmodules:
                _tmpPath.remove(getattr(process, deepCSVmodule))
    return process

###
### HLT configuration
###
if options.runOnData:
    if options.runTiming:
        from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_1_0_GRun_configDump_Data_timing import cms, process
    else:
        from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_1_0_GRun_configDump_Data import cms, process
else:
    from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_1_0_GRun_configDump_MC import cms, process


if options.reco == 'HLT_GRun_oldJECs':
    # default GRun menu (Run 2 configurations)
    update_jmeCalibs = False

elif options.reco == 'HLT_GRun':
    # default GRun menu (Run 2 configurations) + new PFHCs and JECs
    update_jmeCalibs = True

elif options.reco == 'HLT_GRun_PatatrackQuadruplets':
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Quadruplets only) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrack
    process = customizeHLTforPatatrack(process)
    update_jmeCalibs = True
    # process = fixMenu(process)

elif options.reco == 'HLT_GRun_PatatrackTriplets':
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Triplets+Quadruplets) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrackTriplets
    process = customizeHLTforPatatrackTriplets(process)
    update_jmeCalibs = True
    # process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK' or options.reco == 'HLT_Run3TRK_Pt':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    if options.reco == 'HLT_Run3TRK_Pt': process = customizePt(process, options.ptMinThreshold)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_ROIPF import *
    process = customizeRun3_BTag_ROICalo_ROIPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_ROICaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_GlobalPF import *
    process = customizeRun3_BTag_ROICalo_GlobalPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRKNoCaloJetsWithSubstitutions':
    # Run-3 global/central TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging
    # + removal of Calo Btagging
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = fixMenu(process)
    process = deleteCaloOnlyPaths(process)
    process = deleteCaloPrestage(process)

elif options.reco == 'HLT_Run3TRKNoCaloJets':
    # Run-3 global/central TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = fixMenu(process)
    process = deleteCaloOnlyPaths(process)
############################
#   old intermediate and temporary testing configurations
############################
# elif options.reco == 'HLT_Run3TRKPixelOnly':
#     # (c) Run-3 tracking: pixel only tracks
#     from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
#     from RecoBTag.PerformanceMeasurements.customise_TRK import *
#     process = customizeHLTforRun3Tracking(process)
#     process = customisePFForPixelTracks(process)
#     process = fixMenu(process)
#
# elif options.reco == 'HLT_Run3TRKPixelOnlyCleaned2':
#     # (d) Run-3 tracking: pixel only tracks and trimmed with PVs
#     from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
#     from RecoBTag.PerformanceMeasurements.customise_TRK import *
#     process = customizeHLTforRun3Tracking(process)
#     process = customisePFForPixelTracksCleaned(process, "hltPixelTracksCleanForBTag", vertex="hltTrimmedPixelVertices", nVertices = 2)
#     update_jmeCalibs = True
#     process = fixMenu(process)

elif options.reco == 'HLT_Run3TRKForBTag':
    # Run-3 ROI TRK+PF reconstruction
    from RecoBTag.PerformanceMeasurements.customise_TRK import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks(process, clean=True, vertex="hltTrimmedPixelVertices", nVertices = 2)
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRKForBTag_Replacement':
    # Run-3 ROI TRK+PF reconstruction
    from RecoBTag.PerformanceMeasurements.customise_TRK_replacement import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_Replacement(process)
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRKForBTag_DeepJet':
    # Run-3 global/central TRK+PF reconstruction + DeepJet in PF btagging paths
    from RecoBTag.PerformanceMeasurements.customise_TRK_deepjet import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    from RecoBTag.PerformanceMeasurements.customise_TRK import addDeepJet
    process = addDeepJet(process, doPF = True, doPuppi = False)
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_DeepJet(process)
    process = fixMenu(process)


elif options.reco == 'HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets':
    # Run-3 ROI TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging
    from RecoBTag.PerformanceMeasurements.customise_TRK_replacement import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_Replacement(process)
    process = fixMenu(process)

    process = deleteCaloOnlyPaths(process)

elif options.reco == 'HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets_NewCalo':
    # Run-3 ROI TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging (see below)
    # + replacement of Calo Btagging with new ROI tracks
    from RecoBTag.PerformanceMeasurements.customise_TRK_replacement_calo import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_Replacement_calo(process)
    process = fixMenu(process)

    process = deleteCaloOnlyPaths(process)

elif options.reco == 'HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets_NewCalo_Global':
    # Run-3 global/central TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging (see below)
    # + replacement of Calo Btagging with new ROI tracks
    from RecoBTag.PerformanceMeasurements.customise_TRK_replacement_global_calo import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_Replacement_global_calo(process)
    process = fixMenu(process)

    process = deleteCaloOnlyPaths(process)

elif options.reco == 'HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets_NewGlobalCalo_Global':
    # Run-3 global/central TRK+PF reconstruction
    # + removal of all paths with CaloOnlyBtagging (see below)
    # + replacement of Calo Btagging with global/central TRK+PF
    from RecoBTag.PerformanceMeasurements.customise_TRK_replacement_globalGlobal_calo import *
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    process = customiseRun3BTagRegionalTracks_Replacement_global_globalCalo(process)
    process = fixMenu(process)

    process = deleteCaloOnlyPaths(process)

else:
  raise RuntimeError('keyword "reco = '+options.reco+'" not recognised')


# remove cms.OutputModule objects from HLT config-dump
for _modname in process.outputModules_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.OutputModule:
       process.__delattr__(_modname)
       # if options.verbosity > 0:
       #    print '> removed cms.OutputModule:', _modname

# remove cms.EndPath objects from HLT config-dump
for _modname in process.endpaths_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.EndPath:
       process.__delattr__(_modname)
       # if options.verbosity > 0:
       #    print '> removed cms.EndPath:', _modname


# list of patterns to determine paths to keep
keepPaths = [
  # 'MC_*Jets*',
  # 'MC_*PFJets*',
  # 'MC_*CaloJets*',
  # 'MC_*MET*',
  # 'MC_*AK8Calo*',
  # 'MC_*DeepCSV*',
  # 'MC_*CaloBTagDeepCSV*',
  # 'MC_*PFBTagDeepCSV*',
  # 'MC_ReducedIterativeTracking*',
  # 'MC_*DeepJet*',
  # 'HLT_PFJet*_v*',
  # 'HLT_AK4PFJet*_v*',
  # 'HLT_AK8PFJet*_v*',
  # 'HLT_PFHT*_v*',
  # 'HLT_PFMET*_PFMHT*_v*',
  # 'HLT_*DeepCSV*_v*',
  # 'HLT_*_v*',
  '*',
]

removePaths = []
# removePaths+=pathsWithOnlyCalo
# if options.reco == "HLT_Run3TRKForBTag_Replacement" or options.reco=="HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets" or options.reco=="HLT_Run3TRKForBTag_Replacement_Run3TRKNoCaloJets_NewCalo":
#     removePaths+=pathsWithCaloAndPF
#
# print("Deleting removePaths")
# for _tmpPathName in removePaths:
#     attributes = dir(process)
#     for attribute in attributes:
#         if _tmpPathName in attribute:
#             hit_attr = attribute
#             print("Deleting {}".format(hit_attr))
#             process.__delattr__(hit_attr)

# list of paths that are kept
listOfPaths = []
print ("Keep paths:")
print ('-'*108)
for _modname in sorted(process.paths_()):
    _keepPath = False
    _removePath = False
    for _tmpPatt in keepPaths:
        _keepPath = fnmatch.fnmatch(_modname, _tmpPatt)
        for _tmpPatt_r in removePaths:
            _removePath = fnmatch.fnmatch(_modname, _tmpPatt_r)
        # if _keepPath: break
        if _keepPath and not _removePath: break
    if _keepPath and not _removePath:
        print ('{:<99} | {:<4} |'.format(_modname, '+'))
        if _keepPath and not _removePath:
            listOfPaths.append(_modname)
        continue
    _mod = getattr(process, _modname)
    if type(_mod) == cms.Path:
        process.__delattr__(_modname)
        # if options.verbosity > 0:
        #     print '{:<99} | {:<4} |'.format(_modname, '')
        print ('{:<99} | {:<4} |'.format(_modname, ''))
print ('-'*108)

# remove FastTimerService
if hasattr(process, 'FastTimerService'):
  del process.FastTimerService
# remove MessageLogger
if hasattr(process, 'MessageLogger'):
  del process.MessageLogger

if "HLT_Run3TRKPixelOnly" in options.reco:
    process = customizeMinHitsAndPt(process)
    process = customizePt(process, options.ptMinThreshold)

if update_jmeCalibs:
    ## ES modules for PF-Hadron Calibrations
    import os
    from CondCore.CondDB.CondDB_cfi import CondDB as _CondDB

    process.pfhcESSource = cms.ESSource('PoolDBESSource',
      _CondDB.clone(connect = 'sqlite_fip:JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db'),
      toGet = cms.VPSet(
        cms.PSet(
          record = cms.string('PFCalibrationRcd'),
          tag = cms.string('PFCalibration_HLT_mcRun3_2021'),
          label = cms.untracked.string('HLT'),
        ),
      ),
    )

    process.pfhcESPrefer = cms.ESPrefer('PoolDBESSource', 'pfhcESSource')
    ## ES modules for HLT JECs
    process.jescESSource = cms.ESSource('PoolDBESSource',
      _CondDB.clone(connect = 'sqlite_fip:JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db'),
     toGet = cms.VPSet(
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4CaloHLT'),
          label = cms.untracked.string('AK4CaloHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFClusterHLT'),
          label = cms.untracked.string('AK4PFClusterHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFHLT'),
          label = cms.untracked.string('AK4PFHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFHLT'),#!!
          label = cms.untracked.string('AK4PFchsHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFPuppiHLT'),
          label = cms.untracked.string('AK4PFPuppiHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8CaloHLT'),
          label = cms.untracked.string('AK8CaloHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFClusterHLT'),
          label = cms.untracked.string('AK8PFClusterHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFHLT'),
          label = cms.untracked.string('AK8PFHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFHLT'),#!!
          label = cms.untracked.string('AK8PFchsHLT'),
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag = cms.string('JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFPuppiHLT'),
          label = cms.untracked.string('AK8PFPuppiHLT'),
        ),
      ),
    )
    process.jescESPrefer = cms.ESPrefer('PoolDBESSource', 'jescESSource')

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery


if options.inputFiles:
    process.source.fileNames = options.inputFiles
process.source.secondaryFileNames = cms.untracked.vstring()


## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

## Options and Output Report
process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(options.wantSummary),
    # allowUnscheduled = cms.untracked.bool(True)
)

if options.runTiming:
    # multi-threading settings
    process.options.numberOfThreads = cms.untracked.uint32(options.numThreads if (options.numThreads > 1) else 1)
    process.options.numberOfStreams = cms.untracked.uint32(options.numStreams if (options.numStreams > 1) else 1)
    process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32(10240)
else:
    # multi-threading settings
    process.options.numberOfThreads = cms.untracked.uint32(options.numThreads if (options.numThreads > 1) else 1)
    process.options.numberOfStreams = cms.untracked.uint32(options.numStreams if (options.numStreams > 1) else 1)

#Set GT by hand:
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
if globalTag =="DEFAULT":
    if options.runOnData: globalTag = "121X_dataRun3_HLT_v9"
    else: globalTag = "121X_mcRun3_2021_realistic_v15"

process.GlobalTag.globaltag = globalTag


if options.runTiming:
    #timing test
    from HLTrigger.Timer.FastTimer import customise_timer_service_print,customise_timer_service,customise_timer_service_singlejob
    # process = customise_timer_service_print(process)
    # process = customise_timer_service(process)
        # remove any instance of the FastTimerService
    if 'FastTimerService' in process.__dict__:
        del process.FastTimerService

    # instrument the menu with the FastTimerService
    process.load("HLTrigger.Timer.FastTimerService_cfi")

    # print a text summary at the end of the job
    process.FastTimerService.printEventSummary        = False
    process.FastTimerService.printRunSummary          = False
    process.FastTimerService.printJobSummary          = True
    # enable DQM plots
    process.FastTimerService.enableDQM                = True
    # enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
    process.FastTimerService.enableDQMbyPath          = True
    # enable per-module DQM plots
    process.FastTimerService.enableDQMbyModule        = True
    # enable DQM plots vs lumisection
    process.FastTimerService.enableDQMbyLumiSection   = True
    process.FastTimerService.dqmLumiSectionsRange     = 2500    # lumisections (23.31 s)
    # set the time resolution of the DQM plots
    # process.FastTimerService.dqmTimeRange             = 1000.   # ms
    process.FastTimerService.dqmTimeRange             = 5000.   # ms
    process.FastTimerService.dqmTimeResolution        =    5.   # ms
    # process.FastTimerService.dqmPathTimeRange         =  100.   # ms
    process.FastTimerService.dqmPathTimeRange         =  1000.   # ms
    process.FastTimerService.dqmPathTimeResolution    =    0.5  # ms
    process.FastTimerService.dqmModuleTimeRange       =   40.   # ms
    process.FastTimerService.dqmModuleTimeResolution  =    0.2  # ms
    # set the base DQM folder for the plots
    process.FastTimerService.dqmPath                  = "HLT/TimerService"
    process.FastTimerService.enableDQMbyProcesses     = False
    # enable text dump
    if not hasattr(process,'MessageLogger'):
        process.load('FWCore.MessageService.MessageLogger_cfi')
    # process.MessageLogger.categories.append('FastReport')
    process.MessageLogger.cerr.FastReport = cms.untracked.PSet( limit = cms.untracked.int32( 10000000 ) )
    # save the DQM plots in the DQMIO format
    process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
        fileName = cms.untracked.string("DQM.root")
    )
    process.FastTimerOutput = cms.EndPath(process.dqmOutput)
    # process.schedule.append(process.FastTimerOutput)

    # process = customise_timer_service_singlejob(process)
    process.FastTimerService.dqmTimeRange            = 20000.
    process.FastTimerService.dqmTimeResolution       =    10.
    process.FastTimerService.dqmPathTimeRange        = 10000.
    process.FastTimerService.dqmPathTimeResolution   =     5.
    # process.FastTimerService.dqmModuleTimeRange      =  1000.
    process.FastTimerService.dqmModuleTimeRange      =  5000.
    process.FastTimerService.dqmModuleTimeResolution =     1.
    # process.dqmOutput.fileName = cms.untracked.string(options.output)


# dump content of cms.Process to python file
if options.dumpPython is not None:
   open(options.dumpPython, 'w').write(process.dumpPython())

print ('')
print ('option: reco =', options.reco)
print ('option: dumpPython =', options.dumpPython)
print ('')
print ('process.GlobalTag =', process.GlobalTag.globaltag)
print ('process.source =', process.source.dumpPython())
print ('process.maxEvents =', process.maxEvents.input)
print ('-------------------------------')
