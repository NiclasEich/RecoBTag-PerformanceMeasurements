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
    'replaceBTagMuPaths', True,
  VarParsing.multiplicity.singleton,
  VarParsing.varType.bool,
  'renaming BTagMu NoAlgo paths in reconstruction'
)
options.register(
    'loadROIparamsJson', None,
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  'Parameters to load for ROI reco'
)
options.register(
    'histogramJets', False,
  VarParsing.multiplicity.singleton,
  VarParsing.varType.bool,
  'Create histograms of calo and PF jets'
)
## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)

options.parseArguments()
globalTag = options.globalTag

update_jmeCalibs = False

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

###
### HLT configuration
###
if options.runOnData:
    if options.runTiming:
        from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_Data_timing import cms, process
    else:
        from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_Data import cms, process
else:
    from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_MC import cms, process


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
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_ROIPF import *
    process = customizeRun3_BTag_ROICalo_ROIPF(process, options.addDeepJet, options.replaceBTagMuPaths)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_noCaloROIPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_noCalo_ROIPF import *
    process = customizeRun3_BTag_noCalo_ROIPF(process, options.addDeepJet, options.replaceBTagMuPaths)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_noCaloROIPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True

elif options.reco == 'HLT_Run3TRK_noCaloROIPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF_Mu_optimized':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    import json
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True

    process.HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet927664VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet98837115DoublePFBTagDeepCSV1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+
        # process.HLTFastPrimaryVertexSequenceROIForBTag+
        # process.HLTBtagDeepCSVSequenceL3ROIForBTag+
        # process.hltBTagCaloDeepCSV1p56SingleROIForBTag+
        process.HLTAK4PFJetsSequenceROIForBTag+
        process.hltPFQuadJetLooseID15ROIForBTag+
        process.hltPFTripleJetLooseID71ROIForBTag+
        process.hltPFDoubleJetLooseID83ROIForBTag+
        process.hltPFSingleJetLooseID98ROIForBTag+
        process.HLTBtagDeepJetSequencePFROIForBTag+
        process.hltSelector6PFJetsROIForBTag+
        process.hltBTagPFDeepJet7p68Double6JetsROIForBTag+
        process.hltBTagPFDeepJet1p28Single6JetsROIForBTag+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5ROIForBTag+
        process.HLTEndSequence
    )

    roi_params = {}

    if options.loadROIparamsJson is not None:
        try:
            with open(options.loadROIparamsJson, "r") as roi_config_file:
                roi_params.update( json.load(roi_config_file))
        except FileNotFoundError as e:
            print("File {} could not be found. Using default values as fallback".format(roi_config_file))
            raise ValueError

    roi_defaults = {
            "beamSpot" : "hltOnlineBeamSpot",
            "deltaEta" : 0.5,
            "deltaPhi" : 0.5,
            "input" : "hltSelectorCentralJets20L1FastJeta",
            "maxNRegions" : 8,
            "maxNVertices" : 2,
            "measurementTrackerName" : "",
            "mode" : "VerticesFixed",
            "nSigmaZBeamSpot" : 3.0,
            "nSigmaZVertex" : 0.0,
            "originRadius" : 0.3,
            "precise" : True,
            "ptMin" : 0.8,
            "searchOpt" : True,
            "vertexCollection" : "hltTrimmedPixelVertices",
            "whereToUseMeasurementTracker" : "Never",
            "zErrorBeamSpot" : 0.5,
            "zErrorVetex" : 0.3
        }
    process.hltBTaggingRegion = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag(roi_params.get("beamSpot", roi_defaults["beamSpot"])),
            deltaEta = cms.double(roi_params.get("deltaEta", roi_defaults["deltaEta"])),
            deltaPhi = cms.double(roi_params.get("deltaPhi", roi_defaults["deltaPhi"])),
            input = cms.InputTag(roi_params.get("input", roi_defaults["input"])),
            maxNRegions = cms.int32(roi_params.get("maxNRegions", roi_defaults["maxNRegions"])),
            maxNVertices = cms.int32(roi_params.get("maxNVertices", roi_defaults["maxNVertices"])),
            measurementTrackerName = cms.InputTag(roi_params.get("measurementTrackerName", roi_defaults["measurementTrackerName"])),
            mode = cms.string(roi_params.get("mode", roi_defaults["mode"])),
            nSigmaZBeamSpot = cms.double(roi_params.get("nSigmaZBeamSpot", roi_defaults["nSigmaZBeamSpot"])),
            nSigmaZVertex = cms.double(roi_params.get("nSigmaZVertex", roi_defaults["nSigmaZVertex"])),
            originRadius = cms.double(roi_params.get("originRadius", roi_defaults["originRadius"])),
            precise = cms.bool(roi_params.get("precise", roi_defaults["precise"])),
            ptMin = cms.double(roi_params.get("ptMin", roi_defaults["ptMin"])),
            searchOpt = cms.bool(roi_params.get("searchOpt", roi_defaults["searchOpt"])),
            vertexCollection = cms.InputTag(roi_params.get("vertexCollection", roi_defaults["vertexCollection"])),
            whereToUseMeasurementTracker = cms.string(roi_params.get("whereToUseMeasurementTracker", roi_defaults["whereToUseMeasurementTracker"])),
            zErrorBeamSpot = cms.double(roi_params.get("zErrorBeamSpot", roi_defaults["zErrorBeamSpot"])),
            zErrorVetex = cms.double(roi_params.get("zErrorVetex", roi_defaults["zErrorVetex"]))
            )
    )
    process.hltPixelTracksCleanForBTag = cms.EDProducer("TrackWithVertexSelector",
        copyExtras = cms.untracked.bool(False),
        copyTrajectories = cms.untracked.bool(False),
        d0Max = cms.double(999.0),
        dzMax = cms.double(999.0),
        etaMax = cms.double(5.0),
        etaMin = cms.double(0.0),
        nSigmaDtVertex = cms.double(0.0),
        nVertices = cms.uint32(2),
        normalizedChi2 = cms.double(999999.0),
        numberOfLostHits = cms.uint32(999),
        numberOfValidHits = cms.uint32(0),
        numberOfValidPixelHits = cms.uint32(3),
        ptErrorCut = cms.double(5.0),
        ptMax = cms.double(9999.0),
        # ptMin = cms.double(0.8),
        ptMin =  cms.double(roi_params.get("ptMin", roi_defaults["ptMin"])),
        quality = cms.string("loose"),
        rhoVtx = cms.double(0.2),
        src = cms.InputTag("hltPixelTracks"),
        timeResosTag = cms.InputTag(""),
        timesTag = cms.InputTag(""),
        useVtx = cms.bool(True),
        vertexTag = cms.InputTag("hltTrimmedPixelVertices"),
        vtxFallback = cms.bool(True),
        zetaVtx = cms.double(0.3),
    )

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True

elif options.reco == 'HLT_Run3TRK_ROICaloGlobalPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = True
    process.HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet927664VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet98837115DoublePFBTagDeepCSV1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+
        # process.HLTFastPrimaryVertexSequenceROIForBTag+
        # process.HLTBtagDeepCSVSequenceL3ROIForBTag+
        # process.hltBTagCaloDeepCSV1p56SingleROIForBTag+
        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID71+
        process.hltPFDoubleJetLooseID83+
        process.hltPFSingleJetLooseID98+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet7p68Double6Jets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5+
        process.HLTEndSequence
    )

elif options.reco == 'HLT_Run3TRK_ROICaloGlobalPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    # process = BTV_noCalo_roiPF_DeepCSV(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = True

elif options.reco == 'HLT_Run3TRK_ROICaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_GlobalPF import *
    process = customizeRun3_BTag_ROICalo_GlobalPF(process, options.addDeepJet, options.replaceBTagMuPaths)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == 'HLT_Run3TRK_GlobalCaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_GlobalCalo_GlobalPF import *
    process = customizeRun3_BTag_GlobalCalo_GlobalPF(process, options.addDeepJet, options.replaceBTagMuPaths)
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

############################
#   old intermediate and temporary testing configurations
############################
# elif options.reco == 'HLT_Run3TRKPixelOnlyCleaned2':
#     # (d) Run-3 tracking: pixel only tracks and trimmed with PVs
#     from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
#     from RecoBTag.PerformanceMeasurements.customise_TRK import *
#     process = customizeHLTforRun3Tracking(process)
#     process = customisePFForPixelTracksCleaned(process, "hltPixelTracksCleanForBTag", vertex="hltTrimmedPixelVertices", nVertices = 2)
#     update_jmeCalibs = True
#     process = fixMenu(process)
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
# for _modname in process.endpaths_():
#     _mod = getattr(process, _modname)
#     if type(_mod) == cms.EndPath:
#        process.__delattr__(_modname)
#        # if options.verbosity > 0:
#        #    print '> removed cms.EndPath:', _modname


### Drop EndPaths ###
els = process.__dict__
for el in list(els):
    if  ( ( type(els[el]) == cms.OutputModule) or (type(els[el]) == cms.EndPath)  or el == "PrescaleService" or el == "datasets" or el == "streams" ):
        #print("Deleting %s (%s)"%(el, type(els[el])))
        delattr(process, el)

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
  # '*',
  # 'HLT_*',
  # 'HLT_QuadPFJet*DeepJet*',

  'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8',
  # 'HLT_QuadPFJet70_50_40_30_PFBTagParticleNet_2BTagSum0p65_v1',

  # 'HLT_*',
  # 'Alca_*',
  # 'DST_ZeroBias_v2',
  # 'DST_Physics_v7',
  'Status_OnGPU',
  'Status_OnCPU',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath',
]

removePaths = []


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
process.options.makeTriggerResults = cms.untracked.bool(True)
process.hltTrigReport = cms.EDAnalyzer("HLTrigReport",
    HLTriggerResults = cms.InputTag("TriggerResults","","@currentProcess"),
    ReferencePath = cms.untracked.string('HLTriggerFinalPath'),
    ReferenceRate = cms.untracked.double(100.0),
    reportBy = cms.untracked.string('job'),
    resetBy = cms.untracked.string('never'),
    serviceBy = cms.untracked.string('never')
)
process.HLTAnalyzerEndpath = cms.EndPath(process.hltTrigReport)
process.schedule.extend([process.HLTAnalyzerEndpath])
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#Set GT by hand:
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
if globalTag =="DEFAULT":
    if options.runOnData: globalTag = "122X_dataRun3_HLT_v1"
    else: globalTag = "122X_mcRun3_2021_realistic_v1"

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


## Output file
if options.histogramJets:
    process.TFileService = cms.Service("TFileService",
       fileName = cms.string("HHStudy.root")
    )
    from JMETriggerAnalysis.Common.jetHistogrammer_cfi import jetHistogrammer
    process.JetHistograms_hltSelectorCentralJets20L1FastJeta = jetHistogrammer.clone(
        srcCaloJets = 'hltSelectorCentralJets20L1FastJeta',
        srcPFJets   = 'hltAK4PFJetsROIForBTag',
        srcGenJets   = 'DUMMY',
        JetType      = 'CaloJet',
    )
    process.JetHistograms_hltAK4PFJetsROIForBTag = process.JetHistograms_hltSelectorCentralJets20L1FastJeta.clone(
        JetType = "PFJet"
    )
    # process.VertexHistograms_hltTrimmedPixelVertices = JetHistogrammer.clone(src = 'hltTrimmedPixelVertices')
    # process.VertexHistograms_hltVerticesPF = JetHistogrammer.clone(src = 'hltVerticesPF')
    # process.VertexHistograms_hltVerticesPFFilter = JetHistogrammer.clone(src = 'hltVerticesPFFilter')
    #
    process.jetMonitoringSeq = cms.Sequence(
       process.JetHistograms_hltSelectorCentralJets20L1FastJeta
       *process.JetHistograms_hltAK4PFJetsROIForBTag
    )
    process.jetMonitoringEndPath = cms.EndPath(process.jetMonitoringSeq)
    process.schedule.extend([process.jetMonitoringEndPath])

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
