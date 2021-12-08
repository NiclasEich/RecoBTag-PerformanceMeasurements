from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromCRIC
import os

config = Configuration()

config.section_("General")
config.General.requestName = 'HLT_noCaloRoiPF_step0_80-120'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step0_DIGI_L1_DIGI2RAW_HLT_noCaloRoiPF.py'
config.JobType.sendPythonFolder	 = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

config.section_("Data")
config.Data.inputDataset = '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 1
config.Data.splitting = 'Automatic'
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/%s/HLT_noCaloRoiPF_step0_3rd_retry/80-120/' % (getUsernameFromCRIC())
config.Data.outputDatasetTag = 'step0_3rd_retry'

config.section_("Site")
config.Site.storageSite = 'T1_DE_KIT_Disk'

config.section_("User")
config.User.voGroup = 'dcms'
