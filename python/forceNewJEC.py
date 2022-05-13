import FWCore.ParameterSet.Config as cms

psets = [
  cms.PSet(
    record = cms.string('PFCalibrationRcd'),
    tag = cms.string('PFCalibration_120X_mcRun3_2021_hlt'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('HLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK4CaloHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4CaloHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK4PFClusterHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFClusterHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK4PFHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK4PFchsHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFchsHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK4PFPuppiHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK4PFPuppiHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK8CaloHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8CaloHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK8PFClusterHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFClusterHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK8PFHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK8PFchsHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFchsHLT'),
  ),
  cms.PSet(
    record = cms.string('JetCorrectionsRecord'),
    tag = cms.string('JetCorrectorParametersCollection_Run3Winter21_V2_MC_AK8PFPuppiHLT'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    label = cms.untracked.string('AK8PFPuppiHLT'),
  )
]

def forceNewJEC(process):
    if not hasattr(process, "GlobalTag"):
        Exception("The process has not GlobalTag. Please contact silvio.donato@cern.ch")
    gt = getattr(process, "GlobalTag")
    if not hasattr(gt, "toGet"):
        gt.toGet = cms.VPSet()
    for pset in psets:
        gt.toGet.append(pset)
    return process
