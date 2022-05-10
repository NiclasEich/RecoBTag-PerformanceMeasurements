#!/bin/bash

set -e

if [ $# -lt 1 ]; then
  printf "\n%s\n\n" ">> argument missing - specify path to output directory"
  exit 1
fi

NEVT=-1

if [ $# -eq 1 ]; then
  ODIR=${1}
  # ODIR_cmsRun=$1
else
  ODIR=${1}
  # ODIR_cmsRun=${2}
fi

if [ -d ${ODIR} ]; then
  printf "%s\n" "output directory already exists: ${ODIR}"
  exit 1
fi

declare -A samplesMap

# samplesMap["TTbar_14TeV"]="/TT_TuneCP5_14TeV-powheg-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
samplesMap["QCD_Pt15to7000_pu0to80"]="/QCD_Pt15to7000_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU0to80FEVT_castor_112X_mcRun3_2021_realistic_v16-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt20to30"]="/QCD_Pt-20To30_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt30to50"]="/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/Run3Summer21DRPremix-rndm_120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt50to80"]="/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt80to120"]="/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt120to170"]="/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt170to300"]="/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt300to470"]="/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt470to600"]="/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["QCD_Pt600toInf"]="/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["GluGluToHHTo4B_cHHH1"]="/GluGluToHHTo4B_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["GluGluToHHTo4B_cHHH2p45"]="/GluGluToHHTo4B_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/Run3Winter21DRMiniAOD-FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v4/GEN-SIM-DIGI-RAW"
# samplesMap["GluGluToHHTo4B_cHHH5"]="/GluGluToHHTo4B_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"
# samplesMap["VBFHHTo4B"]="/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW"


recoKeys=(
    HLT_GRun_BatchNorm
    # HLT_Run3TRK_ROICaloROIPF
    # HLT_Run3TRK_noCaloROIPF_Mu_oldJECs
    # HLT_Run3TRK_ROICaloROIPF_Mu
    # HLT_Run3TRK_ROICaloROIPF_Mu_oldJECs
)

# options (JobFlavour and AccountingGroup)
opts=""
if [[ ${HOSTNAME} == lxplus* ]]; then
  opts+="--JobFlavour longlunch"
  # opts+="--JobFlavour workday"
  if [[ ${USER} == sewuchte ]]; then
    opts+=" --AccountingGroup group_u_CMS.CAF.PHYS"
  fi
fi

for recoKey in "${recoKeys[@]}"; do
    # python3 ../runHLTBTagAnalyzer_cfg.py dumpPython=.tmp_${recoKey}_cfg.py defaults=Run3 runOnData=True reco=${recoKey} runPuppiJetVariables=False runCaloJetVariables=True lumis=${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/rates/data/json_323775.txt
    python3 ../runHLTBTagAnalyzer_cfg.py dumpPython=.tmp_${recoKey}_cfg.py defaults=Run3 runOnData=False reco=${recoKey} runPuppiJetVariables=False runCaloJetVariables=True
    for sampleKey in ${!samplesMap[@]}; do
        sampleName=${samplesMap[${sampleKey}]}
        numEvents=${NEVT}
        bdriver -c .tmp_${recoKey}_cfg.py --customize-cfg -m ${numEvents} -n 1000 ${opts} --cpus 1 --mem 1999 --time 03:00:00 \
        -d ${sampleName} -p 0 -o ${ODIR}/${recoKey}/${sampleKey} --export-LD-LIBRARY-PATH -b htc\
        --customise-commands \
       '# output [TFileService]' \
       "if hasattr(process, 'TFileService'):" \
       '  process.TFileService.fileName = opts.output'
    done
    unset sampleKey sampleName numEvents
    rm -f .tmp_${recoKey}_cfg.py
done
unset opts samplesMap NEVT ODIR recoKey

