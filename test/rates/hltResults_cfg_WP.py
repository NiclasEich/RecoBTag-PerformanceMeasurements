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

opts.register('addDeepJet', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'add DeepJet paths to reconstruction')

opts.register('replaceBTagMuPaths', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'renaming BTagMu NoAlgo paths in reconstruction')

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

# from RecoBTa .PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_2_0_GRun_Data_NoOutput_configDump import cms, process
# from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_12_3_0_GRun_Data_NoOutput_configDump import cms, process
from tmpRates_dump import cms, process

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

elif opts.reco == 'HLT_Run3TRK_ROICaloROIPF':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloROIPF_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_noCaloROIPF':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    # process = MUO_newReco(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_noCaloROIPF_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    # process = MUO_newReco(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_noCaloROIPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_noCaloROIPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_noCalo_roiPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloROIPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloROIPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_roiPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloGlobalPF_Mu':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloGlobalPF_Mu_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloGlobalPF':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = True
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_ROICaloGlobalPF_oldJECs':
    from HLTrigger.Configuration.customizeHLTforRun3 import *
    process = TRK_newTracking(process)
    process = MUO_newReco(process)
    process = BTV_roiCalo_globalPF_DeepJet(process)
    update_jmeCalibs = False
    prescale_path(process.DST_Run3_PFScoutingPixelTracking_v16, process.PrescaleService)

elif opts.reco == 'HLT_Run3TRK_GlobalCaloGlobalPF':
    # Run-3 tracking: standard (Triplets+Quadruplets)
    from HLTrigger.Configuration.customizeHLTforRun3Tracking import customizeHLTforRun3Tracking
    process = customizeHLTforRun3Tracking(process)
    from RecoBTag.PerformanceMeasurements.customizeRun3_BTag_GlobalCalo_GlobalPF import *
    process = customizeRun3_BTag_GlobalCalo_GlobalPF(process, opts.addDeepJet, opts.replaceBTagMuPaths)
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
process.schedule.extend([process.hltOutputEndPath])

###
"""
test new paths + WPs
"""
import numpy as np
import json

pathList =  [p for p in dir(process) if (("DeepJet" in p) or ("DeepCSV" in p)) and ("HLT_" == p[0:4])]

print("Starting to add custom WP adjustment paths")
print("all paths:")
print("- - "*20)
for basePathName in pathList:
    print(basePathName)
print("- - "*20)

for basePathName in pathList:
    print("Creating working points for {}".format(basePathName))

    basePath = getattr(process, basePathName)

    prescaleName = next(p for p in basePath.moduleNames() if "hltPre" in p)

    taggerModules = [p for p in basePath.moduleNames() if ("DeepCSV" in p or "DeepJet" in p) and ("hltBTag" in p)]

    # taggerModuleName = next(p for p in basePath.moduleNames() if ("DeepCSV" in p or "DeepJet" in p) and ("hltBTag" in p))
    if len(taggerModules) > 1:
        print("more than one taggerModule found!")
        # do not care about Calo Prefilter
        tagger = [tM for tM in taggerModules if "Calo" not in tM]

        # there might be multiple filters - then chose the sinlge jet one (tighter) 
        if len(tagger) != 1:
            if any("Double" in t for t in tagger) and any("Single" in t for t in tagger):
                tagger = [t for t in tagger if "Single" in t]
            else:
                raise ValueError("This should not happen. Make sure to delete the right calo prefilter")
            taggerModuleName = tagger[0]
        else:
            taggerModuleName = tagger[0]
    else:
        # print("bar")
        taggerModuleName = taggerModules[0]
    taggerModule = getattr(process, taggerModuleName)
    # from IPython import embed;embed()
    print()
    print("Working point for: {} minTag: {}".format(taggerModuleName, taggerModule.MinTag.value()))
    # if basePathName == "HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v8":
    # if "PFBTagDeepJet" in basePathName:
    #     discName = "hltDeepJetDiscriminatorsJetTags"
    # elif "PFBTagDeepCSV" in basePathName or "PFAK8BTagDeepCSV":
    #     discName = "hltDeepCombinedSecondaryVertexBJetTagsPF"
    # elif "CaloBTagDeepCSV" in basePathName:
    #     discName = "hltDeepCombinedSecondaryVertexBJetTagsCalo"
    # else:
    #     raise NotImplementedError("This case is not handled properly!") 

    discName =  taggerModule.JetTags.value().split(":")


    # if "DeepCombine" in discName:
    #     from IPython import embed;embed()


    # Create N working points with -0.1/+0.1 %
    for wp_diff in np.linspace(-0.1, +0.1, 7):

        # 0 < wp < 1
        wp = min( max(0.001, taggerModule.MinTag.value() + wp_diff), 0.99999)

        prescale = getattr(process, prescaleName).clone()
        prescales = next( p.prescales for p in process.PrescaleService.prescaleTable if p.pathName.value() == basePathName)

        wp_string = "{0:2d}".format(int(wp* 100))
        value = taggerModule.clone(
            JetTags = cms.InputTag(discName),
            MinTag = cms.double(wp),
        )

        discriminatorNameNew = "{}WP{}".format(taggerModuleName, wp_string)
        setattr(process, discriminatorNameNew,value)

        prescaleNameNew = "{}WP{}".format(prescaleName, wp_string)
        setattr(process, prescaleNameNew, prescale)

        newPath = basePath.copy()

        newPath.replace( getattr(process, prescaleName), getattr(process, prescaleNameNew))
        newPath.replace( getattr(process, taggerModuleName), getattr(process, discriminatorNameNew))

        newPathName = "{}_WP_{}".format(basePathName, wp_string)
        setattr(process, newPathName , newPath)

        process.schedule.extend([
            getattr(process, newPathName)
            ])

        process.PrescaleService.prescaleTable.insert(-1,
            cms.PSet(
                pathName = cms.string(newPathName),
                prescales = prescales
            ),
        )
        del newPath
        del prescale
        del value


# write PathList to json
pathListFname = "pathlist.json"
print("saving pathlist to {}".format(pathListFname))
pathListNew =  [p for p in dir(process) if (("DeepJet" in p) or ("DeepCSV" in p)) and ("HLT_" == p[0:4])]
with open(pathListFname, "w") as pathListFile:
    json.dump(pathListNew, pathListFile)

# from IPython import embed;embed()
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

