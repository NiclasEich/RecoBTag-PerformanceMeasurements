###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to python file with content of cms.Process')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('lumis', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to .json with list of luminosity sections')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('globalTag', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('reco', 'HLT_GRun',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'keyword to define HLT reconstruction')

opts.register('output', 'out.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to output ROOT file')

opts.register('verbosity', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'level of output verbosity')

opts.parseArguments()

###
### HLT configuration
###
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

from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_Data_NoOutput_configDump import cms, process

if opts.reco == 'HLT_GRun_oldJECs':
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_GRun':
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_GRun_PatatrackQuadruplets':
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Quadruplets only) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrack
    process = customizeHLTforPatatrack(process)
    update_jmeCalibs = True
    # process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_GRun_PatatrackTriplets':
    # default GRun menu (Run 2 configurations) + Patatrack pixeltracks (Triplets+Quadruplets) instead of legacy pixeltracks
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrackTriplets
    process = customizeHLTforPatatrackTriplets(process)
    update_jmeCalibs = True
    # process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)


elif opts.reco == 'HLT_Run3TRK':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    update_jmeCalibs = True
    process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif options.reco == 'HLT_Run3TRK_ROICaloROIPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_ROIPF import *
    process = customizeRun3_BTag_ROICalo_ROIPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif options.reco == 'HLT_Run3TRK_noCaloROIPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_noCalo_ROIPF import *
    process = customizeRun3_BTag_noCalo_ROIPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif options.reco == 'HLT_Run3TRK_ROICaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_ROICalo_GlobalPF import *
    process = customizeRun3_BTag_ROICalo_GlobalPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif options.reco == 'HLT_Run3TRK_GlobalCaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_GlobalCalo_GlobalPF import *
    process = customizeRun3_BTag_GlobalCalo_GlobalPF(process, options.addDeepJet)
    update_jmeCalibs = True
    process = fixMenu(process)
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)
else:
    raise RuntimeError('keyword "reco = '+opts.reco+'" not recognised')

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
        _CondDB.clone(connect = 'sqlite_file:'+os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db'),
        toGet = cms.VPSet(
            cms.PSet(
                record = cms.string('PFCalibrationRcd'),
                tag = cms.string('PFCalibration_HLT_mcRun3_2021'),
                label = cms.untracked.string('HLT'),
            ),
        ),
    )
    process.pfhcESPrefer = cms.ESPrefer('PoolDBESSource', 'pfhcESSource')
    #process.hltParticleFlow.calibrationsLabel = '' # standard label for Offline-PFHC in GT

  ## ES modules for HLT JECs
    process.jescESSource = cms.ESSource('PoolDBESSource',
    _CondDB.clone(connect = 'sqlite_file:'+os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db'),
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

###
### output
###
if hasattr(process, 'DQMOutput'):
    process.DQMOutput.remove(process.dqmOutput)

process.hltOutput = cms.OutputModule('PoolOutputModule',
    fileName = cms.untracked.string(opts.output),
    fastCloning = cms.untracked.bool(False),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep edmTriggerResults_*_*_'+process.name_(),
    )
)

process.hltOutputEndPath = cms.EndPath(process.hltOutput)

###
### standard options
###

# max number of events to be processed
process.maxEvents.input = opts.maxEvents

# number of events to be skipped
process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

# multi-threading settings
process.options.numberOfThreads = max(opts.numThreads, 1)
process.options.numberOfStreams = max(opts.numStreams, 0)

# show cmsRun summary at job completion
process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

# update process.GlobalTag.globaltag
if opts.globalTag is not None:
    from Configuration.AlCa.GlobalTag import GlobalTag
    process.GlobalTag = GlobalTag(process.GlobalTag, opts.globalTag, '')

# select luminosity sections from .json file
if opts.lumis is not None:
    import FWCore.PythonUtilities.LumiList as LumiList
    process.source.lumisToProcess = LumiList.LumiList(filename = opts.lumis).getVLuminosityBlockRange()

# input EDM files [primary]
if opts.inputFiles:
    process.source.fileNames = opts.inputFiles
else:
    process.source.fileNames = [
        '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/65EA98C3-88C1-5A43-8152-824F3169174E.root',
    ]

# input EDM files [secondary]
if not hasattr(process.source, 'secondaryFileNames'):
    process.source.secondaryFileNames = cms.untracked.vstring()

if opts.secondaryInputFiles:
    process.source.secondaryFileNames = opts.secondaryInputFiles
else:
    process.source.secondaryFileNames = [
    ]

# dump content of cms.Process to python file
if opts.dumpPython is not None:
    open(opts.dumpPython, 'w').write(process.dumpPython())

# printouts
if opts.verbosity > 0:
    print ('--- hltResults_cfg.py ---------')
    print ('')
    print ('option: output =', opts.output)
    print ('option: reco =', opts.reco)
    print ('option: dumpPython =', opts.dumpPython)
    print ('')
    print ('process.name_() =', process.name_())
    print ('process.GlobalTag =', process.GlobalTag.dumpPython())
    print ('process.source =', process.source.dumpPython())
    print ('process.maxEvents =', process.maxEvents.dumpPython())
    print ('process.options =', process.options.dumpPython())
    print ('-------------------------------')
