from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromCRIC
import os

config = Configuration()

config.section_("General")
config.General.requestName = 'HLT_noCaloRoiPF_step1_80-120'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_VALIDATION_DQM_noCaloRoiPF.py'
config.JobType.sendPythonFolder	 = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

config.section_("Data")
config.Data.inputDataset = '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_14TeV-pythia8/mullerd-step0_3rd_retry-1b6b10f4d737e49cdc03478bd3b6a0e0/USER'
config.Data.inputDBS = 'phys03'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 1
config.Data.splitting = 'Automatic'
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/%s/HLT_noCaloRoiPF_step1_retry/80-120/' % (getUsernameFromCRIC())
config.Data.outputDatasetTag = 'step1_retry'

config.section_("Site")
config.Site.storageSite = 'T1_DE_KIT_Disk'

config.section_("User")
config.User.voGroup = 'dcms'
