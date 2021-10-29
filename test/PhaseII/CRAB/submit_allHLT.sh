#!/bin/bash

echo "!!!! WARNING: Submitting for MC!!!"
# ==========================cutsv2===================


python ../submit_allHLT.py \
  ../runHLTBTagAnalyzer_PhaseII_cfg.py \
  -f tosubmit.txt \
  -s T2_DE_DESY \
  -o /store/user/sewuchte/BTagServiceWork/PhaseII/Online/ \
  -p reco=HLT_TRKv06p1_TICL BTVreco=cutsV2 globalTag=111X_mcRun4_realistic_T15_v4\
  -v crab_projects_FebruaryTDR_TrackingV6p1_TICL_cutsV2_v1 \
  -t 2750 \
  # -m 4500
