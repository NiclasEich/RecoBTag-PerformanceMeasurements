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

opts.register('crab', True,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'running with')

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

    PFHCpath = os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db'
    JESCpath = os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db'
    if opts.crab:
        PFHCpath = './PFHC_Run3Winter20_HLT_v01.db'
        JESCpath = './JESC_Run3Winter20_V2_MC.db'

    process.pfhcESSource = cms.ESSource('PoolDBESSource',
        _CondDB.clone(connect = 'sqlite_file:'+PFHCpath),
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
    _CondDB.clone(connect = 'sqlite_file:'+JESCpath),
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
    process.source.fileNames = ['/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/0244D183-F28D-2741-9DBF-1638BEDC734E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/08D3F006-5E29-7945-B32A-CEF9CA8CA51E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/0E3CB569-5250-5C4A-848A-1BDA2E32700B.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/102C594B-84FE-7540-AD4D-8BE75F1C8E9D.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/2EF1B5B0-1C31-1C4E-9876-5DC82E000465.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/311502E8-3FD3-204F-AC98-6F0A22F86812.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/3552E1AA-595B-FD48-B1B1-4977E2C10BA7.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/36EB9880-284A-9848-8AD2-5E065353EFB7.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/432749D4-9AEF-5845-B557-302884DC2B78.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/50A28BB4-3ACA-464F-A5E6-60F3D0062547.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/534721E2-EEBE-1F48-84AE-364F55A8CE1A.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/5AA70A8A-6807-0548-9E2E-99726A80C8B4.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/5FB1F56D-A583-3148-B634-06E37459CD87.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/6514D401-ECA9-8F48-B3C1-0ABB3AB99838.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/65EA98C3-88C1-5A43-8152-824F3169174E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/6CB9E9DA-BEFE-3A4C-903A-C70BAC1542D6.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/720B4B82-1883-F84D-9016-6050BA9F7BB3.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7AAC7654-1C3C-1A40-BD82-7F92B899A048.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7F3D4F09-8335-7047-9420-0F8438E0C606.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7F8818CF-AB9A-3847-B3B1-31175BC67EEA.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/839E1796-3459-6443-93CF-5B6DDED6ADD2.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/8F75E00C-8209-1A48-AEE8-F37A59D46FFB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/9B8F48E7-8EB9-CA4E-B545-DDF63D28E4DB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/A27DFA33-8FCB-BE42-A2D2-1A396EEE2B6E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/AB95AEB0-C511-114C-B54C-9C0A9B78AF1E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/AC589D97-A8ED-2B4C-B961-5595C88A8CEF.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/ADEDA3A0-2806-9840-8977-941CDDDEF4CC.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B14F28B7-490B-DA4E-8EA4-AF1B0C07756C.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B1D33CE9-6EDD-BF4C-9FF5-88956C5F7AA5.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B26AAAB6-F701-0C44-860E-CAB8EDC85876.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B71884AE-9951-FF47-915E-2C8C38421AF2.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B7DBE80D-BF96-6744-BF0A-D7AE6BBE7077.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/BCAD5D59-5C76-9E47-8216-573FA32A7C6F.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C707212D-9264-0F43-9937-A0053CBFEDDE.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C8A17517-E49C-4149-8301-A9523DCF6094.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C9B068C6-7C5E-5F4C-8556-33D138EB30CB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/CA095F57-5636-6A4F-BD4B-A6C35C0BBD03.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D20C7DA2-996F-B54E-AAE0-DA110878E4BA.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D5D2CF9C-2557-4243-B42E-4345100839DA.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/DA29E8B1-6A6A-214D-9405-4CD055D39303.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/DFBCDC7A-4389-9246-96EC-779943404AD1.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/E85A6840-68D8-E141-AAB8-BD6A05F7FE7F.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/F2293A8A-1B29-524B-895C-EFC12F58FF32.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/F83FFC16-0D3B-6E44-B744-29036A93DFCB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/FBF117EE-5699-F147-BBFC-07815D5A2582.root']

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

