INPUTFILE="/store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/53CA5A7D-9114-2D4C-8E51-C04EE9B68C08.root"
GLOBALTAG='auto:phase2_realistic'

cmsRun runBTagAnalyzer_cfg.py  miniAOD=True  runOnData=False maxEvents=100 groups='EventInfo,PV,TagVar,JetInfo,JetSV,JetTrack,CSVTagVar,PFElectron,PFMuon,JetDeepCSV,PatMuon,PatElec' inputFiles=$INPUTFILE mcGlobalTag=$GLOBALTAG
