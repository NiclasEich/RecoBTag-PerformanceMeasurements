#!/bin/bash

set -e

if [ $# -ne 1 ]; then
  printf "\n%s\n\n" ">> argument missing - specify path to output directory"
  exit 1
fi

NEVT=-1

version="run10"
basedir="/nfs/dust/cms/user/neich/BTV/cmssw_tests/working_points_02/CMSSW_12_3_0_pre6/src/RecoBTag/PerformanceMeasurements/test/rates"

ODIR=${1}

if [ -d ${ODIR} ]; then
  printf "%s\n" "output directory already exists: ${ODIR}"
  exit 1
fi

declare -A samplesMap
samplesMap["Run2018D_EphemeralHLTPhysics1_RAW_run323775_ls38to81and84to151"]="${CMSSW_BASE}"/src/RecoBTag/PerformanceMeasurements/test/rates/data/working_points_data.json


recoKeys=(
  HLT_GRun
  # HLT_GRun_oldJECs
  # HLT_Run3TRK
  #HLT_Run3TRK_noCaloROIPF_Mu
  #HLT_Run3TRK_noCaloROIPF_Mu_oldJECs
)

for recoKey in "${recoKeys[@]}"; do
  cmsRun "${CMSSW_BASE}"/src/RecoBTag/PerformanceMeasurements/test/rates/hltResults_cfg_WP.py \
    dumpPython=${basedir}/wp_out/${version}_cfg.py numThreads=1 maxEvents=1000 output=${basedir}/wp_out/${version}.root lumis=lumi_sections_323775.txt

  for sampleKey in ${!samplesMap[@]}; do
      echo ${sampleKey}
    sampleName=${samplesMap[${sampleKey}]}
    echo ${sampleName}

    # bdriver -c .tmp_${recoKey}_cfg.py --customize-cfg -m ${NEVT} -n 500 --cpus 1 --mem 2G --time 02:00:00 \
    # bdriver -c wp_out/${version}_cfg.py --customize-c wp_out/${version}-cfg -m ${NEVT} -n 500 --export-LD-LIBRARY-PATH -b htc \
    bdriver -c ${basedir}/wp_out/${version}_cfg.py -m ${NEVT} -n 500 --export-LD-LIBRARY-PATH -b htc \
      -d ${sampleName} -p 0 -o ${ODIR}/${recoKey}/${sampleKey} --cpus 1 --mem 1999 --time 03:00:00\
      --customise-commands \
       '# output' \
       "if hasattr(process, 'hltOutput'):" \
       '  process.hltOutput.fileName = opts.output'
  done

#   rm -f .tmp_${recoKey}_cfg.py
done
