from FWCore.ParameterSet.VarParsing import VarParsing
import fnmatch
###############################
####### Parameters ############
###############################

options = VarParsing ("analysis")

options.register("runOnData", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register("outFilename", "TwoFileTree.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
)
options.register("reportEvery", 10,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=1)"
)
options.register("wantSummary", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Print out trigger and timing summary"
)
options.register("dumpPython", None,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Dump python config, pass SaveName.py"
)
options.register("globalTag", "FIXME",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MC global tag, no default value provided"
)
options.register("runEventInfo", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run Event Info"
)
options.register("processStdAK4Jets", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process standard AK4 jets"
)
options.register("useTrackHistory", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "uses track history, for GEN-SIM-RECODEBUG samples only"
)
options.register("produceJetTrackTree", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run info for tracks associated to jets : for commissioning studies"
)
options.register("produceAllTrackTree", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Produce all track tree"
)

options.register("fillPU", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Fill PU"
)
### Options for upgrade studies
# Change hits requirements
options.register("changeMinNumberOfHits", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Change minimum number of tracker hits"
)
options.register("minNumberOfHits", 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Minimum number of tracker hits"
)
# Change eta for extended forward pixel coverage
options.register("maxJetEta", 4.5,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum jet |eta| (default is 4.5)"
)
options.register("minJetPt", 25.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum jet pt (default is 20)"
)
options.register("usePrivateJEC", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use JECs from private SQLite files")
options.register("jecDBFileMC", "FIXME",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "SQLite filename for JECs, no default value provided")
options.register("jecDBFileData", "FIXME",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "SQLite filename for JECs, no default value provided")
options.register("isReHLT", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "80X reHLT samples")
options.register("JPCalibration", "FIXME",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "JP Calibration pyload to use")
options.register("runJetVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Jet Variables")
options.register("runCaloJetVariables", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Jet Variables")
options.register("runPuppiJetVariables", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Jet Variables")
options.register("runTagVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Tag Variables")
options.register("runQuarkVariables", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run c/b quark Variables")
options.register("runHadronVariables", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Hadron Variables")
options.register("runGenVariables", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run Gen Variables")
options.register("runCSVTagVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run CSV TaggingVariables")
options.register("runCSVTagTrackVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run CSV Tagging Track Variables")
options.register("runDeepFlavourTagVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run DeepFlavour TaggingVariables")
options.register("runPFElectronVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run PF Electron Variables")
options.register("runPFMuonVariables", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run PF Muon Variables")
options.register("defaults", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "baseline default settings to be used")
options.register("eras", [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    "era modifiers to be used to be used")
options.register("groups", [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    "variable groups to be stored")
options.register(
    "skipEvents", 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "skip N events")

options.register("runTiming", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "run timing instead of rates")
options.register("numThreads", 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "number of threads")
options.register("numStreams", 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "number of streams")
options.register(
    "reco", "HLT_GRun",
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  "keyword to define HLT reconstruction"
)

## "maxEvents" is already registered by the Framework, changing default value
options.setDefault("maxEvents", -1)

options.parseArguments()
if options.defaults:
	from importlib import import_module
	try:
		defaults = import_module("RecoBTag.PerformanceMeasurements.defaults_HLT.%s" % options.defaults)
	except ImportError:
		raise ValueError("The default settings named %s.py are not present in PerformanceMeasurements/python/defaults_HLT/" % options.defaults)
	if not hasattr(defaults, "common") or not isinstance(defaults.common, dict):
		raise RuntimeError("the default file %s.py does not contain a dictionary named common" % options.defaults)
	items = defaults.common.items()
	if hasattr(defaults, "data") and options.runOnData:
		if not isinstance(defaults.data, dict):
			raise RuntimeError("the default file %s.py contains an object called \"data\" which is not a dictionary" % options.defaults)
		items.extend(defaults.data.items())
	if hasattr(defaults, "mc") and not options.runOnData:
		if not isinstance(defaults.mc, dict):
			raise RuntimeError("the default file %s.py contains an object called \"mc\" which is not a dictionary" % options.defaults)
		items.extend(defaults.mc.items())
	for key, value in items:
		if key not in options._beenSet:
			raise ValueError("The key set by the defaults: %s does not exist among the cfg options!" % key)
		elif not options._beenSet[key]:
			if key == "inputFiles" and options.inputFiles: continue #skip input files that for some reason are never considered set
			print ("setting default option for", key)
			setattr(options, key, value)

from RecoBTag.PerformanceMeasurements.HLTTwoFileBTagAnalyzer_cff import *
btagana_tmp = HLTTwoFileBTagAnalyzer.clone()
print("Storing the variables from the following groups:")
options_to_change = set() #store which swtiches we need on
for requiredGroup in options.groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var or "PuppiJet." in var:
            var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print("WARNING: The group " + requiredGroup + " was not found")

#change values accordingly
for switch in options_to_change:
  if switch in ["runTagVariablesSubJets","runCSVTagVariablesSubJets"]:
      continue
  elif switch not in options._beenSet:
    raise ValueError("The option set by the variables: %s does not exist among the cfg options!" % switch)
  elif not options._beenSet[switch]:
    print ("Turning on %s, as some stored variables demands it" % switch)
    setattr(options, switch, True)

## Global tag
globalTag = options.globalTag
# if options.runOnData:
#     globalTag = options.dataGlobalTag

# trigresults="TriggerResults::HLT2"
# trigresults= cms.InputTag("TriggerResults","","HLT2")
# trigresults= cms.InputTag("TriggerResults")
trigresults= cms.InputTag("TriggerResults","","HLT")
if options.runOnData: options.isReHLT=False
# if options.isReHLT: trigresults = trigresults+"2"

#pfjets = "hltAK4PFJets" #original ak4PFJetsCHS
#calojets = "hltAK4CaloJets" #original ak4CaloJets
#puppijets = "hltAK4PFPuppiJets"
#PFDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPatJetTags" # original: pfDeepCSVJetTags
# PFDeepFlavourTags = "hltPFDeepFlavourJetTags" # original: pfDeepFlavourJetTagsSlimmedDeepFlavour
# PFDeepFlavourTagInfos = "hltPFDeepFlavour"
PFDeepFlavourTags = "hltPFDeepFlavourPatJetTags" # original: pfDeepFlavourJetTagsSlimmedDeepFlavour
PFDeepFlavourTagInfos = "hltPFDeepFlavourPat"
PFDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPatJetTags"
IPTagInfos = "hltDeepBLifetimePFPat"
SVTagInfos = "hltDeepSecondaryVertexPFPat"

PuppiDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPuppiPatJetTags"
PuppiDeepFlavourTags = "hltPFPuppiDeepFlavourJetTags"
PuppiDeepFlavourTagInfos = "hltPFPuppiDeepFlavour"
PuppiIPTagInfos = "hltDeepBLifetimePFPuppiPat"
SVPuppiTagInfos = "hltDeepSecondaryVertexPFPuppiPat"

rho = "hltFixedGridRhoFastjetAll" #original fixedGridRhoFastjetAll
hltVertices = "hltVerticesPFFilter" #original offlinePrimaryVertices
hltVerticesSlimmed = "hltVerticesPFFilter" #original offlineSlimmedPrimaryVertices
siPixelClusters = "hltSiPixelClusters" #original siPixelClusters
ecalRecHit = "hltEcalRecHit" #original ecalRecHit
hbhereco = "hltHbhereco" #original hbhereco
hfreco = "hltHfreco" #original hfreco
horeco = "hltHoreco" #original horeco
rpcRecHits = "hltRpcRecHits" #original rpcRecHits
tracks = "hltPFMuonMerging" #original generalTracks

# genParticles = "genParticles:HLT"
genParticles = "prunedGenParticles"
patJetSource = "hltPatJets"
patCaloJetSource = "hltPatJetsCalo"
patPuppiJetSource = "hltPatJetsPuppi"
genJetCollection = "ak4GenJetsNoNu:HLT"
pfCandidates = "hltParticleFlow"
pvSource = hltVertices
svSource = "hltDeepInclusiveMergedVerticesPF"
muSource = "hltMuons"
elSource = "hltEgammaGsfElectrons"
trackSource = tracks

update_jmeCalibs = False

def fixMenu(process):
	if hasattr(process, "hltEG60R9Id90CaloIdLIsoLDisplacedIdFilter"):
		process.hltEG60R9Id90CaloIdLIsoLDisplacedIdFilter.inputTrack = "hltMergedTracks"
	if hasattr(process, "hltIter1ClustersRefRemoval"):
		process.hltIter1ClustersRefRemoval.trajectories = "hltMergedTracks"
	return process

def prescale_path(path,ps_service):
  for pset in ps_service.prescaleTable:
      if pset.pathName.value() == path.label():
          pset.prescales = [0]*len(pset.prescales)

###
### HLT configuration
###
if options.runOnData:
    from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_Data import cms, process
else:
    from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_configDump_MC import cms, process

if options.reco == "HLT_GRun_oldJECs":
    # default GRun menu (Run 2 configurations)
    update_jmeCalibs = False

elif options.reco == "HLT_GRun":
    # default GRun menu (Run 2 configurations) + new PFHCs and JECs
    update_jmeCalibs = True

elif options.reco == "HLT_GRun_PatatrackQuadruplets":
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Quadruplets only) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrack
    process = customizeHLTforPatatrack(process)
    # process = fixMenu(process)
    update_jmeCalibs = True

elif options.reco == "HLT_GRun_PatatrackTriplets":
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Triplets+Quadruplets) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrackTriplets
    process = customizeHLTforPatatrackTriplets(process)
    # process = fixMenu(process)
    update_jmeCalibs = True

elif options.reco == "HLT_Run3TRK":
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == "HLT_Run3TRK_Quadruplets":
    # Run-3 tracking: standard (Quadruplets only)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process, quadrupletOnly=True)
    update_jmeCalibs = True
    process = fixMenu(process)
############################
#   old intermediate and temporary testing configurations
############################
# elif options.reco == "HLT_Run3TRKPixelOnlyCleaned2":
#     # (d) Run-3 tracking: pixel only tracks and trimmed with PVs
#     from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
#     from RecoBTag.PerformanceMeasurements.customise_TRK import *
#     process = customizeHLTforRun3Tracking(process)
#     process = customisePFForPixelTracksCleaned(process, "hltPixelTracksCleanForBTag", vertex="hltTrimmedPixelVertices", nVertices = 2)
#     update_jmeCalibs = True
#     process = fixMenu(process)

elif options.reco == "HLT_Run3TRK_ROICaloROIPF":
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_ROIPF import *
    process = customizeRun3_BTag_ROICalo_ROIPF(process, True)
    update_jmeCalibs = True
    process = fixMenu(process)
    pvSource                 = "hltVerticesPFFilterROIForBTag"
    pfCandidates             = "hltParticleFlowROIForBTag"
    trackSource              = "hltMergedTracksROIForBTag"
    rho                      = "hltFixedGridRhoFastjetAllROIForBTag"
    muSource = "hltMuonsROIForBTag"
    elSource = "hltEgammaGsfElectrons"

elif options.reco == "HLT_Run3TRK_noCaloROIPF":
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_noCalo_ROIPF import *
    process = customizeRun3_BTag_noCalo_ROIPF(process, True)
    update_jmeCalibs = True
    process = fixMenu(process)
    pvSource                 = "hltVerticesPFFilterROIForBTag"
    pfCandidates             = "hltParticleFlowROIForBTag"
    trackSource              = "hltMergedTracksROIForBTag"
    rho                      = "hltFixedGridRhoFastjetAllROIForBTag"
    muSource = "hltMuonsROIForBTag"
    elSource = "hltEgammaGsfElectrons"

elif options.reco == "HLT_Run3TRK_ROICaloGlobalPF":
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_GlobalPF import *
    process = customizeRun3_BTag_ROICalo_GlobalPF(process, True)
    update_jmeCalibs = True
    process = fixMenu(process)

elif options.reco == "HLT_Run3TRK_GlobalCaloGlobalPF":
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_GlobalCalo_GlobalPF import *
    process = customizeRun3_BTag_GlobalCalo_GlobalPF(process, True)
    update_jmeCalibs = True
    process = fixMenu(process)

else:
  raise RuntimeError("keyword \"reco = "+options.reco+"\" not recognised")



# remove cms.OutputModule objects from HLT config-dump
for _modname in process.outputModules_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.OutputModule:
       process.__delattr__(_modname)
       # if options.verbosity > 0:
       #    print "> removed cms.OutputModule:", _modname

# remove cms.EndPath objects from HLT config-dump
for _modname in process.endpaths_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.EndPath:
       process.__delattr__(_modname)
       # if options.verbosity > 0:
       #    print "> removed cms.EndPath:", _modname

### customizations
#          only relevant for Ntuplizing
###

if options.reco == "HLT_Run3TRK" or  options.reco == "HLT_GRun":
    from RecoBTag.PerformanceMeasurements.customise_TRK import addDeepJet
    process = addDeepJet(process, doPF = True, doPuppi = options.runPuppiJetVariables,
            roiReplace = "ROIPF" in options.reco,
            # roiReplaceCalo = "ROICalo" in options.reco or "noCalo" in options.reco
    )
from RecoBTag.PerformanceMeasurements.PATLikeConfig import customizePFPatLikeJets
process = customizePFPatLikeJets(process, runPF=True, runCalo=options.runCaloJetVariables, runPuppi=options.runPuppiJetVariables,
    roiReplace = "ROIPF" in options.reco,
    roiReplaceCalo = "ROICalo" in options.reco or "noCalo" in options.reco
)

if "HLT_Run3TRKPixelOnly" in options.reco:
    process = customizeMinHitsAndPt(process, doForPat=True)


# list of patterns to determine paths to keep
keepPaths = [
  # "MC_*Jets*",
  # "MC_*MET*",
  # "MC_*AK8Calo*",
  # "MC_*DeepCSV*",
  # "MC_*DeepJet*",
  # "MC_*DeepCSV*ROI*",
  # "MC_*DeepJet*ROI*",
  # "MC_*Matching*",
  # "DST_Run3_PFScoutingPixelTracking_v*",
  # "HLT_PFJet*_v*",
  # "HLT_AK4PFJet*_v*",
  # "HLT_AK8PFJet*_v*",
  # "HLT_PFHT*_v*",
  # "HLT_PFMET*_PFMHT*_v*",
  # "HLT_*_*_v*",
]

keepPaths = [
        "MC_AK4CaloJets_v*",
        "MC_AK4PFJets_v*",
        "MC_AK8CaloHT_v*",
        "MC_AK8PFJets_v*",
        "MC_AK8TrimPFJets_v*",
        "MC_CaloBTagDeepCSV_v*",
        "MC_CaloMET_JetIdCleaned_v*",
        "MC_CaloMET_v*",
        "MC_PFBTagDeepCSV_v*",
        "MC_PFBTagDeepJet_v*",
        "MC_PFMET_v1*",
        "HLT_PFJet40_v*",
        "HLT_PFJet60_v*",
        "HLT_PFJet80_v*",
        "HLT_PFJet140_v*",
        "HLT_PFJet200_v*",
        "HLT_PFJet260_v*",
        "HLT_PFJet320_v*",
        "HLT_PFJet400_v*",
        "HLT_PFJet450_v*",
        "HLT_PFJet500_v*",
        "HLT_PFJet550_v*",
        # AK8 PF Jets
        "HLT_AK8PFJet40_v*",
        "HLT_AK8PFJet60_v*",
        "HLT_AK8PFJet80_v*",
        "HLT_AK8PFJet140_v*",
        "HLT_AK8PFJet200_v*",
        "HLT_AK8PFJet260_v*",
        "HLT_AK8PFJet320_v*",
        "HLT_AK8PFJet400_v*",
        "HLT_AK8PFJet450_v*",
        "HLT_AK8PFJet500_v*",
        "HLT_AK8PFJet550_v*",
        # PF HT
        "HLT_PFHT180_v*",
        "HLT_PFHT250_v*",
        "HLT_PFHT370_v*",
        "HLT_PFHT430_v*",
        "HLT_PFHT510_v*",
        "HLT_PFHT590_v*",
        "HLT_PFHT680_v*",
        "HLT_PFHT780_v*",
        "HLT_PFHT890_v*",
        "HLT_PFHT1050_v*",
        # BTagMu
        "HLT_BTagMu_AK4DiJet20_Mu5_v*",
        "HLT_BTagMu_AK4DiJet40_Mu5_v*",
        "HLT_BTagMu_AK4DiJet70_Mu5_v*",
        "HLT_BTagMu_AK4DiJet110_Mu5_v*",
        "HLT_BTagMu_AK4DiJet170_Mu5_v*",
        "HLT_BTagMu_AK4Jet300_Mu5_v*",
        "HLT_BTagMu_AK8DiJet170_Mu5_v*",
        "HLT_BTagMu_AK8Jet300_Mu5_v*",
        # BTagMu Triggers with fix from Xavier
        # "HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v*", #triggerIdx=40
        # "HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v*", #triggerIdx=41
        # "HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v*", #triggerIdx=42
        # "HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v*", #triggerIdx=43
        # "HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v*", #triggerIdx=44
        # "HLT_BTagMu_AK4Jet300_Mu5_noalgo_v*", #triggerIdx+45
        # "HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v*",
        # "HLT_BTagMu_AK8Jet300_Mu5_noalgo_v*",
        # "HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v*"
]

# list of paths that are kept
listOfPaths = []
print ("Keep paths:")
print ("-"*108)
# remove selected cms.Path objects from HLT config-dump
for _modname in sorted(process.paths_()):
    _keepPath = False
    for _tmpPatt in keepPaths:
        _keepPath = fnmatch.fnmatch(_modname, _tmpPatt)
        if _keepPath: break
    if _keepPath:
        print ("{:<99} | {:<4} |".format(_modname, "+"))
        listOfPaths.append(_modname)
        continue
    _mod = getattr(process, _modname)
    if type(_mod) == cms.Path:
        process.__delattr__(_modname)
        # if options.verbosity > 0:
        #     print "{:<99} | {:<4} |".format(_modname, "")
print ("-"*108)

# remove FastTimerService
if hasattr(process, "FastTimerService"):
  del process.FastTimerService
# remove MessageLogger
if hasattr(process, "MessageLogger"):
  del process.MessageLogger



if update_jmeCalibs:
    ## ES modules for PF-Hadron Calibrations
    import os
    # from CondCore.DBCommon.CondDBSetup_cfi import *
    from CondCore.CondDB.CondDB_cfi import CondDB as _CondDB

    process.pfhcESSource = cms.ESSource("PoolDBESSource",
      _CondDB.clone(connect = "sqlite_fip:JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db"),
      toGet = cms.VPSet(
        cms.PSet(
          record = cms.string("PFCalibrationRcd"),
          tag = cms.string("PFCalibration_HLT_mcRun3_2021"),
          label = cms.untracked.string("HLT"),
        ),
      ),
    )

    process.pfhcESPrefer = cms.ESPrefer("PoolDBESSource", "pfhcESSource")
    ## ES modules for HLT JECs
    process.jescESSource = cms.ESSource("PoolDBESSource",
      _CondDB.clone(connect = "sqlite_fip:JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db"),
     toGet = cms.VPSet(
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4CaloHLT"),
          label = cms.untracked.string("AK4CaloHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFClusterHLT"),
          label = cms.untracked.string("AK4PFClusterHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFHLT"),
          label = cms.untracked.string("AK4PFHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFHLT"),#!!
          label = cms.untracked.string("AK4PFchsHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK4PFPuppiHLT"),
          label = cms.untracked.string("AK4PFPuppiHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8CaloHLT"),
          label = cms.untracked.string("AK8CaloHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFClusterHLT"),
          label = cms.untracked.string("AK8PFClusterHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFHLT"),
          label = cms.untracked.string("AK8PFHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFHLT"),#!!
          label = cms.untracked.string("AK8PFchsHLT"),
        ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_Run3Winter20_V2_MC_AK8PFPuppiHLT"),
          label = cms.untracked.string("AK8PFPuppiHLT"),
        ),
      ),
    )
    process.jescESPrefer = cms.ESPrefer("PoolDBESSource", "jescESSource")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
#process.MessageLogger.cerr.default.limit = 10
#process.MessageLogger.cerr.default.limit = 1

process.MessageLogger.suppressWarning = cms.untracked.vstring(
        "hltPatJetFlavourAssociationCalo"
)
process.MessageLogger.suppressError = cms.untracked.vstring(
        "hltPatJetFlavourAssociationCalo"
)
process.MessageLogger.cerr.threshold = "DEBUG"
#process.MessageLogger.debugModules = ["hltBTagPFDeepCSV4p06SingleROI","hltDeepCombinedSecondaryVertexBJetTagsPFROI","hltDeepCombinedSecondaryVertexBPFPatROIJetTags","hltPatJetsROI"]


# if options.inputFiles:
if False:
    process.source.fileNames = options.inputFiles
else:
    process.source.fileNames = [
        "file:///nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
        # "file:///nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/4edf2114-0dc8-4277-95c5-e55989d35c9e.root",
        # "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
        # # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4edf2114-0dc8-4277-95c5-e55989d35c9e.root",
        # # "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
    ]
# input EDM files [secondary]
if not hasattr(process.source, "secondaryFileNames"):
    process.source.secondaryFileNames = cms.untracked.vstring()
if options.secondaryInputFiles:
    process.source.secondaryFileNames = options.secondaryInputFiles
else:
    process.source.secondaryFileNames = [
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/a32ce6ba-6c9f-408e-9e3f-d9a93712c215.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/1c2e04fc-3ecc-4c34-a5a4-388d1a137530.root",

        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/40a66eee-8c49-4ca1-a5f6-73012543f72f.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/5b3dcd6c-99af-4c06-a447-10394b1fbd33.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/6cb2c3f8-1355-45c6-b0bc-9b14f2dcee21.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/743105e7-5848-4f04-9e58-8ea32e7b77e6.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/95153321-49f1-44f8-8b9d-f4fbd08306c5.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/9be50047-83df-4e55-abfe-a69a036c7cee.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/f030184d-7b2b-42db-b160-e16fa55cc255.root",

        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/052ece05-ff48-4fe7-9fdc-d4290f0b1d0b.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/8c918936-49b8-4a0d-907c-d8e9d2a29a36.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/a1b770d3-bf98-468f-bce4-057f0f4ce001.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/aa7e98fe-ddbc-415f-afeb-0bc5f9492cd6.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/dab63b08-97ec-4c1f-ae5a-8da6847f095c.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/edaa7369-785c-4f2b-866d-e4b68994f4c7.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/fd6c9b98-eb10-4b17-97fe-87814ac82c17.root",

        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/2c5880e9-81b8-4ec1-8e34-31764390592d.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/57aafa00-4aa6-4b52-9f7a-dcf93808dc05.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/5f409ffb-ef07-4825-944a-10982d1f7595.root",
        # "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/9c37be55-f5ee-4fb3-92c3-5c7d0e31508a.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/b71f8b97-5831-4602-a157-5aeefa1c7b36.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/cfea9793-91e8-415e-859a-afb876bad76b.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/fff0d30c-e551-4866-b236-391f1e5ef906.root",

        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/163c2e4f-6bbf-42e4-b385-1a21a4dc2070.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/2eb81a25-273d-4706-b986-866a39845097.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/47ec003d-00cd-4432-997c-983585ee3483.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/4ba0fbb9-99b5-45e2-bb17-e5829461c579.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/662543a5-7928-4b23-abf4-d97657cbe63e.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/7d970a90-b490-47c3-857b-b27521da3eb8.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/ddc6fee6-6f9a-4d3b-af15-c229684a39b6.root",

        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/56afbbd8-ffeb-4dcc-8e7c-5fe60b4ea1f6.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/7ff7ad0f-36c4-411d-b889-df8623a1dbf0.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/b59b4429-e89c-47c7-9711-1c855acedd16.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/c9b5efaf-8a64-497c-a1a1-75020b41f6db.root",
        "file:///pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/e7d89bb3-c588-4697-bdf5-d59177fd5443.root",

        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/a32ce6ba-6c9f-408e-9e3f-d9a93712c215.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140001/1c2e04fc-3ecc-4c34-a5a4-388d1a137530.root",
        #
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/40a66eee-8c49-4ca1-a5f6-73012543f72f.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/5b3dcd6c-99af-4c06-a447-10394b1fbd33.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/6cb2c3f8-1355-45c6-b0bc-9b14f2dcee21.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/743105e7-5848-4f04-9e58-8ea32e7b77e6.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/95153321-49f1-44f8-8b9d-f4fbd08306c5.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/9be50047-83df-4e55-abfe-a69a036c7cee.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/f030184d-7b2b-42db-b160-e16fa55cc255.root",
        #
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/052ece05-ff48-4fe7-9fdc-d4290f0b1d0b.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/8c918936-49b8-4a0d-907c-d8e9d2a29a36.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/a1b770d3-bf98-468f-bce4-057f0f4ce001.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/aa7e98fe-ddbc-415f-afeb-0bc5f9492cd6.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/dab63b08-97ec-4c1f-ae5a-8da6847f095c.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/edaa7369-785c-4f2b-866d-e4b68994f4c7.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/fd6c9b98-eb10-4b17-97fe-87814ac82c17.root",
        #
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/2c5880e9-81b8-4ec1-8e34-31764390592d.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/57aafa00-4aa6-4b52-9f7a-dcf93808dc05.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/5f409ffb-ef07-4825-944a-10982d1f7595.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/9c37be55-f5ee-4fb3-92c3-5c7d0e31508a.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/b71f8b97-5831-4602-a157-5aeefa1c7b36.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/cfea9793-91e8-415e-859a-afb876bad76b.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/fff0d30c-e551-4866-b236-391f1e5ef906.root",
        #
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/163c2e4f-6bbf-42e4-b385-1a21a4dc2070.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/2eb81a25-273d-4706-b986-866a39845097.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/47ec003d-00cd-4432-997c-983585ee3483.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/4ba0fbb9-99b5-45e2-bb17-e5829461c579.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/662543a5-7928-4b23-abf4-d97657cbe63e.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/7d970a90-b490-47c3-857b-b27521da3eb8.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/ddc6fee6-6f9a-4d3b-af15-c229684a39b6.root",
        #
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/56afbbd8-ffeb-4dcc-8e7c-5fe60b4ea1f6.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/7ff7ad0f-36c4-411d-b889-df8623a1dbf0.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/b59b4429-e89c-47c7-9711-1c855acedd16.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/c9b5efaf-8a64-497c-a1a1-75020b41f6db.root",
        # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/e7d89bb3-c588-4697-bdf5-d59177fd5443.root",
    ]

## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(options.outFilename)
)

## Events to process
process.source.skipEvents = cms.untracked.uint32(options.skipEvents)
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
    # process.options.numberOfThreads = cms.untracked.uint32(options.numThreads if (options.numThreads > 0) else 1)
    # process.options.numberOfStreams = cms.untracked.uint32(options.numStreams if (options.numStreams > 0) else 1)
    process.options.numberOfThreads = cms.untracked.uint32(0)
    process.options.numberOfStreams = cms.untracked.uint32(0)
process.GlobalTag.globaltag = globalTag

#-------------------------------------
## Output Module Configuration (expects a path "p")
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outFilename),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring("p") ),
)
#-------------------------------------
# if options.runOnData:
#     # Remove MC matching when running over data
#     from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
#     removeMCMatching( process, ["Photons", "Electrons","Muons", "Taus", "Jets", "METs", "PFElectrons","PFMuons", "PFTaus"] )
#-------------------------------------
## Add GenParticlePruner for boosted b-tagging studies
if not options.runOnData:
    process.prunedGenParticlesBoost = cms.EDProducer("GenParticlePruner",
        src = cms.InputTag(genParticles),
        select = cms.vstring(
            "drop  *  ", #by default
            "keep ( status = 3 || (status>=21 && status<=29) ) && pt > 0", #keep hard process particles with non-zero pT
            "keep abs(pdgId) = 13 || abs(pdgId) = 15" #keep muons and taus
        )
    )

#-------------------------------------
## Change the minimum number of tracker hits used in the track selection
if options.changeMinNumberOfHits:
    for m in process.producerNames().split(" "):
        if m.startswith("pfImpactParameterTagInfos"):
            print ("Changing \"minimumNumberOfHits\" for " + m + " to " + str(options.minNumberOfHits))
            getattr(process, m).minimumNumberOfHits = cms.int32(options.minNumberOfHits)

#-------------------------------------
process.btagana = HLTTwoFileBTagAnalyzer.clone()
#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = options.maxJetEta ## for extended forward pixel coverage
process.btagana.MinPt                 = options.minJetPt
process.btagana.tracksColl            = cms.InputTag(trackSource)
process.btagana.useTrackHistory       = options.useTrackHistory ## Can only be used with GEN-SIM-RECODEBUG files
process.btagana.produceJetTrackTruthTree = options.useTrackHistory ## can only be used with GEN-SIM-RECODEBUG files and when useTrackHistory is True
process.btagana.produceAllTrackTree   = options.produceAllTrackTree ## True if you want to run info for all tracks : for commissioning studies
#------------------
process.btagana.runTagVariables     = options.runTagVariables  ## True if you want to run TagInfo TaggingVariables
process.btagana.runCSVTagVariables  = options.runCSVTagVariables   ## True if you want to run CSV TaggingVariables
process.btagana.runCSVTagTrackVariables  = options.runCSVTagTrackVariables   ## True if you want to run CSV Tagging Track Variables
process.btagana.runDeepFlavourTagVariables = options.runDeepFlavourTagVariables
process.btagana.primaryVertexColl     = cms.InputTag(pvSource)
process.btagana.Jets                  = cms.InputTag(patJetSource)
process.btagana.CaloJets              = cms.InputTag(patCaloJetSource)
process.btagana.PuppiJets             = cms.InputTag(patPuppiJetSource)
process.btagana.muonCollectionName    = cms.InputTag(muSource)
process.btagana.electronCollectionName= cms.InputTag(elSource)

process.btagana.reco_muonCollectionName = cms.InputTag("slimmedMuons")
process.btagana.reco_electronCollectionName = cms.InputTag("slimmedElectrons")
# process.btagana.reco_electronID = cms.InputTag("slimmedElectrons:cutBasedElectronID-Fall17-94X-V1-tight")
# process.btagana.reco_electronID = "slimmedElectrons:cutBasedElectronID-Fall17-94X-V1-tight"
process.btagana.reco_electronID = cms.string("cutBasedElectronID-Fall17-94X-V1-tight")
process.btagana.reco_Jets = cms.InputTag("slimmedJets")
process.btagana.reco_met = cms.InputTag("slimmedMETs")
process.btagana.reco_photons = cms.InputTag("slimmedPhotons")
process.btagana.reco_vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
# process.btagana.reco_btagAlgosDeepCSV = ["pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probbb"]
process.btagana.reco_btagAlgosDeepCSV = cms.vstring(["pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probbb"])
# process.btagana.reco_btagAlgosDeepJet = ["pfDeepFlavourJetTags:probb", "pfDeepFlavourJetTags:probbb", "pfDeepFlavourJetTags:problepb"]


# process.btagana.patMuonCollectionName = cms.InputTag(patMuons)
process.btagana.rho                   = cms.InputTag(rho)

# process.btagana.triggerTable          = cms.InputTag("TriggerResults::HLT") # Data and MC
process.btagana.triggerTable          = trigresults # Data and MC
process.btagana.genParticles          = cms.InputTag(genParticles)
process.hltPatJetPartons.particles = cms.InputTag(genParticles)
process.hltPatJetPartons.src = cms.InputTag("generator:SIM")
process.hltPatJetPartonsLegacy.genParticles = cms.InputTag(genParticles)
process.hltPatJetPartonsLegacy.src = cms.InputTag(genParticles)
process.hltPackedGenParticles.genParticles = cms.InputTag(genParticles)
process.hltPackedGenParticles.inputOriginal = cms.InputTag(genParticles)
process.hltPrunedGenParticlesWithStatusOne.genParticles = cms.InputTag(genParticles)
process.hltPrunedGenParticlesWithStatusOne.src = cms.InputTag(genParticles)
process.hltSlimmedGenJets.src = cms.InputTag("ak4GenJetsNoNu::HLT")
process.hltSlimmedGenJets.packedGenParticles = cms.InputTag("packedGenParticles::RECO")
process.btagana.candidates            = cms.InputTag(pfCandidates)
process.btagana.runJetVariables       = options.runJetVariables
process.btagana.runCaloJetVariables   = options.runCaloJetVariables
process.btagana.runPuppiJetVariables   = options.runPuppiJetVariables
process.btagana.runQuarkVariables     = options.runQuarkVariables
process.btagana.runHadronVariables    = options.runHadronVariables
process.btagana.runGenVariables       = options.runGenVariables
process.btagana.runPFElectronVariables = options.runPFElectronVariables
process.btagana.runPFMuonVariables = options.runPFMuonVariables
# process.btagana.runPatMuons = options.runPatMuons
process.btagana.runEventInfo = options.runEventInfo
process.btagana.runOnData = options.runOnData


process.btagana.deepCSVBJetTags = PFDeepCSVTags
process.btagana.deepCSVBPuppiJetTags = PuppiDeepCSVTags

process.btagana.deepFlavourJetTags    = PFDeepFlavourTags
process.btagana.deepFlavourTagInfos   = PFDeepFlavourTagInfos

process.btagana.deepFlavourPuppiJetTags    = PuppiDeepFlavourTags
process.btagana.deepFlavourPuppiTagInfos = PuppiDeepFlavourTagInfos

process.btagana.ipPuppiTagInfos = PuppiIPTagInfos
process.btagana.ipTagInfos = IPTagInfos

process.btagana.svPuppiTagInfos = SVPuppiTagInfos
process.btagana.svTagInfos = SVTagInfos

if options.runOnData:
  process.btagana.runHadronVariables  = False
  process.btagana.runQuarkVariables   = False
  process.btagana.runGenVariables     = False

if not process.btagana.useTrackHistory  or not options.produceJetTrackTree:
    process.btagana.produceJetTrackTruthTree = False

if process.btagana.useTrackHistory:
    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

if process.btagana.produceJetTrackTruthTree:
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
    process.load("SimTracker.TrackHistory.TrackHistory_cff")
    process.load("SimTracker.TrackHistory.TrackClassifier_cff")
    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
    process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

#---------------------------------------
# process.options.numberOfThreads = cms.untracked.uint32(1)
# process.options.numberOfStreams = cms.untracked.uint32(1)
#---------------------------------------
## Trigger selection !
#import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
#process.JetHLTFilter = hlt.triggerResultsFilter.clone(
#    triggerConditions = cms.vstring(
#        "HLT_PFJet80_v*"
#    ),
#    hltResults = cms.InputTag("TriggerResults","","HLT"),
#    l1tResults = cms.InputTag( "" ),
#    throw = cms.bool( False ) #set to false to deal with missing triggers while running over different trigger menus
#)
#---------------------------------------

#---------------------------------------
## Optional MET filters:
## https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
#process.load("RecoMET.METFilters.metFilters_cff")
#process.trackingFailureFilter.VertexSource = cms.InputTag("goodOfflinePrimaryVertices")
#---------------------------------------

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------
## Define analyzer sequence
process.analyzerSeq = cms.Sequence( )
process.analyzerSeq += process.btagana
#--------


# from JMETriggerAnalysis.Common.TrackHistogrammer_cfi import TrackHistogrammer
# process.TrackHistograms_hltPixelTracks = TrackHistogrammer.clone(src = "hltPixelTracks")
# process.TrackHistograms_hltPixelTracksCleanForBTag = TrackHistogrammer.clone(src = "hltPixelTracksCleanForBTag")
# process.TrackHistograms_hltMergedTracks = TrackHistogrammer.clone(src = "hltMergedTracks")
# process.TrackHistograms_hltPixelTracksForBTag = TrackHistogrammer.clone(src = "hltPixelTracksForBTag")
# process.TrackHistograms_hltPixelTracksZetaClean = TrackHistogrammer.clone(src = "hltPixelTracksZetaClean")
# process.TrackHistograms_hltPFMuonMerging = TrackHistogrammer.clone(src = "hltPFMuonMerging")
# process.TrackHistograms_hltLightPFTracks = TrackHistogrammer.clone(src = "hltLightPFTracks")
#
# process.trkMonitoringSeq = cms.Sequence(
#    process.TrackHistograms_hltPixelTracks
#  + process.TrackHistograms_hltMergedTracks
#  + process.TrackHistograms_hltPixelTracksZetaClean
#  + process.TrackHistograms_hltPFMuonMerging
#  + process.TrackHistograms_hltLightPFTracks
# )
# if "HLT_Run3TRKForBTag" in options.reco or "HLT_Run3TRKPixelOnly" in options.reco:
#     process.trkMonitoringSeq+= process.TrackHistograms_hltPixelTracksForBTag
#     process.trkMonitoringSeq+= process.TrackHistograms_hltPixelTracksCleanForBTag

# process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)
# process.schedule.extend([process.trkMonitoringEndPath])

# from JMETriggerAnalysis.Common.VertexHistogrammer_cfi import VertexHistogrammer
# process.VertexHistograms_hltPixelVertices = VertexHistogrammer.clone(src = "hltPixelVertices")
# process.VertexHistograms_hltTrimmedPixelVertices = VertexHistogrammer.clone(src = "hltTrimmedPixelVertices")
# process.VertexHistograms_hltVerticesPF = VertexHistogrammer.clone(src = "hltVerticesPF")
# process.VertexHistograms_hltVerticesPFFilter = VertexHistogrammer.clone(src = "hltVerticesPFFilter")
# #
# process.vtxMonitoringSeq = cms.Sequence(
#    process.VertexHistograms_hltPixelVertices
#    + process.VertexHistograms_hltTrimmedPixelVertices
#    + process.VertexHistograms_hltVerticesPF
#    + process.VertexHistograms_hltVerticesPFFilter
# )
# process.vtxMonitoringEndPath = cms.EndPath(process.vtxMonitoringSeq)

if options.runTiming:
    #timing test
    from HLTrigger.Timer.FastTimer import customise_timer_service_print,customise_timer_service,customise_timer_service_singlejob
    # process = customise_timer_service_print(process)
    # process = customise_timer_service(process)
        # remove any instance of the FastTimerService
    if "FastTimerService" in process.__dict__:
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
    process.FastTimerService.dqmTimeRange             = 1000.   # ms
    process.FastTimerService.dqmTimeResolution        =    5.   # ms
    process.FastTimerService.dqmPathTimeRange         =  100.   # ms
    process.FastTimerService.dqmPathTimeResolution    =    0.5  # ms
    process.FastTimerService.dqmModuleTimeRange       =   40.   # ms
    process.FastTimerService.dqmModuleTimeResolution  =    0.2  # ms
    # set the base DQM folder for the plots
    process.FastTimerService.dqmPath                  = "HLT/TimerService"
    process.FastTimerService.enableDQMbyProcesses     = False
    # enable text dump
    if not hasattr(process,"MessageLogger"):
        process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.categories.append("FastReport")
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
    process.FastTimerService.dqmModuleTimeRange      =  1000.
    process.FastTimerService.dqmModuleTimeResolution =     1.
    # process.dqmOutput.fileName = cms.untracked.string(options.output)

process.p = cms.Path(
    process.allEvents
    * process.selectedEvents
    * process.analyzerSeq
    # * process.trkMonitoringSeq
    # * process.vtxMonitoringSeq
)
process.analysisNTupleEndPath = cms.EndPath(process.btagana)
process.schedule.extend([process.p])

# if options.runTiming:
#     process.p *= process.FastTimerOutput

# Delete predefined output module (needed for running with CRAB)
# del process.out
# dump content of cms.Process to python file
if options.dumpPython is not None:
   open(options.dumpPython, "w").write(process.dumpPython())

print ("")
print ("option: output =", options.outFilename)
print ("option: reco =", options.reco)
print ("option: dumpPython =", options.dumpPython)
print ("")
print ("process.GlobalTag =", process.GlobalTag.globaltag)
print ("process.source =", process.source.dumpPython())
print ("process.maxEvents =", process.maxEvents.input)
print ("-------------------------------")
