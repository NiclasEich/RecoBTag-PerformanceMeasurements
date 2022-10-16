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
options.register('outFilename', 'JetTreeHLT.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
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
options.register('globalTag', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MC global tag, no default value provided"
)
options.register('runEventInfo', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run Event Info"
)
options.register('processStdAK4Jets', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process standard AK4 jets"
)
options.register('useTrackHistory', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "uses track history, for GEN-SIM-RECODEBUG samples only"
)
options.register('produceJetTrackTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run info for tracks associated to jets : for commissioning studies"
)
options.register('produceAllTrackTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Produce all track tree"
)

options.register('fillPU', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Fill PU"
)
### Options for upgrade studies
# Change hits requirements
options.register('changeMinNumberOfHits', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Change minimum number of tracker hits"
)
options.register('minNumberOfHits', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Minimum number of tracker hits"
)
# Change eta for extended forward pixel coverage
options.register('maxJetEta', 4.5,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum jet |eta| (default is 4.5)"
)

options.register('lumis', None,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'path to .json with list of luminosity sections'
)
options.register('minJetPt', 25.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum jet pt (default is 20)"
)
options.register('usePrivateJEC', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Use JECs from private SQLite files')
options.register('jecDBFileMC', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'SQLite filename for JECs, no default value provided')
options.register('jecDBFileData', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'SQLite filename for JECs, no default value provided')
options.register('isReHLT', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    '80X reHLT samples')
options.register('JPCalibration', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'JP Calibration pyload to use')
options.register('runJetVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Jet Variables')
options.register('runCaloJetVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Jet Variables')
options.register('runPuppiJetVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Jet Variables')
options.register('runTagVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Tag Variables')
options.register('runQuarkVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run c/b quark Variables')
options.register('runHadronVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Hadron Variables')
options.register('runGenVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Gen Variables')
options.register('runCSVTagVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run CSV TaggingVariables')
options.register('runCSVTagTrackVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run CSV Tagging Track Variables')
options.register('runDeepFlavourTagVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run DeepFlavour TaggingVariables')
options.register('runPFElectronVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run PF Electron Variables')
options.register('runPFMuonVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run PF Muon Variables')
options.register('defaults', '',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'baseline default settings to be used')
options.register('eras', [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    'era modifiers to be used to be used')
options.register('groups', [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    'variable groups to be stored')
options.register(
    'skipEvents', 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "skip N events")
options.register('runTiming', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'run timing instead of rates')
options.register('numThreads', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    'number of threads')
options.register('numStreams', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    'number of streams')
options.register(
    'reco', 'HLT_GRun',
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  'keyword to define HLT reconstruction'
)

## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)

options.parseArguments()
if options.defaults:
	from importlib import import_module
	try:
		defaults = import_module('RecoBTag.PerformanceMeasurements.defaults_HLT.%s' % options.defaults)
	except ImportError:
		raise ValueError('The default settings named %s.py are not present in PerformanceMeasurements/python/defaults_HLT/' % options.defaults)
	if not hasattr(defaults, 'common') or not isinstance(defaults.common, dict):
		raise RuntimeError('the default file %s.py does not contain a dictionary named common' % options.defaults)
	items = defaults.common.items()
	if hasattr(defaults, 'data') and options.runOnData:
		if not isinstance(defaults.data, dict):
			raise RuntimeError('the default file %s.py contains an object called "data" which is not a dictionary' % options.defaults)
		items.extend(defaults.data.items())
	if hasattr(defaults, 'mc') and not options.runOnData:
		if not isinstance(defaults.mc, dict):
			raise RuntimeError('the default file %s.py contains an object called "mc" which is not a dictionary' % options.defaults)
		items.extend(defaults.mc.items())
	for key, value in items:
		if key not in options._beenSet:
			raise ValueError('The key set by the defaults: %s does not exist among the cfg options!' % key)
		elif not options._beenSet[key]:
			if key == 'inputFiles' and options.inputFiles: continue #skip input files that for some reason are never considered set
			print ('setting default option for', key)
			setattr(options, key, value)

from RecoBTag.PerformanceMeasurements.HLTBTagAnalyzer_cff import *
btagana_tmp = HLTBTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on

for requiredGroup in options.groups:
  # print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    # print (existingGroup)
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var or "PuppiJet." in var:
            var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')

#change values accordingly
for switch in options_to_change:
  if switch in ["runTagVariablesSubJets","runCSVTagVariablesSubJets"]:
      continue
  elif switch not in options._beenSet:
    raise ValueError('The option set by the variables: %s does not exist among the cfg options!' % switch)
  elif not options._beenSet[switch]:
    print ('Turning on %s, as some stored variables demands it' % switch)
    setattr(options, switch, True)

## Global tag
globalTag = options.globalTag
# if options.runOnData:
#     globalTag = options.dataGlobalTag

# trigresults='TriggerResults::HLT'
trigresults='TriggerResults'
if options.runOnData: options.isReHLT=False
if options.isReHLT: trigresults = trigresults+'2'

#pfjets = "hltAK4PFJets" #original ak4PFJetsCHS
#calojets = "hltAK4CaloJets" #original ak4CaloJets
#puppijets = "hltAK4PFPuppiJets"
#PFDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPatJetTags" # original: pfDeepCSVJetTags
# PFDeepFlavourTags = "hltPFDeepFlavourJetTags" # original: pfDeepFlavourJetTagsSlimmedDeepFlavour
# PFDeepFlavourTagInfos = 'hltPFDeepFlavour'
PFDeepFlavourTags = "hltPFDeepFlavourPatJetTags" # original: pfDeepFlavourJetTagsSlimmedDeepFlavour
PFDeepFlavourTagInfos = 'hltPFDeepFlavourPat'
PFDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPatJetTags"
IPTagInfos = 'hltDeepBLifetimePFPat'
SVTagInfos = 'hltDeepSecondaryVertexPFPat'

PuppiDeepCSVTags = 'hltDeepCombinedSecondaryVertexBPFPuppiPatJetTags'
PuppiDeepFlavourTags = 'hltPFPuppiDeepFlavourJetTags'
PuppiDeepFlavourTagInfos = 'hltPFPuppiDeepFlavour'
PuppiIPTagInfos = 'hltDeepBLifetimePFPuppiPat'
SVPuppiTagInfos = 'hltDeepSecondaryVertexPFPuppiPat'

rho = "hltFixedGridRhoFastjetAll" #original fixedGridRhoFastjetAll
hltVertices = "hltVerticesPFFilter" #original offlinePrimaryVertices
# hltVerticesSlimmed = "hltVerticesPFFilter" #original offlineSlimmedPrimaryVertices
siPixelClusters = "hltSiPixelClusters" #original siPixelClusters
ecalRecHit = "hltEcalRecHit" #original ecalRecHit
hbhereco = "hltHbhereco" #original hbhereco
hfreco = "hltHfreco" #original hfreco
horeco = "hltHoreco" #original horeco
rpcRecHits = "hltRpcRecHits" #original rpcRecHits
tracks = "hltPFMuonMerging" #original generalTracks

genParticles = 'genParticles'
patJetSource = 'hltPatJets'
patCaloJetSource = 'hltPatJetsCalo'
patPuppiJetSource = 'hltPatJetsPuppi'
genJetCollection = 'ak4GenJetsNoNu'
pfCandidates = 'hltParticleFlow'
pvSource = hltVertices
# svSource = 'hltDeepInclusiveMergedVerticesPF'
muSource = 'hltMuons'
elSource = 'hltEgammaGsfElectrons'
trackSource = tracks

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
    from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_3_0_GRun_configDump_Data import cms, process
else:
    # from Phase2_HLT_configDump import cms, process
    # from JMETriggerAnalysis.Common.configs.HLT_75e33_cfg import cms, process
    from Phase2_HLT_configDump import cms, process
    # from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_3_2_GRun_configDump_MC import cms, process

if options.reco == 'HLT_GRun' or options.reco == "HLT_GRun_oldJECs":
    # default GRun menu (Run 2 configurations) + new PFHCs and JECs
    # do nothing
    process = process

elif options.reco == "Phase2":
    process = process

elif options.reco == "HLT_GRun_BatchNorm":
    process = process
    from RecoBTag.PerformanceMeasurements.forceNewJEC import *
    process = forceNewJEC(process)
    if hasattr(process, "hltDeepCombinedSecondaryVertexBJetTagsCalo"):
        process.hltDeepCombinedSecondaryVertexBJetTagsCalo.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
    if hasattr(process, "hltDeepCombinedSecondaryVertexBJetTagsPF"):
        process.hltDeepCombinedSecondaryVertexBJetTagsPF.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
    if hasattr(process, "hltDeepCombinedSecondaryVertexBJetTagsPFAK8"):
        process.hltDeepCombinedSecondaryVertexBJetTagsPFAK8.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
    if hasattr(process, "hltDeepCombinedSecondaryVertexBPFPuppiPatJetTags"):
        process.hltDeepCombinedSecondaryVertexBPFPuppiPatJetTags.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
    if hasattr(process, "hltDeepCombinedSecondaryVertexBPFPatJetTags"):
        process.hltDeepCombinedSecondaryVertexBPFPatJetTags.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
    if hasattr(process, "hltDeepCombinedSecondaryVertexCaloPatBJetTags"):
        process.hltDeepCombinedSecondaryVertexCaloPatBJetTags.NNConfig = cms.FileInPath("RecoBTag/Combined/data/model_no_offset_DeepCSV.json")
else:
  raise RuntimeError('keyword "reco = '+options.reco+'" not recognised')

# remove cms.OutputModule objects from HLT config-dump
for _modname in process.outputModules_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.OutputModule:
       process.__delattr__(_modname)
       # if options.verbosity > 0:
       #    print '> removed cms.OutputModule:', _modname

# # remove cms.EndPath objects from HLT config-dump
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

### customizations
#          only relevant for Ntuplizing
###

from RecoBTag.PerformanceMeasurements.PATLikeConfig import customizePFPatLikeJets
# process = customizePFPatLikeJets(process, runPF=True, runCalo=options.runCaloJetVariables, runPuppi=options.runPuppiJetVariables,
    # # roiReplace = "ROIPF" in options.reco,
    # roiReplace = False,
    # # roiReplaceCalo = ("ROICalo" in options.reco and not "GlobalPF" in options.reco) or "noCalo" in options.reco,
    # roiReplaceCalo = False,
    # isData = options.runOnData
# )

# list of patterns to determine paths to keep
keepPaths = [
  'MC_*',
#   'HLT_*DeepCSV*',
  'HLT_*DeepJet*',
  'Status_OnCPU',
  'Status_OnGPU',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath',
  'HLTAnalyzerEndpath',
]

# list of paths that are kept
listOfPaths = []
print ("Keep paths:")
print ('-'*108)
# remove selected cms.Path objects from HLT config-dump
for _modname in sorted(process.paths_()):
    _keepPath = False
    for _tmpPatt in keepPaths:
        _keepPath = fnmatch.fnmatch(_modname, _tmpPatt)
        if _keepPath: break
    if _keepPath:
        print ('{:<99} | {:<4} |'.format(_modname, '+'))
        listOfPaths.append(_modname)
        continue
    _mod = getattr(process, _modname)
    if type(_mod) == cms.Path:
        process.__delattr__(_modname)
        # if options.verbosity > 0:
        #     print '{:<99} | {:<4} |'.format(_modname, '')
print ('-'*108)

# remove FastTimerService
if hasattr(process, 'FastTimerService'):
  del process.FastTimerService
# remove MessageLogger
if hasattr(process, 'MessageLogger'):
  del process.MessageLogger

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
#process.MessageLogger.cerr.default.limit = 10
#process.MessageLogger.cerr.default.limit = 1

process.MessageLogger.suppressWarning = cms.untracked.vstring(
        'hltPatJetFlavourAssociationCalo',
        'hltCTPPSPixelDigis',
       'VertexHistograms_hltPixelVertices',
       'VertexHistograms_hltTrimmedPixelVertices',
       'VertexHistograms_hltVerticesPF',
       'VertexHistograms_hltVerticesPFFilter',
       'VertexHistograms_hltVerticesL3FilterROIForBTag',
       'VertexHistograms_hltVerticesL3SelectorROIForBTag',
       'VertexHistograms_hltVerticesL3ROIForBTag',
       'VertexHistograms_hltVerticesPFROIForBTag',
       'VertexHistograms_hltVerticesPFSelectorROIForBTag',
       'VertexHistograms_hltVerticesPFFilterROIForBTag',

       'hltL3NoFiltersNoVtxMuonsOIState',
       'hltL3MuonsIterL3OINoVtx',
       'hltL3NoFiltersNoVtxMuonsOIHit',
       'hltL3NoFiltersTkTracksFromL2IOHitNoVtx',
       'hltCSCHaloData',
)
process.MessageLogger.suppressError = cms.untracked.vstring(
    'hltPatJetFlavourAssociationCalo',
    'hltCTPPSPixelDigis',
    'VertexHistograms_hltPixelVertices',
    'VertexHistograms_hltTrimmedPixelVertices',
    'VertexHistograms_hltVerticesPF',
    'VertexHistograms_hltVerticesPFFilter',
    'VertexHistograms_hltVerticesL3FilterROIForBTag',
    'VertexHistograms_hltVerticesL3SelectorROIForBTag',
    'VertexHistograms_hltVerticesL3ROIForBTag',
    'VertexHistograms_hltVerticesPFROIForBTag',
    'VertexHistograms_hltVerticesPFSelectorROIForBTag',
    'VertexHistograms_hltVerticesPFFilterROIForBTag',

    'TrackHistograms_hltPixelTracks',
    'TrackHistograms_hltMergedTracks',
    'TrackHistograms_hltPixelTracksZetaClean',
    'TrackHistograms_hltPFMuonMerging',
    'TrackHistograms_hltLightPFTracks',

    'hltL3NoFiltersNoVtxMuonsOIState',
    'hltL3MuonsIterL3OINoVtx',
    'hltL3NoFiltersNoVtxMuonsOIHit',
    'hltL3NoFiltersTkTracksFromL2IOHitNoVtx',
    'hltCSCHaloData',
)
process.MessageLogger.cerr.threshold = "DEBUG"
#process.MessageLogger.debugModules = ["hltBTagPFDeepCSV4p06SingleROI","hltDeepCombinedSecondaryVertexBJetTagsPFROI","hltDeepCombinedSecondaryVertexBPFPatROIJetTags","hltPatJetsROI"]


if options.inputFiles:
    process.source.fileNames = options.inputFiles
process.source.secondaryFileNames = cms.untracked.vstring()

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
    process.options.numberOfThreads = cms.untracked.uint32(options.numThreads if (options.numThreads > 1) else 1)
    process.options.numberOfStreams = cms.untracked.uint32(options.numStreams if (options.numStreams > 1) else 1)
    process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32(10240)
    process.options.makeTriggerResults = cms.untracked.bool(True)
    process.hltTrigReport = cms.EDAnalyzer("HLTrigReport",
        HLTriggerResults = cms.InputTag("TriggerResults","","@currentProcess"),
        ReferencePath = cms.untracked.string('HLTriggerFinalPath'),
        ReferenceRate = cms.untracked.double(100.0),
        reportBy = cms.untracked.string('job'),
        resetBy = cms.untracked.string('never'),
        serviceBy = cms.untracked.string('never')
    )

process.GlobalTag.globaltag = globalTag

#-------------------------------------
## Output Module Configuration (expects a path 'p')
# process.out = cms.OutputModule("PoolOutputModule",
#     fileName = cms.untracked.string(options.outFilename),
#     SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
# )
#-------------------------------------
# if options.runOnData:
#     # Remove MC matching when running over data
#     from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
#     removeMCMatching( process, ['Photons', 'Electrons','Muons', 'Taus', 'Jets', 'METs', 'PFElectrons','PFMuons', 'PFTaus'] )
#-------------------------------------
## Add GenParticlePruner for boosted b-tagging studies
if not options.runOnData:
    process.prunedGenParticlesBoost = cms.EDProducer('GenParticlePruner',
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
    for m in process.producerNames().split(' '):
        if m.startswith('pfImpactParameterTagInfos'):
            print ("Changing 'minimumNumberOfHits' for " + m + " to " + str(options.minNumberOfHits))
            getattr(process, m).minimumNumberOfHits = cms.int32(options.minNumberOfHits)

#-------------------------------------
process.btagana = HLTBTagAnalyzer.clone()
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
process.btagana.tofPIDColl = cms.InputTag("tofPID", "t0", "RECO") 
process.btagana.primaryVertexColl     = cms.InputTag(pvSource)
process.btagana.Jets                  = cms.InputTag(patJetSource)
process.btagana.CaloJets              = cms.InputTag(patCaloJetSource)
process.btagana.PuppiJets             = cms.InputTag(patPuppiJetSource)
process.btagana.muonCollectionName    = cms.InputTag(muSource)
process.btagana.electronCollectionName= cms.InputTag(elSource)
# process.btagana.patMuonCollectionName = cms.InputTag(patMuons)
process.btagana.rho                   = cms.InputTag(rho)

# process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
# process.btagana.triggerTable          = cms.InputTag(trigresults) # Data and MC
process.btagana.triggerTable          = cms.InputTag("TriggerResults","","@currentProcess") # Data and MC
process.btagana.genParticles          = cms.InputTag(genParticles)
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
  # select luminosity sections from .json file
  if options.lumis is not None:
      import FWCore.PythonUtilities.LumiList as LumiList
      process.source.lumisToProcess = LumiList.LumiList(filename = options.lumis).getVLuminosityBlockRange()

if not process.btagana.useTrackHistory  or not options.produceJetTrackTree:
    process.btagana.produceJetTrackTruthTree = False

if process.btagana.useTrackHistory:
    process.load('SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi')
    process.load('SimTracker.TrackerHitAssociation.tpClusterProducer_cfi')

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
#process.trackingFailureFilter.VertexSource = cms.InputTag('goodOfflinePrimaryVertices')
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
monitorTracks = False
if monitorTracks:

    from JMETriggerAnalysis.Common.TrackHistogrammer_cfi import TrackHistogrammer
    process.TrackHistograms_hltPixelTracks = TrackHistogrammer.clone(src = 'hltPixelTracks')
    process.TrackHistograms_hltPixelTracksCleanForBTag = TrackHistogrammer.clone(src = 'hltPixelTracksCleanForBTag')
    process.TrackHistograms_hltMergedTracks = TrackHistogrammer.clone(src = 'hltMergedTracks')
    process.TrackHistograms_hltPixelTracksForBTag = TrackHistogrammer.clone(src = 'hltPixelTracksForBTag')
    process.TrackHistograms_hltPixelTracksZetaClean = TrackHistogrammer.clone(src = 'hltPixelTracksZetaClean')
    process.TrackHistograms_hltPFMuonMerging = TrackHistogrammer.clone(src = 'hltPFMuonMerging')
    process.TrackHistograms_hltLightPFTracks = TrackHistogrammer.clone(src = 'hltLightPFTracks')

    process.trkMonitoringSeq = cms.Sequence(
       process.TrackHistograms_hltPixelTracks
     + process.TrackHistograms_hltMergedTracks
     + process.TrackHistograms_hltPixelTracksZetaClean
     + process.TrackHistograms_hltPFMuonMerging
     + process.TrackHistograms_hltLightPFTracks
    )
    # if "HLT_Run3TRKForBTag" in options.reco or "HLT_Run3TRKPixelOnly" in options.reco:
    #     process.trkMonitoringSeq+= process.TrackHistograms_hltPixelTracksForBTag
    #     process.trkMonitoringSeq+= process.TrackHistograms_hltPixelTracksCleanForBTag

    process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)
    process.schedule.extend([process.trkMonitoringEndPath])

monitorVertices = False
if monitorVertices:

    from JMETriggerAnalysis.Common.VertexHistogrammer_cfi import VertexHistogrammer
    process.VertexHistograms_hltPixelVertices = VertexHistogrammer.clone(src = 'hltPixelVertices')
    process.VertexHistograms_hltTrimmedPixelVertices = VertexHistogrammer.clone(src = 'hltTrimmedPixelVertices')
    process.VertexHistograms_hltVerticesPF = VertexHistogrammer.clone(src = 'hltVerticesPF')
    process.VertexHistograms_hltVerticesPFFilter = VertexHistogrammer.clone(src = 'hltVerticesPFFilter')
    process.VertexHistograms_hltVerticesL3FilterROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesL3FilterROIForBTag')
    process.VertexHistograms_hltVerticesL3SelectorROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesL3SelectorROIForBTag')
    process.VertexHistograms_hltVerticesL3ROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesL3ROIForBTag')
    process.VertexHistograms_hltVerticesPFROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesPFROIForBTag')
    process.VertexHistograms_hltVerticesPFSelectorROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesPFSelectorROIForBTag')
    process.VertexHistograms_hltVerticesPFFilterROIForBTag = VertexHistogrammer.clone(src = 'hltVerticesPFFilterROIForBTag')
    # #
    process.vtxMonitoringSeq = cms.Sequence(
       process.VertexHistograms_hltPixelVertices
       + process.VertexHistograms_hltTrimmedPixelVertices
       + process.VertexHistograms_hltVerticesPF
       + process.VertexHistograms_hltVerticesPFFilter
       + process.VertexHistograms_hltVerticesL3FilterROIForBTag
       + process.VertexHistograms_hltVerticesL3SelectorROIForBTag
       + process.VertexHistograms_hltVerticesL3ROIForBTag
       + process.VertexHistograms_hltVerticesPFROIForBTag
       + process.VertexHistograms_hltVerticesPFSelectorROIForBTag
       + process.VertexHistograms_hltVerticesPFFilterROIForBTag
    )
    process.vtxMonitoringEndPath = cms.EndPath(process.vtxMonitoringSeq)
    process.schedule.extend([process.vtxMonitoringEndPath])

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
    if not hasattr(process,'MessageLogger'):
        process.load('FWCore.MessageService.MessageLogger_cfi')
    process.MessageLogger.categories.append('FastReport')
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

process.analysisNTupleEndPath = cms.EndPath(process.btagana)
process.schedule.extend([process.analysisNTupleEndPath])

# if options.runTiming:
#     process.p *= process.FastTimerOutput

# Delete predefined output module (needed for running with CRAB)
# del process.out
# dump content of cms.Process to python file
if options.dumpPython is not None:
   open(options.dumpPython, 'w').write(process.dumpPython())

print ('')
print ('option: output =', options.outFilename)
print ('option: reco =', options.reco)
print ('option: dumpPython =', options.dumpPython)
print ('')
print ('process.GlobalTag =', process.GlobalTag.globaltag)
print ('process.source =', process.source.dumpPython())
print ('process.maxEvents =', process.maxEvents.input)
print ('process.numberOfStreams =', process.options.numberOfStreams)
print ('process.numberOfThreads =', process.options.numberOfThreads)
print ('-------------------------------')
