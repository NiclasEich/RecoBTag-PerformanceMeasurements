common = {
	'groups' : ['EventInfo','PV',
                # 'PFMuon',"PFElectron",
                "TagVar",'JetTrack',
                'JetInfo','JetSV','CSVTagVar','JetDeepCSV','JetDeepFlavour','CSVTagTrackVar', 'DeepFlavourFeat',
                # 'PuppiJetTagVar','PuppiJetTrack',
                # 'PuppiJetInfo','PuppiJetSV','PuppiJetCSVTagVar','PuppiJetDeepCSV','PuppiJetDeepFlavour','PuppiJetCSVTagTrackVar','PuppiJetDeepFlavourFeat',
                # 'PuppiJetTrack','PuppiJetTagVar',
                'CaloJetInfo','CaloJetSV','CaloJetCSVTagVar','CaloJetDeepCSV','CaloJetCSVTagTrackVar',
                'CaloJetTrack','CaloJetTagVar',
                ],
	'eras' : ['Run3'],
    'runCaloJetVariables' : True,
    'runPuppiJetVariables' : False,
	'globalTag' : '122X_mcRun3_2021_realistic_v5', # mc
	# 'globalTag' : '122X_dataRun3_HLT_v1', # data
	'maxJetEta' : 2.5,
	'usePrivateJEC' : False,
	# 'jecDBFileMC' : 'PhaseIIFall17_V5b_MC',
	'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/120005/57b8b842-4736-4f6f-9627-38d4da5dc87d.root',],
    # 'JPCalibration' : 'JPcalib_MC81X_v0',
}
