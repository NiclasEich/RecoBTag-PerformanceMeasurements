import FWCore.ParameterSet.Config as cms
### configuration file to re-run customized HLT Menu on RAW
###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('globalTag', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('logs', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'create log files configured via MessageLogger')

opts.register('reco', 'HLT_TRKv06p1_TICL',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Which tracking version to run')

opts.register('outName', 'JetTree_mc.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Name of the output root file')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'Path to python file with content of cms.Process')

opts.register('trkdqm', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for selected Tracks and Vertices')

opts.register('BTVreco', 'cutsV2',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'which reco to load for BTV sequence, default = default')

opts.register('pfdqm', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'added monitoring histograms for selected PF-Candidates')

opts.register('pvdqm', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'added monitoring histograms for selected Vertex collections (partly, to separate output files)')

opts.register('l1tdqm', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'added monitoring histograms for L1T objects')



opts.parseArguments()

# flag: skim original collection of generalTracks (only tracks associated to first N pixel vertices)
opt_skimTracks = False
#
opt_reco = opts.reco
if opt_reco.endswith('_skimmedTracks'):
   opt_reco = opt_reco[:-len('_skimmedTracks')]
   opt_skimTracks = True
#
# if   opt_reco == 'HLT_TRKv00':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_cfg      import cms, process
# elif opt_reco == 'HLT_TRKv00_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_TICL_cfg import cms, process
# elif opt_reco == 'HLT_TRKv02':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_cfg      import cms, process
# elif opt_reco == 'HLT_TRKv02_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_TICL_cfg import cms, process
# elif opt_reco == 'HLT_TRKv06':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_cfg      import cms, process
# elif opt_reco == 'HLT_TRKv06_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_TICL_cfg import cms, process
# elif opt_reco == 'HLT_TRKv06p1':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_cfg      import cms, process
# elif opt_reco == 'HLT_TRKv06p1_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_TICL_cfg import cms, process
# elif opt_reco == 'HLT_TRKv07p2':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_cfg      import cms, process
# elif opt_reco == 'HLT_TRKv07p2_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_TICL_cfg import cms, process
# else:
#    raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"')
#
# opt_BTVreco = opts.BTVreco
# if opt_BTVreco == 'default':
#       from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV import customize_hltPhase2_BTV
#       process = customize_hltPhase2_BTV(process)
# elif opt_BTVreco == 'cutsV1':
#       from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cuts import customize_hltPhase2_BTV
#       process = customize_hltPhase2_BTV(process)
# elif opt_BTVreco == 'cutsV2':
#       from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cutsV2 import customize_hltPhase2_BTV
#       process = customize_hltPhase2_BTV(process)
# else:
#    raise RuntimeError('invalid argument for option "BTVreco": "'+opt_BTVreco+'"')
#
#
# skimming of tracks
# if opt_skimTracks:
#    from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
#    process = customize_hltPhase2_skimmedTracks(process)
#
from RecoBTag.PerformanceMeasurements.Configs.testTriggerPaths_cfg import customize_hltPhase2_BTV_paths
process = customize_hltPhase2_BTV_paths(opts.reco, opts.BTVreco)


# reset path to EDM input files
process.source.fileNames = []
process.source.secondaryFileNames = []

process.schedule_().append(process.MC_JME)

process.schedule_().extend([
    process.noFilter_PFDeepCSVPuppi,
    process.noFilter_PFDeepFlavourPuppi
    ])

process.noFilter_PFDeepCSV_path = cms.Path(process.HLTBtagDeepCSVSequencePF)
process.noFilter_PFProba_path = cms.Path(process.HLTBtagProbabiltySequencePF)
process.noFilter_PFBProba_path = cms.Path(process.HLTBtagBProbabiltySequencePF)
process.noFilter_PFDeepCSVPuppi_path = cms.Path(process.HLTBtagDeepCSVSequencePFPuppi)
process.noFilter_PFDeepFlavourPuppi_path = cms.Path(process.HLTBtagDeepFlavourSequencePFPuppi)
process.noFilter_PFProbaPuppi_path = cms.Path(process.HLTBtagProbabiltySequencePFPuppi)
process.noFilter_PFBProbaPuppi_path = cms.Path(process.HLTBtagBProbabiltySequencePFPuppi)

process.schedule.extend([process.noFilter_PFDeepCSV_path, process.noFilter_PFProba_path, process.noFilter_PFBProba_path])
process.schedule.extend([process.noFilter_PFDeepCSVPuppi_path, process.noFilter_PFProbaPuppi_path, process.noFilter_PFBProbaPuppi_path, process.noFilter_PFDeepFlavourPuppi_path])


# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)

# show cmsRun summary at job completion
process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

# MessageLogger
if opts.logs:
   process.MessageLogger = cms.Service('MessageLogger',
     destinations = cms.untracked.vstring(
       'cerr',
       'logError',
       'logInfo',
       'logDebug',
     ),
     # scram b USER_CXXFLAGS="-DEDM_ML_DEBUG"
     debugModules = cms.untracked.vstring(
       'PixelVerticesSelector',
       'TracksClosestToFirstVerticesSelector',
       'JMETriggerNTuple',
     ),
     categories = cms.untracked.vstring(
       'FwkReport',
     ),
     cerr = cms.untracked.PSet(
       threshold = cms.untracked.string('WARNING'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logError = cms.untracked.PSet(
       threshold = cms.untracked.string('ERROR'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logInfo = cms.untracked.PSet(
       threshold = cms.untracked.string('INFO'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
     logDebug = cms.untracked.PSet(
       threshold = cms.untracked.string('DEBUG'),
       extension = cms.untracked.string('.txt'),
       FwkReport = cms.untracked.PSet(
         reportEvery = cms.untracked.int32(1),
       ),
     ),
   )

# input EDM files [primary]
if opts.inputFiles:
   process.source.fileNames = opts.inputFiles
else:
   process.source.fileNames = [
     # "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/003ACFBC-23B2-EA45-9A12-BECFF07760FC.root"
     "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280001/24F29B43-B3E2-9048-9BFD-9A1FC232B4A6.root"
     # "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/VBF_HHTo4B_CV_0_5_C2V_1_C3_1_TuneCP5_PSWeights_14TeV-madgraph-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/08904C2F-2A34-1C45-86B3-F05541DB0C00.root"
     # " /store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph_pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v1/130000/45253B8E-D22A-BF43-9BA8-92F4C0391B0A.root"
     # "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/250000/95FB2E3E-1DA2-FC4C-82D6-0BEB5C0195E3.root"
     # "/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/QCD_Pt-15to20_EMEnriched_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_111X_mcRun4_realistic_T15_v1-v1/110000/2CFDBC2B-460F-9C45-9383-2F41381DD9C0.root"
   ]


#===========
# Begin BTagAna

###############################
####### Parameters ############
###############################

groups = ["HLTEventInfo","HLTJetInfo","HLTTagVar","HLTJetTrack","HLTJetSV","HLTCSVTagVar","HLTDeepFlavourVar"]
groups.append("L1ObjectInfo")
groups.append("JetTruthInfo")


from RecoBTag.PerformanceMeasurements.BTagAnalyzer_cff import *
btagana_tmp = bTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
# for requiredGroup in options.groups:
for requiredGroup in groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        if "CaloJet." in var:
          var = var.split(".")[1]
        if "PFJet." in var:
          var = var.split(".")[1]
        if "PuppiJet." in var:
          var = var.split(".")[1]
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')



# update process.GlobalTag.globaltag
if opts.globalTag is not None:
   from Configuration.AlCa.GlobalTag import GlobalTag
   process.GlobalTag = GlobalTag(process.GlobalTag, opts.globalTag, '')

# fix for AK4PF Phase-2 JECs
# process.GlobalTag.toGet.append(cms.PSet(
#   record = cms.string('JetCorrectionsRecord'),
#   tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_AK4PF'),
#   label = cms.untracked.string('AK4PF'),
# ))

# process.CondDB.connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/L1TObjScaling.db'
# process.L1TScalingESSource.connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/L1TObjScaling.db'

#~ outFilename = 'JetTree_mc.root'
outFilename = opts.outName
# process.RECOoutput.fileName=opts.outName

## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(outFilename)
)


process.selectedHadronsAndPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("genParticles::HLT"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator","","SIM")
)


process.ak4JetFlavourInfos = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
    cHadrons = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("hltAK4PFPuppiJetsCorrected"),
    weights = cms.InputTag("hltPFPuppi"),
    leptons = cms.InputTag("selectedHadronsAndPartons","leptons"),
    partons = cms.InputTag("selectedHadronsAndPartons","physicsPartons"),
    rParam = cms.double(0.4),
    relPtTolerance = cms.double(5) # because of JES corrections applied
)

process.jetPartonMatchPuppi = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles::HLT"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5,
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hltAK4PFPuppiJetsCorrected")
)

process.jetGenJetMatchPuppi = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    # matched = cms.InputTag("slimmedGenJets"),
    matched = cms.InputTag("ak4GenJetsNoNu::HLT"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hltAK4PFPuppiJetsCorrected")
)

# process.patJetFlavourAssociationLegacyPuppi = cms.EDProducer("JetFlavourIdentifier",
#     physicsDefinition = cms.bool(False),
#     srcByReference = cms.InputTag("patJetPartonAssociationLegacyPuppi")
# )
# process.patJetPartonAssociationLegacyPuppi = cms.EDProducer("JetPartonMatcher",
#     coneSizeToAssociate = cms.double(0.3),
#     jets = cms.InputTag("ak4PFJetsPuppi"),
#     partons = cms.InputTag("patJetPartonsLegacy")
# )
# process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
#     src = cms.InputTag("genParticles"),
#     withLeptons = cms.bool(False)
# )

process.jetMatchingPath = cms.Path(process.selectedHadronsAndPartons*process.ak4JetFlavourInfos*process.jetPartonMatchPuppi*process.jetGenJetMatchPuppi)
process.schedule.extend([process.jetMatchingPath])

from JMETriggerAnalysis.NTuplizers.qcdWeightProducer import qcdWeightProducer
process.qcdWeightPU140 = qcdWeightProducer(BXFrequency = 30. * 1e6, PU = 140.)
process.qcdWeightPU200 = qcdWeightProducer(BXFrequency = 30. * 1e6, PU = 200.)
process.qcdWeightpath = cms.Path(process.qcdWeightPU140*process.qcdWeightPU200)
process.schedule.extend([process.qcdWeightpath])

#-------------------------------------
from RecoBTag.PerformanceMeasurements.BTagHLTAnalyzer_cff import *
process.btagana = bTagHLTAnalyzer.clone()

#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = 4.5
process.btagana.MinPt                 = 25
# process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLTX') # Data and MC
# process.btagana.triggerTable          = cms.InputTag('TriggerResults') # Data and MC
process.btagana.triggerTable          = cms.InputTag("TriggerResults","","HLTX") # Data and MC
process.btagana.HLTTriggerPathNames   = cms.vstring(
    'MC_JME',
      # L1T seeds
    'L1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1',
    'L1_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_p71_2p4_v1',

      # general paths and filters
    'L1Objects',
    'HLTObjects',
    # 'QCDMuon',
    # 'Gen_QCDMuGenFilter',
    # 'Gen_QCDEmEnrichingNoBCToEFilter',
    # 'Gen_QCDEmEnrichingFilter',
    # 'Gen_QCDBCToEFilter',
    'noFilter_PFDeepCSVPuppi',
    'noFilter_PFDeepFlavourPuppi',

      # based on DeepCSV
    'HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1',
    'HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepCSV_2p4_v1',
    'HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_2p4_v1',


      # based on DeepJet
    'HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour_2p4_v1',
    'HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepFlavour_2p4_v1',
    'HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepFlavour_2p4_v1',
    )
# process.btagana.primaryVertexColl     = cms.InputTag('hltVerticesPF')
process.btagana.primaryVertexColl     = cms.InputTag('offlinePrimaryVertices') #change with new Offline like sequence
# process.btagana.primaryVertexColl     = cms.InputTag('goodOfflinePrimaryVertices') #change with new Offline like sequence

process.btagana.runHLTJetVariables     = cms.bool(True)
process.btagana.runDeepFlavourTagVariables     = cms.bool(True)
process.btagana.runOnData = False

process.btagana.runTruthFlavor = cms.bool(True)

# if opts.FastPV:
    # process.btagana.PFJets               = cms.InputTag('hltAK4PFCHSJetsCorrected')
    # process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosFastPV')
    # process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPFFastPV')
    # process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFFastPV:probb')
    # process.btagana.PFJetBPBJetTags      = cms.InputTag('hltPfJetBProbabilityBJetTagsFastPV')
    # process.btagana.PFJetPBJetTags       = cms.InputTag('hltPfJetProbabilityBJetTagsFastPV')
    #
    # process.btagana.PuppiJets            = cms.InputTag('hltAK4PuppiJetsCorrected')
    # process.btagana.PuppiJetTags         = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiFastPV')
    # process.btagana.PuppiSVs             = cms.InputTag('hltDeepSecondaryVertexTagInfosPFPuppiFastPV')
    # process.btagana.PuppiJetDeepCSVTags  = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppiFastPV:probb')
    # process.btagana.PuppiJetBPBJetTags   = cms.InputTag('hltPfJetBProbabilityBJetTagsPuppiFastPV')
    # process.btagana.PuppiJetPBJetTags    = cms.InputTag('hltPfJetProbabilityBJetTagsPuppiFastPV')
    # process.btagana.PuppiJetCSVTags      = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppiFastPV')
# else:
process.btagana.PFJets               = cms.InputTag('hltAK4PFCHSJetsCorrected')
process.btagana.PFJetTags            = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfos')
process.btagana.PFSVs                = cms.InputTag('hltDeepSecondaryVertexTagInfosPF')
process.btagana.PFJetDeepCSVTags     = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF:probb')
process.btagana.PFJetBPBJetTags      = cms.InputTag('hltPfJetBProbabilityBJetTags')
process.btagana.PFJetPBJetTags       = cms.InputTag('hltPfJetProbabilityBJetTags')

process.btagana.GenJets              = cms.InputTag('ak4GenJetsNoNu::HLT')
process.btagana.GenParticles         = cms.InputTag("genParticles::HLT")


process.btagana.HepMCProduct = cms.InputTag("generatorSmeared","","SIM")
process.btagana.GenEventInfoProduct = cms.InputTag('generator')
process.btagana.PileupSummaryInfo = cms.InputTag('addPileupInfo')

process.btagana.qcdWeightPU140 = cms.InputTag('qcdWeightPU140')
process.btagana.qcdWeightPU200 = cms.InputTag('qcdWeightPU200')



process.btagana.PuppiJets            = cms.InputTag('hltAK4PFPuppiJetsCorrected')
process.btagana.PuppiJetsFlavorInfos = cms.InputTag('ak4JetFlavourInfos')
process.btagana.PuppiJetsMatchedGenJets = cms.InputTag('jetGenJetMatchPuppi')
process.btagana.PuppiJetsMatchedGenPartons = cms.InputTag('jetPartonMatchPuppi')
process.btagana.PuppiJetTags         = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi')
process.btagana.PuppiDeepFlavourTags = cms.InputTag('hltPfDeepFlavourTagInfos')
process.btagana.PuppiSVs             = cms.InputTag('hltDeepSecondaryVertexTagInfosPFPuppi')
process.btagana.PuppiJetDeepCSVTags  = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPFPuppi:probb')
# process.btagana.PuppiJetBPBJetTags   = cms.InputTag('hltPfJetBProbabilityBJetTagsPuppi')
# process.btagana.PuppiJetPBJetTags    = cms.InputTag('hltPfJetProbabilityBJetTagsPuppi')
# process.btagana.PuppiJetCSVTags      = cms.InputTag('hltCombinedSecondaryVertexBJetTagsPFPuppi')
process.btagana.PuppiJetDeepFlavourTags     = cms.InputTag('hltPfDeepFlavourJetTags:probb')
process.btagana.PuppiJetDeepFlavourTags_bb  = cms.InputTag('hltPfDeepFlavourJetTags:probbb')
process.btagana.PuppiJetDeepFlavourTags_lb  = cms.InputTag('hltPfDeepFlavourJetTags:problepb')

process.btagana.HLTPuppiHTEta2p4            = cms.InputTag('hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4')
# process.btagana.HLTPuppiHTEta4p0            = cms.InputTag('hltHtMhtPFPuppiCentralJetsQuadC30MaxEta4p0')
process.btagana.HLTPuppiHTEta4p0            = cms.InputTag('hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4')
process.btagana.HLTPuppiHTJME               = cms.InputTag('hltPFPuppiHT')

process.btagana.analyzeL1Objects            =  cms.bool(True)
process.btagana.L1VertexColl                =  cms.InputTag('L1TkPrimaryVertex')
process.btagana.L1BarrelTrackColl           =  cms.InputTag('pfTracksFromL1TracksBarrel')
process.btagana.L1HGcalTrackColl            =  cms.InputTag('pfTracksFromL1TracksHGCal')
process.btagana.L1PFJets                    =  cms.InputTag('ak4PFL1PuppiCorrected')
process.btagana.L1PuppiJets                 =  cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates')
# process.btagana.L1PuppiJets               =  cms.InputTag('l1tSlwPFPuppiJetsCorrected')
# process.btagana.L1HT                        =  cms.InputTag('l1tPFPuppiHT')
process.btagana.L1HT                        =  cms.InputTag('l1tPFPuppiHTMaxEta2p4')
process.btagana.L1ExtendedTracks            =  cms.InputTag('TTTracksFromExtendedTrackletEmulation','Level1TTTracks')
process.btagana.L1Tracks                    =  cms.InputTag('TTTracksFromTrackletEmulation','Level1TTTracks')

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------

# update JESC via local SQLite file
# from CondCore.CondDB.CondDB_cfi import CondDB
# CondDBJECFile = CondDB.clone(connect = 'sqlite_fip:RecoBTag/PerformanceMeasurements/data/PhaseIIFall17_V5b_MC.db' )
# process.jec = cms.ESSource('PoolDBESSource', CondDBJECFile, toGet = cms.VPSet())
# for _tmp in [
#   'AK4PF',
# #      'AK4PFchs',
# #      'AK4PFPuppi',
# #      'AK8PF',
# #      'AK8PFchs',
# #      'AK8PFPuppi',
# ]:
#   process.jec.toGet.append(
#     cms.PSet(
#       record = cms.string('JetCorrectionsRecord'),
#       tag = cms.string('JetCorrectorParametersCollection_PhaseIIFall17_V5b_MC_'+_tmp),
#       label = cms.untracked.string(_tmp),
#     )
#   )

# Add an ESPrefer to override JEC that might be available from the global tag
# process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

# Tracking Monitoring
if opts.trkdqm > 0:

   if opt_reco in ['HLT_TRKv00', 'HLT_TRKv00_TICL', 'HLT_TRKv02', 'HLT_TRKv02_TICL']:
      process.reconstruction_pixelTrackingOnly_step = cms.Path(process.reconstruction_pixelTrackingOnly)
      process.schedule_().extend([process.reconstruction_pixelTrackingOnly_step])

   from JMETriggerAnalysis.Common.trackHistogrammer_cfi import trackHistogrammer
   process.TrackHistograms_hltPixelTracks = trackHistogrammer.clone(src = 'pixelTracks')
   process.TrackHistograms_hltInitialStepTracks = trackHistogrammer.clone(src = 'initialStepTracks')
   process.TrackHistograms_hltGeneralTracks = trackHistogrammer.clone(src = 'generalTracks')

   process.trkMonitoringSeq = cms.Sequence(
       process.TrackHistograms_hltPixelTracks
     + process.TrackHistograms_hltInitialStepTracks
     + process.TrackHistograms_hltGeneralTracks
   )

   if opt_skimTracks:
      process.TrackHistograms_hltGeneralTracksOriginal = trackHistogrammer.clone(src = 'generalTracksOriginal')
      process.trkMonitoringSeq += process.TrackHistograms_hltGeneralTracksOriginal

   process.trkMonitoringEndPath = cms.EndPath(process.trkMonitoringSeq)
   process.schedule_().extend([process.trkMonitoringEndPath])

# Vertexing monitoring
if opts.pvdqm > 0:

    from JMETriggerAnalysis.Common.vertexHistogrammer_cfi import vertexHistogrammer
    process.VertexHistograms_hltPixelVertices = vertexHistogrammer.clone(src = 'pixelVertices')
    process.VertexHistograms_hltTrimmedPixelVertices = vertexHistogrammer.clone(src = 'trimmedPixelVertices')
    process.VertexHistograms_hltPrimaryVertices = vertexHistogrammer.clone(src = 'offlinePrimaryVertices')
    process.VertexHistograms_hltPrimaryVerticesGood = vertexHistogrammer.clone(src = 'goodOfflinePrimaryVertices')
    process.VertexHistograms_offlinePrimaryVertices = vertexHistogrammer.clone(src = 'offlineSlimmedPrimaryVertices')

    process.pvMonitoringSeq = cms.Sequence(
        process.VertexHistograms_hltPixelVertices
        + process.VertexHistograms_hltTrimmedPixelVertices
        + process.VertexHistograms_hltPrimaryVertices
        + process.VertexHistograms_hltPrimaryVerticesGood
        + process.VertexHistograms_offlinePrimaryVertices
    )

# if opts.pvdqm > 1:
#
#     if not hasattr(process, 'tpClusterProducer'):
#         from SimTracker.TrackerHitAssociation.tpClusterProducer_cfi import tpClusterProducer as _tpClusterProducer
#         process.tpClusterProducer = _tpClusterProducer.clone()
#
#     from SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi import quickTrackAssociatorByHits as _quickTrackAssociatorByHits
#     process.quickTrackAssociatorByHits = _quickTrackAssociatorByHits.clone()
#
#     from SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi import trackingParticleRecoTrackAsssociation as _trackingParticleRecoTrackAsssociation
#     process.trackingParticleRecoTrackAsssociation = _trackingParticleRecoTrackAsssociation.clone()
#
#     process.trackingParticlePixelTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
#         associator = cms.InputTag('quickTrackAssociatorByHits'),
#         ignoremissingtrackcollection = cms.untracked.bool(False),
#         label_tp = cms.InputTag('mix', 'MergedTrackTruth'),
#         label_tr = cms.InputTag('pixelTracks')
#     )
#
#     process.trkTruthInfoSeq = cms.Sequence(
#         process.tpClusterProducer
#         + process.quickTrackAssociatorByHits
#         + process.trackingParticleRecoTrackAsssociation
#         + process.trackingParticlePixelTrackAssociation
#     )
#
#     process.trkTruthInfoPath = cms.Path(process.trkTruthInfoSeq)
#     process.schedule_().extend([process.trkTruthInfoPath])
#
#     if hasattr(process, 'pixelVertices') or hasattr(process, 'trimmedPixelVertices'):
#         process.pvAnalyzer1 = cms.EDAnalyzer('PrimaryVertexAnalyzer4PU',
#             info = cms.untracked.string(opts.reco),
#             f4D = cms.untracked.bool(False),
#             beamSpot = cms.InputTag('offlineBeamSpot'),
#             simG4 = cms.InputTag('g4SimHits'),
#             outputFile = cms.untracked.string('pv_hltPixelVertices.root'),
#             verbose = cms.untracked.bool(False),
#             veryverbose = cms.untracked.bool(False),
#             recoTrackProducer = cms.untracked.string('pixelTracks'),
#             minNDOF = cms.untracked.double(-1),
#             zmatch = cms.untracked.double(0.05),
#             autodump = cms.untracked.int32(0),
#             nDump = cms.untracked.int32(0),
#             nDumpTracks = cms.untracked.int32(0),
#             RECO = cms.untracked.bool(False),
#             track_timing = cms.untracked.bool(True),
#             TkFilterParameters = cms.PSet(
#                 maxD0Error = cms.double(999.0),
#                 maxD0Significance = cms.double(999.0),
#                 maxDzError = cms.double(999.0),
#                 maxEta = cms.double(4.0),
#                 maxNormalizedChi2 = cms.double(999.0),
#                 minPixelLayersWithHits = cms.int32(2),
#                 minPt = cms.double(1.0),
#                 minSiliconLayersWithHits = cms.int32(-1),
#                 trackQuality = cms.string('any')
#             ),
#             trackingParticleCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
#             trackingVertexCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
#             trackAssociatorMap = cms.untracked.InputTag('trackingParticlePixelTrackAssociation'),
#             TrackTimesLabel = cms.untracked.InputTag('tofPID4DnoPID:t0safe'), # as opposed to 'tofPID:t0safe'
#             TrackTimeResosLabel = cms.untracked.InputTag('tofPID4DnoPID:sigmat0safe'),
#             vertexAssociator = cms.untracked.InputTag(''),
#             useVertexFilter = cms.untracked.bool(False),
#             compareCollections = cms.untracked.int32(0),
#             vertexRecoCollections = cms.VInputTag(),
#         )
#
#     for _tmp in ['pixelVertices', 'trimmedPixelVertices']:
#         if hasattr(process, _tmp):
#             process.pvAnalyzer1.vertexRecoCollections += [_tmp]
#
#     process.pvMonitoringSeq += process.pvAnalyzer1
#
#     if hasattr(process, 'offlinePrimaryVertices'):
#         process.pvAnalyzer2 = cms.EDAnalyzer('PrimaryVertexAnalyzer4PU',
#             info = cms.untracked.string(opts.reco),
#             f4D = cms.untracked.bool(False),
#             beamSpot = cms.InputTag('offlineBeamSpot'),
#             simG4 = cms.InputTag('g4SimHits'),
#             outputFile = cms.untracked.string('pv_hltPrimaryVertices.root'),
#             verbose = cms.untracked.bool(False),
#             veryverbose = cms.untracked.bool(False),
#             recoTrackProducer = cms.untracked.string('generalTracks'),
#             minNDOF = cms.untracked.double(4.0),
#             zmatch = cms.untracked.double(0.05),
#             autodump = cms.untracked.int32(0),
#             nDump = cms.untracked.int32(0),
#             nDumpTracks = cms.untracked.int32(0),
#             RECO = cms.untracked.bool(False),
#             track_timing = cms.untracked.bool(True),
#             TkFilterParameters = cms.PSet(
#                 maxD0Error = cms.double(1.0),
#                 maxD0Significance = cms.double(4.0),
#                 maxDzError = cms.double(1.0),
#                 maxEta = cms.double(4.0),
#                 maxNormalizedChi2 = cms.double(10.0),
#                 minPixelLayersWithHits = cms.int32(2),
#                 minPt = cms.double(0.0),
#                 minSiliconLayersWithHits = cms.int32(5),
#                 trackQuality = cms.string('any')
#             ),
#             trackingParticleCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
#             trackingVertexCollection = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
#             trackAssociatorMap = cms.untracked.InputTag('trackingParticleRecoTrackAsssociation'),
#             TrackTimesLabel = cms.untracked.InputTag('tofPID4DnoPID:t0safe'),  # as opposed to 'tofPID:t0safe'
#             TrackTimeResosLabel = cms.untracked.InputTag('tofPID4DnoPID:sigmat0safe'),
#             vertexAssociator = cms.untracked.InputTag(''),
#             useVertexFilter = cms.untracked.bool(False),
#             compareCollections = cms.untracked.int32(0),
#             vertexRecoCollections = cms.VInputTag(
#             'offlinePrimaryVertices',
#             ),
#         )
#     process.pvMonitoringSeq += process.pvAnalyzer2
#
#     process.pvMonitoringEndPath = cms.EndPath(process.pvMonitoringSeq)
#     process.schedule_().extend([process.pvMonitoringEndPath])

# L1T Monitoring
if opts.l1tdqm:
    from JMETriggerAnalysis.Common.l1tPFTrackHistogrammer_cfi import l1tPFTrackHistogrammer
    from JMETriggerAnalysis.Common.l1tVertexHistogrammer_cfi import l1tVertexHistogrammer
    from JMETriggerAnalysis.Common.l1tPFJetHistogrammer_cfi import l1tPFJetHistogrammer
    from JMETriggerAnalysis.Common.pfJetHistogrammer_cfi import pfJetHistogrammer
    process.TrackHistograms_L1BarrelTracks = l1tPFTrackHistogrammer.clone(src = 'pfTracksFromL1TracksBarrel')
    process.TrackHistograms_L1HGCalTracks = l1tPFTrackHistogrammer.clone(src = 'pfTracksFromL1TracksHGCal')
    # process.trkMonitoringSeq += process.TrackHistograms_L1BarrelTracks
    # process.trkMonitoringSeq += process.TrackHistograms_L1HGCalTracks
    process.VertexHistograms_L1PrimaryVertices = l1tVertexHistogrammer.clone(src = 'L1TkPrimaryVertex')
    # process.trkMonitoringSeq += process.VertexHistograms_L1PrimaryVertices
    process.JetHistograms_L1PFCHSCorrected = l1tPFJetHistogrammer.clone(src = 'l1tSlwPFJetsCorrected')
    process.JetHistograms_L1PFPUPPICorrected = l1tPFJetHistogrammer.clone(src = 'l1tSlwPFPuppiJetsCorrected')
    # process.JetHistograms_L1PFCHS = pfJetHistogrammer.clone(src = 'ak4PFL1PF')
    # process.JetHistograms_L1PFPUPPI = pfJetHistogrammer.clone(src = 'ak4PFL1Puppi')
    # process.trkMonitoringSeq += process.JetHistograms_L1PFCHSCorrected
    # process.trkMonitoringSeq += process.JetHistograms_L1PFPUPPICorrected
    # process.trkMonitoringSeq += process.JetHistograms_L1PFCHS
    # process.trkMonitoringSeq += process.JetHistograms_L1PFPUPPI

    process.l1MonitoringSeq = cms.Sequence(
       process.TrackHistograms_L1BarrelTracks
     + process.TrackHistograms_L1HGCalTracks
     # + process.VertexHistograms_L1PrimaryVertices
     + process.JetHistograms_L1PFCHSCorrected
     + process.JetHistograms_L1PFPUPPICorrected
     # + process.JetHistograms_L1PFCHS
     # + process.JetHistograms_L1PFPUPPI
    )
    process.l1MonitoringEndPath = cms.EndPath(process.l1MonitoringSeq)
    process.schedule.extend([process.l1MonitoringEndPath])

# ParticleFlow Monitoring
if opts.pfdqm > 0:

    from JMETriggerAnalysis.Common.pfCandidateHistogrammerRecoPFCandidate_cfi import pfCandidateHistogrammerRecoPFCandidate
    from JMETriggerAnalysis.Common.pfCandidateHistogrammerPatPackedCandidate_cfi import pfCandidateHistogrammerPatPackedCandidate
    from JMETriggerAnalysis.Common.leafCandidateHistogrammer_cfi import leafCandidateHistogrammer

    _candTags = [
        ('_offlineParticleFlow', 'packedPFCandidates', '', pfCandidateHistogrammerPatPackedCandidate),
        ('_hltParticleFlow', 'particleFlowTmp', '', pfCandidateHistogrammerRecoPFCandidate),
        ('_hltPFPuppi', 'hltPFPuppi', '(pt > 0)', pfCandidateHistogrammerRecoPFCandidate),
        # ('_l1tParticleFlow', 'l1pfCandidates:PF', '', leafCandidateHistogrammer),
        ('_l1tPFPuppi', 'l1pfCandidates:Puppi', '(pt > 0)', leafCandidateHistogrammer),
    ]

    if 'TICL' in opt_reco:
        _candTags += [
            ('_pfTICL', 'pfTICL', '', pfCandidateHistogrammerRecoPFCandidate),
        ]
    else:
        _candTags += [
            ('_simPFProducer', 'simPFProducer', '', pfCandidateHistogrammerRecoPFCandidate),
        ]

    if opts.pfdqm > 2:
        _tmpCandTags = []
        for _tmp in _candTags:
            _tmpCandTags += [(_tmp[0]+'_2GeV', _tmp[1], '(pt > 2.)', _tmp[3])]
            _candTags += _tmpCandTags
        del _tmpCandTags

    _regTags = [
        ['', ''],
        ['_HB'   , '(0.0<=abs(eta) && abs(eta)<1.5)'],
        ['_HGCal', '(1.5<=abs(eta) && abs(eta)<3.0)'],
        ['_HF'   , '(3.0<=abs(eta) && abs(eta)<5.0)'],
    ]

    _pidTags = [['', '']]
    if opts.pfdqm > 1:
        _pidTags += [
            ['_h', '(abs(pdgId) == 211)'],
            ['_e', '(abs(pdgId) == 11)'],
            ['_mu', '(abs(pdgId) == 13)'],
            ['_gamma', '(abs(pdgId) == 22)'],
            ['_h0', '(abs(pdgId) == 130)'],
        ]

    process.pfMonitoringSeq = cms.Sequence()
    for _candTag in _candTags:
        for _regTag in _regTags:
            for _pidTag in _pidTags:
                _modName = 'PFCandidateHistograms'+_candTag[0]+_regTag[0]+_pidTag[0]
                setattr(process, _modName, _candTag[3].clone(
                src = _candTag[1],
                cut = ' && '.join([_tmp for _tmp in [_candTag[2], _regTag[1], _pidTag[1]] if _tmp]),
                ))
                process.pfMonitoringSeq += getattr(process, _modName)

    process.pfMonitoringEndPath = cms.EndPath(process.pfMonitoringSeq)
    process.schedule_().extend([process.pfMonitoringEndPath])


process.p = cms.Path(
    process.allEvents
    * process.selectedEvents
)
process.schedule.extend([process.p])
process.analysisNTupleEndPath = cms.EndPath(process.btagana)
process.schedule.extend([process.analysisNTupleEndPath])

process.prune()

# dump content of cms.Process to python file
if opts.dumpPython is not None:
   open(opts.dumpPython, 'w').write(process.dumpPython())


# print-outs
print '--- runHLTBTagAnalyzer_PhaseII_cfg.py ---\n'
print 'process.maxEvents.input =', process.maxEvents.input
print 'process.source.skipEvents =', process.source.skipEvents
print 'process.source.fileNames =', process.source.fileNames
print 'process.source.secondaryFileNames =', process.source.secondaryFileNames
print 'numThreads =', opts.numThreads
print 'numStreams =', opts.numStreams
print 'logs =', opts.logs
print 'wantSummary =', opts.wantSummary
print 'process.GlobalTag =', process.GlobalTag.dumpPython()
print 'process.source =', process.source.dumpPython()
print 'process.maxEvents =', process.maxEvents.dumpPython()
print 'option: dumpPython =', opts.dumpPython
print ''
print 'option: trkdqm =', opts.trkdqm
print 'option: pfdqm =', opts.pfdqm
print 'option: reco =', opt_reco, '(skimTracks = '+str(opt_skimTracks)+')'
print 'option: BTVreco =', opts.BTVreco
print '\n-------------------------------'
