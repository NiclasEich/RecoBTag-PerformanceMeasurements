import FWCore.ParameterSet.Config as cms

def replaceBTagMuPathsInProcess(process):
    # delete the old ones
    if hasattr(process, "HLT_BTagMu_AK4DiJet20_Mu5_v13"):
         del process.HLT_BTagMu_AK4DiJet20_Mu5_v13
    if hasattr(process, "HLT_BTagMu_AK4DiJet40_Mu5_v13"):
         del process.HLT_BTagMu_AK4DiJet40_Mu5_v13
    if hasattr(process, "HLT_BTagMu_AK4DiJet70_Mu5_v13"):
         del process.HLT_BTagMu_AK4DiJet70_Mu5_v13
    if hasattr(process, "HLT_BTagMu_AK4DiJet110_Mu5_v13"):
         del process.HLT_BTagMu_AK4DiJet110_Mu5_v13
    if hasattr(process, "HLT_BTagMu_AK4DiJet170_Mu5_v12"):
         del process.HLT_BTagMu_AK4DiJet170_Mu5_v12
    if hasattr(process, "HLT_BTagMu_AK4Jet300_Mu5_v12"):
         del process.HLT_BTagMu_AK4Jet300_Mu5_v12
    if hasattr(process, "HLT_BTagMu_AK8DiJet170_Mu5_v9"):
         del process.HLT_BTagMu_AK8DiJet170_Mu5_v9
    if hasattr(process, "HLT_BTagMu_AK8Jet170_DoubleMu5_v2"):
         del process.HLT_BTagMu_AK8Jet170_DoubleMu5_v2
    if hasattr(process, "HLT_BTagMu_AK8Jet300_Mu5_v12"):
         del process.HLT_BTagMu_AK8Jet300_Mu5_v12

    # Rename NoAlgo BTagMu branches and delete NoAlgo paths afterwards


    ############################################################################
    #### HLT_BTagMu_AK4DiJet20_Mu5_v13
    ############################################################################
    process.hltPreBTagMuAK4DiJet20Mu5 = process.hltPreBTagMuAK4DiJet20Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4DiJet20Mu5noalgo"):
        del process.hltPreBTagMuAK4DiJet20Mu5noalgo

    process.HLT_BTagMu_AK4DiJet20_Mu5_v13 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC16dRMax0p4+
        process.hltPreBTagMuAK4DiJet20Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBDiJet20L1FastJetCentral+
        process.HLTBTagMuDiJet20L1FastJetSequenceL25+
        process.hltBSoftMuonDiJet20L1FastJetL25FilterByDR+
        process.HLTBTagMuDiJet20L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonDiJet20L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v13"):
        del process.HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v13

    ############################################################################
    #### HLT_BTagMu_AK4DiJet40_Mu5_v13
    ############################################################################
    process.hltPreBTagMuAK4DiJet40Mu5 = process.hltPreBTagMuAK4DiJet40Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4DiJet40Mu5noalgo"):
        del process.hltPreBTagMuAK4DiJet40Mu5noalgo

    process.HLT_BTagMu_AK4DiJet40_Mu5_v13 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC35dRMax0p4+
        process.hltPreBTagMuAK4DiJet40Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBDiJet40L1FastJetCentral+
        process.HLTBTagMuDiJet40L1FastJetSequenceL25+
        process.hltBSoftMuonDiJet40L1FastJetL25FilterByDR+
        process.HLTBTagMuDiJet40L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonDiJet40L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v13"):
        del process.HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v13

    ############################################################################
    #### HLT_BTagMu_AK4DiJet70_Mu5_v13
    ############################################################################
    process.hltPreBTagMuAK4DiJet70Mu5 = process.hltPreBTagMuAK4DiJet70Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4DiJet70Mu5noalgo"):
        del process.hltPreBTagMuAK4DiJet70Mu5noalgo

    process.HLT_BTagMu_AK4DiJet70_Mu5_v13 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC60dRMax0p4+
        process.hltPreBTagMuAK4DiJet70Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBDiJet70L1FastJetCentral+
        process.HLTBTagMuDiJet70L1FastJetSequenceL25+
        process.hltBSoftMuonDiJet70L1FastJetL25FilterByDR+
        process.HLTBTagMuDiJet70L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonDiJet70L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v13"):
        del process.HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v13

    ############################################################################
    #### HLT_BTagMu_AK4DiJet110_Mu5_v13
    ############################################################################
    process.hltPreBTagMuAK4DiJet110Mu5 = process.hltPreBTagMuAK4DiJet110Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4DiJet110Mu5noalgo"):
        del process.hltPreBTagMuAK4DiJet110Mu5noalgo

    process.HLT_BTagMu_AK4DiJet110_Mu5_v13 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC80dRMax0p4+
        process.hltPreBTagMuAK4DiJet110Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBDiJet110L1FastJetCentral+
        process.HLTBTagMuDiJet110L1FastJetSequenceL25+
        process.hltBSoftMuonDiJet110L1FastJetL25FilterByDR+
        process.HLTBTagMuDiJet110L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonDiJet110L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v13"):
        del process.HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v13

    ############################################################################
    #### HLT_BTagMu_AK4DiJet170_Mu5_v12
    ############################################################################
    process.hltPreBTagMuAK4DiJet170Mu5 = process.hltPreBTagMuAK4DiJet170Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4DiJet170Mu5noalgo"):
        del process.hltPreBTagMuAK4DiJet170Mu5noalgo

    process.HLT_BTagMu_AK4DiJet170_Mu5_v12 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC120dRMax0p4+
        process.hltPreBTagMuAK4DiJet170Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBDiJet200L1FastJetCentral+
        process.HLTBTagMuDiJet200L1FastJetSequenceL25+
        process.hltBSoftMuonDiJet200L1FastJetL25FilterByDR+
        process.HLTBTagMuDiJet200L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonDiJet200L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v12"):
        del process.HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v12

    ############################################################################
    #### HLT_BTagMu_AK4Jet300_Mu5_v12
    ############################################################################
    process.hltPreBTagMuAK4Jet300Mu5 = process.hltPreBTagMuAK4Jet300Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK4Jet300Mu5noalgo"):
        del process.hltPreBTagMuAK4Jet300Mu5noalgo

    process.HLT_BTagMu_AK4Jet300_Mu5_v12 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sSingleJet200+
        process.hltPreBTagMuAK4Jet300Mu5+
        process.HLTAK4CaloJetsSequence+
        process.hltBJet300L1FastJetCentral+
        process.HLTBTagMuJet300L1FastJetSequenceL25+
        process.hltBSoftMuonJet300L1FastJetL25FilterByDR+
        process.HLTBTagMuJet300L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonJet300L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK4Jet300_Mu5_noalgo_v12"):
        del process.HLT_BTagMu_AK4Jet300_Mu5_noalgo_v12

    ############################################################################
    #### HLT_BTagMu_AK8DiJet170_Mu5_v9
    ############################################################################
    process.hltPreBTagMuAK8DiJet170Mu5 = process.hltPreBTagMuAK8DiJet170Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK8DiJet170Mu5noalgo"):
        del process.hltPreBTagMuAK8DiJet170Mu5noalgo

    process.HLT_BTagMu_AK8DiJet170_Mu5_v9 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu3JetC120dRMax0p8+
        process.hltPreBTagMuAK8DiJet170Mu5+
        process.HLTAK8CaloJetsSequence+
        process.hltBAK8DiJet170L1FastJetCentral+
        process.HLTBTagMuAK8DiJet170L1FastJetSequenceL25+
        process.hltBSoftMuonAK8DiJet170L1FastJetL25FilterByDR+
        process.HLTBTagMuAK8DiJet170L1FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonAK8DiJet170L1FastJetMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v9"):
        del process.HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v9

    ############################################################################
    #### HLT_BTagMu_AK8Jet170_DoubleMu5_v2
    ############################################################################
    process.hltPreBTagMuAK8Jet170DoubleMu5 = process.hltPreBTagMuAK8Jet170DoubleMu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK8Jet170DoubleMu5noalgo"):
        del process.hltPreBTagMuAK8Jet170DoubleMu5noalgo

    process.HLT_BTagMu_AK8Jet170_DoubleMu5_v2 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sDoubleMu0Jet90er2p5dRMax0p8dRMu1p6+
        process.hltPreBTagMuAK8Jet170DoubleMu5+
        process.hltDoubleMuon0L1Filtered0+
        process.HLTAK8CaloJetsSequence+
        process.hltBAK8Jet170L1FastJetCentral+
        process.HLTBTagMuAK8Jet170L1FastJetDoubleMuSequenceL25+
        process.hltBSoftMuonAK8Jet170L1FastJetL25FilterByDR+
        process.HLTBTagMuAK8Jet170L1FastJetDoubleMu5SelSequenceL3noalgo+
        process.hltBSoftMuonAK8Jet170L1FastJetDoubleMu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v2"):
        del process.HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v2

    ############################################################################
    #### HLT_BTagMu_AK8Jet300_Mu5_v12
    ############################################################################
    process.hltPreBTagMuAK8Jet300Mu5 = process.hltPreBTagMuAK8Jet300Mu5noalgo.clone()

    if hasattr(process, "hltPreBTagMuAK8Jet300Mu5noalgo"):
        del process.hltPreBTagMuAK8Jet300Mu5noalgo

    process.HLT_BTagMu_AK8Jet300_Mu5_v12 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sSingleJet200+
        process.hltPreBTagMuAK8Jet300Mu5+
        process.HLTAK8CaloJetsSequence+
        process.hltBJet300L1AK8FastJetCentral+
        process.HLTBTagMuJet300L1AK8FastJetSequenceL25+
        process.hltBSoftMuonJet300L1FastJetAK8L25FilterByDR+
        process.HLTBTagMuJet300L1AK8FastJetMu5SelSequenceL3noalgo+
        process.hltBSoftMuonJet300L1FastJetAK8Mu5L3FilterByDRnoalgo+
        process.HLTEndSequence
    )
    if hasattr(process, "HLT_BTagMu_AK8Jet300_Mu5_noalgo_v12"):
        del process.HLT_BTagMu_AK8Jet300_Mu5_noalgo_v12


    if hasattr(process, "schedule"):
        process.schedule.extend([
            process.HLT_BTagMu_AK4DiJet20_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet40_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet70_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet110_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet170_Mu5_v12,
            process.HLT_BTagMu_AK4Jet300_Mu5_v12,
            process.HLT_BTagMu_AK8DiJet170_Mu5_v9,
            process.HLT_BTagMu_AK8Jet170_DoubleMu5_v2,
            process.HLT_BTagMu_AK8Jet300_Mu5_v12,

        ])
    elif hasattr(process, "HLTSchedule"):
        process.HLTSchedule.extend([
            process.HLT_BTagMu_AK4DiJet20_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet40_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet70_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet110_Mu5_v13,
            process.HLT_BTagMu_AK4DiJet170_Mu5_v12,
            process.HLT_BTagMu_AK4Jet300_Mu5_v12,
            process.HLT_BTagMu_AK8DiJet170_Mu5_v9,
            process.HLT_BTagMu_AK8Jet170_DoubleMu5_v2,
            process.HLT_BTagMu_AK8Jet300_Mu5_v12,

        ])

    # fix prescales, remove NoAlgo ones, old ones have been clones
    if hasattr(process, 'PrescaleService'):
        paths_to_delete=[
            "HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v13",
            "HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v13",
            "HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v13",
            "HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v13",
            "HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v12",
            "HLT_BTagMu_AK4Jet300_Mu5_noalgo_v12",
            "HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v9",
            "HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v2",
            "HLT_BTagMu_AK8Jet300_Mu5_noalgo_v12",
        ]
        psets_to_delete = []
        for path in paths_to_delete:
            # print ("Fix prescale for",path)
            for pset in process.PrescaleService.prescaleTable:
                if pset.pathName.value() == path:
                    psets_to_delete.append(pset)
        for p in psets_to_delete:
            process.PrescaleService.prescaleTable.remove(p)

    return process
