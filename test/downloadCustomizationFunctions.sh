curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_GlobalCalo_GlobalPF.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_ROICalo_GlobalPF.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_ROICalo_ROIPF.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_noCalo_ROIPF.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_BTagMu.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/python/customizeRun3_BTag_DisplacedJets.py
curl -O https://raw.githubusercontent.com/SWuchterl/RecoBTag-PerformanceMeasurements/Run3_ForJIRA_12_3_0/test/runHLTPaths_cfg.py
curl -O https://raw.githubusercontent.com/mmasciov/cmssw/defaultRun3Tracking_forJIRA/HLTrigger/Configuration/python/customizeHLTforRun3Tracking.py
curl -O https://raw.githubusercontent.com/annamasce/TauTriggerTools/triggerRnD_counter/HLTProducers/python/applyL2TauTag.py
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/customizeMuonHLTForRun3.py
curl -O https://raw.githubusercontent.com/khaosmos93/MuonHLTForRun3/master/mvaScale.py

sed -i 's/import HLTrigger.Configuration.MuonHLTForRun3.mvaScale/from . import mvaScale/g' customizeMuonHLTForRun3.py

cat runHLTPaths_cfg.py | grep "def fixMenu" -A100  | grep "def prescale_path(path,ps_service)" -B100  | grep -v prescale_path > tmp.py
mv tmp.py runHLTPaths_cfg.py
