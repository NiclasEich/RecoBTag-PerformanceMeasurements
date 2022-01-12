common = {
	# 'groups' : ['EventInfo','PV','TagVar','JetInfo','JetSV','JetTrack','CSVTagVar','PFElectron','PFMuon','JetDeepCSV','PatMuon','PatElec','JetDeepFlavour'],
	'groups' : ['EventInfo','PV',
                'PFMuon',"PFElectron",
                'PatMuon','PatElec',
                'TagVar','JetTrack',
                'JetInfo','JetSV','CSVTagVar','JetDeepCSV','JetDeepFlavour','CSVTagTrackVar', 'DeepFlavourFeat',],
	'eras' : ['Run3'],
	'miniAOD' : True,
	'usePuppi' : True,
	'usePuppiForFatJets' : True,
	'usePuppiForBTagging' : True,
	# 'dataGlobalTag' : '122X_dataRun3_HLT_v1', #for data
	'mcGlobalTag' : '122X_mcRun3_2021_realistic_v5', #for MC
	'remakeAllDiscr' : True,
	'maxJetEta' : 2.5,
	'usePrivateJEC' : False,
	# 'jecDBFileMC' : 'PhaseIIFall17_V5b_MC',
	'inputFiles' : ['/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4edf2114-0dc8-4277-95c5-e55989d35c9e.root',],
    # 'JPCalibration' : 'JPcalib_MC81X_v0',
}
