import os
from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = True
config.General.transferOutputs = True
config.General.workArea = 'crab'
config.General.requestName = 'hltRates'
config.section_('JobType')
config.JobType.psetName = './hltResults_cfg_WP.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = [os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/PFHC_Run3Winter20_HLT_v01.db',
                             os.environ['CMSSW_BASE']+'/src/JMETriggerAnalysis/NTuplizers/data/JESC_Run3Winter20_V2_MC.db']
config.JobType.outputFiles = ['out.root']
config.JobType.pyCfgParams = ['crab=True', 'output=out.root']
config.JobType.maxMemoryMB = 2500
config.section_('Data')
config.Data.inputDataset = '/EphemeralHLTPhysics1/Run2018D-v1/RAW'
config.Data.outputDatasetTag = 'hltrates'
config.Data.publication = False
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.allowNonValidInputDataset = False
config.Data.outLFNDirBase = '/store/user/mlink/hltrates/'
config.Data.lumiMask = 'lumi_sections_323775.txt'
config.section_('Site')
config.Site.storageSite = 'T1_DE_KIT_Disk'
config.section_('User')
config.User.voGroup = 'dcms'

