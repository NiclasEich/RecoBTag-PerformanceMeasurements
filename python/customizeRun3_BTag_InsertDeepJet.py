import FWCore.ParameterSet.Config as cms

def addDeepJetPathsIntoProcess(process, useNewDeepJetModel = True):
        ####                    DeepJet?
    from CommonTools.RecoAlgos.primaryVertexAssociation_cfi import primaryVertexAssociation
    from RecoBTag.FeatureTools.pfDeepFlavourTagInfos_cfi import pfDeepFlavourTagInfos
    from RecoBTag.ONNXRuntime.pfDeepFlavourJetTags_cfi import pfDeepFlavourJetTags

    process.hltDeepJetDiscriminatorsJetTags = cms.EDProducer(
        "BTagProbabilityToDiscriminator",
        discriminators = cms.VPSet(
            cms.PSet(
                name = cms.string("BvsAll"),
                numerator = cms.VInputTag(
                    cms.InputTag("hltPFDeepFlavourJetTags:probb"),
                    cms.InputTag("hltPFDeepFlavourJetTags:probbb"),
                    cms.InputTag("hltPFDeepFlavourJetTags:problepb"),
                    ),
                denominator=cms.VInputTag(
                    cms.InputTag("hltPFDeepFlavourJetTags:probb"),
                    cms.InputTag("hltPFDeepFlavourJetTags:probbb"),
                    cms.InputTag("hltPFDeepFlavourJetTags:problepb"),
                    cms.InputTag("hltPFDeepFlavourJetTags:probc"),
                    cms.InputTag("hltPFDeepFlavourJetTags:probuds"),
                    cms.InputTag("hltPFDeepFlavourJetTags:probg"),
                    ),
            ),
        )
    )

    process.hltPrimaryVertexAssociation = primaryVertexAssociation.clone(
        jets = cms.InputTag("hltPFJetForBtag"),
        particles = cms.InputTag("hltParticleFlow"),
        vertices = cms.InputTag("hltVerticesPFFilter"),
    )

    process.hltPFDeepFlavourTagInfos = pfDeepFlavourTagInfos.clone(
        candidates = cms.InputTag("hltParticleFlow"),
        jets = cms.InputTag("hltPFJetForBtag"),
        fallback_puppi_weight = cms.bool(True),
        puppi_value_map = cms.InputTag(""),
        secondary_vertices = cms.InputTag("hltDeepInclusiveSecondaryVerticesPF"),
        shallow_tag_infos = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfos"),
        vertex_associator = cms.InputTag("hltPrimaryVertexAssociation","original"),
        vertices = cms.InputTag("hltVerticesPFFilter")
    )
    if useNewDeepJetModel==True:
        process.hltPFDeepFlavourJetTags = pfDeepFlavourJetTags.clone(
            src = cms.InputTag("hltPFDeepFlavourTagInfos"),
            model_path = cms.FileInPath("RecoBTag/Combined/data/DeepFlavour_HLT_12X/model.onnx"),
            output_names = cms.vstring("ID_pred"),
            input_names = cms.vstring(
                "input_0",
                "input_1",
                "input_2",
                "input_3",
                "input_4",
            ),
        )
    else:
        process.hltPFDeepFlavourJetTags = pfDeepFlavourJetTags.clone(
            src = cms.InputTag("hltPFDeepFlavourTagInfos"),
        )

    process.HLTBtagDeepJetSequencePF = cms.Sequence(
        process.hltVerticesPF+
        process.hltVerticesPFSelector+
        process.hltVerticesPFFilter+
        process.hltPFJetForBtagSelector+
        process.hltPFJetForBtag+
        process.hltDeepBLifetimeTagInfosPF+
        process.hltDeepInclusiveVertexFinderPF+
        process.hltDeepInclusiveSecondaryVerticesPF+
        process.hltDeepTrackVertexArbitratorPF+
        process.hltDeepInclusiveMergedVerticesPF+
        process.hltDeepSecondaryVertexTagInfosPF+
        process.hltDeepCombinedSecondaryVertexBJetTagsInfos+
        process.hltPrimaryVertexAssociation+
        process.hltPFDeepFlavourTagInfos+
        process.hltPFDeepFlavourJetTags+
        process.hltDeepJetDiscriminatorsJetTags
    )

    # process.hltPreMCPFBTagDeepJet = process.hltPreMCPFBTagDeepCSV.clone()

    process.hltBTagPFDeepJet4p06Single = process.hltBTagPFDeepCSV4p06Single.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltPFJetForBtag"),
        MaxTag = cms.double(999999.0),
        MinJets = cms.int32(1),
        MinTag = cms.double(0.25),
        TriggerType = cms.int32(86),
        saveTags = cms.bool(True)
    )

    ############################################################################
    ####                    MC_PFBTagDeepJet_v1                   ###
    ############################################################################
    process.hltPreMCPFBTagDeepJet = process.hltPreMCPFBTagDeepCSV.clone()

    process.MC_PFBTagDeepJet_v1 = cms.Path(
        process.HLTBeginSequence+
        process.hltPreMCPFBTagDeepJet+
        process.HLTAK4PFJetsSequence+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet4p06Single+
        process.HLTEndSequence
    )


    ############################################################################
    #### HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v3
    ############################################################################

    process.hltBTagPFDeepJet4p5Triple = process.hltBTagPFDeepCSV4p5Triple.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        MinTag = cms.double(0.24),
    )
    process.hltPrePFHT330PT30QuadPFJet75604540TriplePFBTagDeepJet4p5 = process.hltPrePFHT330PT30QuadPFJet75604540TriplePFBTagDeepCSV4p5.clone()
    process.HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet+
        process.hltPrePFHT330PT30QuadPFJet75604540TriplePFBTagDeepJet4p5+

        process.HLTAK4CaloJetsSequence+
        process.hltQuadCentralJet30+
        process.hltCaloJetsQuad30ForHt+
        process.hltHtMhtCaloJetsQuadC30+
        process.hltCaloQuadJet30HT320+

        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSVp17Double+

        process.HLTAK4PFJetsSequence+
        process.hltPFCentralJetLooseIDQuad30+
        process.hlt1PFCentralJetLooseID75+
        process.hlt2PFCentralJetLooseID60+
        process.hlt3PFCentralJetLooseID45+
        process.hlt4PFCentralJetLooseID40+
        process.hltPFCentralJetLooseIDQuad30forHt+
        process.hltHtMhtPFCentralJetsLooseIDQuadC30+
        process.hltPFCentralJetsLooseIDQuad30HT330+

        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet4p5Triple+

        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v8
    ############################################################################

    process.hltBTagPFDeepJet4p5Double = process.hltBTagPFDeepCSV4p5Double.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltPFJetForBtag"),
    )
    process.hltPrePFHT400FivePFJet100100603030DoublePFBTagDeepJet4p5 = process.hltPrePFHT400FivePFJet100100603030DoublePFBTagDeepCSV4p5.clone()
    process.HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sHTT280to500erIorHTT250to340erQuadJetTripleJet+
        process.hltPrePFHT400FivePFJet100100603030DoublePFBTagDeepJet4p5+
        process.HLTAK4CaloJetsSequence+
        process.hltCaloJetFilterFiveC25+
        process.hltCaloJetsFive25ForHt+
        process.hltHtMhtCaloJetsFiveC25+
        process.hltCaloFiveJet25HT300+

        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV10p01Single+
        process.HLTAK4PFJetsSequence+

        process.hltPFJetFilterTwo100er3p0+
        process.hltPFJetFilterThree60er3p0+
        process.hltPFJetFilterFive30er3p0+
        process.hltPFJetsFive30ForHt+
        process.hltHtMhtPFJetsFive30er3p0+
        process.hltPFFiveJet30HT400+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet4p5Double+

        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v
    ############################################################################

    process.hltPrePFHT400FivePFJet120120603030DoublePFBTagDeepJet4p5 = process.hltPrePFHT400FivePFJet120120603030DoublePFBTagDeepCSV4p5.clone()
    process.HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sHTT280to500erIorHTT250to340erQuadJetTripleJet+
        process.hltPrePFHT400FivePFJet120120603030DoublePFBTagDeepJet4p5+
        process.HLTAK4CaloJetsSequence+
        process.hltCaloJetFilterFiveC25+
        process.hltCaloJetsFive25ForHt+
        process.hltHtMhtCaloJetsFiveC25+
        process.hltCaloFiveJet25HT300+

        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV10p01Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFJetFilterTwo120er3p0+
        process.hltPFJetFilterThree60er3p0+
        process.hltPFJetFilterFive30er3p0+
        process.hltPFJetsFive30ForHt+
        process.hltHtMhtPFJetsFive30er3p0+
        process.hltPFFiveJet30HT400+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet4p5Double+

        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v
    ############################################################################

    process.hltBTagPFDeepJet2p94Double = process.hltBTagPFDeepCSV2p94Double.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltPFJetForBtag"),
    )
    process.hltPrePFHT400SixPFJet32DoublePFBTagDeepJet2p94 = process.hltPrePFHT400SixPFJet32DoublePFBTagDeepCSV2p94.clone()
    process.HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sHTT280to500erIorHTT250to340erQuadJet+
        process.hltPrePFHT400SixPFJet32DoublePFBTagDeepJet2p94+
        process.HLTAK4CaloJetsSequence+
        process.hltCaloJetFilterSixC25+
        process.hltCaloJetsSix25ForHt+
        process.hltHtMhtCaloJetsSixC25+
        process.hltCaloSixJet25HT300+

        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV10p01Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFJetFilterSix30er2p5+
        process.hltPFJetFilterSix32er2p5+
        process.hltPFJetsSix30ForHt+
        process.hltHtMhtPFJetsSix30er2p5+
        process.hltPFSixJet30HT400+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet2p94Double+

        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v
    ############################################################################

    process.hltBTagPFDeepJet1p59Single = process.hltBTagPFDeepCSV1p59Single.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltPFJetForBtag"),
    )
    process.hltPrePFHT450SixPFJet36PFBTagDeepJet1p59 = process.hltPrePFHT450SixPFJet36PFBTagDeepCSV1p59.clone()
    process.HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v7 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sHTT280to500erIorHTT250to340erQuadJet+
        process.hltPrePFHT450SixPFJet36PFBTagDeepJet1p59+
        process.HLTAK4CaloJetsSequence+
        process.hltCaloJetFilterSixC30+
        process.hltCaloJetsSix30ForHt+
        process.hltHtMhtCaloJetsSixC30+
        process.hltCaloSixJet30HT350+

        process.HLTAK4PFJetsSequence+
        process.hltPFJetFilterSix30er2p5+
        process.hltPFJetFilterSix36er2p5+
        process.hltPFJetsSix30ForHt+
        process.hltHtMhtPFJetsSix30er2p5+
        process.hltPFSixJet30HT450+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet1p59Single+

        process.HLTEndSequence
    )
    ############################################################################
    #### HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v
    ############################################################################

    process.hltBTagPFDeepJet7p68Double6Jets = process.hltBTagPFDeepCSV7p68Double6Jets.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltSelector6PFJets"),
    )

    process.hltBTagPFDeepJet1p28Single6Jets = process.hltBTagPFDeepCSV1p28Single6Jets.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltSelector6PFJets"),
    )

    process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5 = process.hltVBFPFJetCSVSortedMqq200Detaqq1p5.clone(
        inputJetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        inputJets = cms.InputTag("hltAK4PFJetsLooseIDCorrected"),
    )
    process.hltPreQuadPFJet103887515DoublePFBTagDeepJet1p37p7VBF1 = process.hltPreQuadPFJet103887515DoublePFBTagDeepCSV1p37p7VBF1.clone()
    process.HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJetVBFIorHTTIorSingleJet+
        process.hltPreQuadPFJet103887515DoublePFBTagDeepJet1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID75+
        process.hltPFDoubleJetLooseID88+
        process.hltPFSingleJetLooseID103+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet7p68Double6Jets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5+

        process.HLTEndSequence
    )


    ############################################################################
    #### HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v
    ############################################################################

    process.hltVBFPFJetDeepJetSortedMqq460Detaqq3p5 = process.hltVBFPFJetCSVSortedMqq460Detaqq3p5.clone(
        inputJetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        inputJets = cms.InputTag("hltAK4PFJetsLooseIDCorrected"),
    )
    process.hltPreQuadPFJet103887515PFBTagDeepJet1p3VBF2 = process.hltPreQuadPFJet103887515PFBTagDeepCSV1p3VBF2.clone()
    process.HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJetVBFIorHTTIorSingleJet+
        process.hltPreQuadPFJet103887515PFBTagDeepJet1p3VBF2+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID75+
        process.hltPFDoubleJetLooseID88+
        process.hltPFSingleJetLooseID103+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq460Detaqq3p5+
        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v
    ############################################################################

    process.hltPreQuadPFJet105887615DoublePFBTagDeepJet1p37p7VBF1 = process.hltPreQuadPFJet105887615DoublePFBTagDeepCSV1p37p7VBF1.clone()
    process.HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet1008572VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet105887615DoublePFBTagDeepJet1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID76+
        process.hltPFDoubleJetLooseID88+
        process.hltPFSingleJetLooseID105+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet7p68Double6Jets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5+
        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v
    ############################################################################

    process.hltPreQuadPFJet105887615PFBTagDeepJet1p3VBF2 = process.hltPreQuadPFJet105887615PFBTagDeepCSV1p3VBF2.clone()
    process.HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet1008572VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet105887615PFBTagDeepJet1p3VBF2+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID76+
        process.hltPFDoubleJetLooseID88+
        process.hltPFSingleJetLooseID105+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq460Detaqq3p5+
        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v
    ############################################################################

    process.hltPreQuadPFJet111908015DoublePFBTagDeepJet1p37p7VBF1 = process.hltPreQuadPFJet111908015DoublePFBTagDeepCSV1p37p7VBF1.clone()
    process.HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet1058576VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet111908015DoublePFBTagDeepJet1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID80+
        process.hltPFDoubleJetLooseID90+
        process.hltPFSingleJetLooseID111+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet7p68Double6Jets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5+

        process.HLTEndSequence
    )


    ############################################################################
    #### HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v
    ############################################################################

    process.hltPreQuadPFJet111908015PFBTagDeepJet1p3VBF2 = process.hltPreQuadPFJet111908015PFBTagDeepCSV1p3VBF2.clone()
    process.HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet1058576VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet111908015PFBTagDeepJet1p3VBF2+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID80+
        process.hltPFDoubleJetLooseID90+
        process.hltPFSingleJetLooseID111+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq460Detaqq3p5+

        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v
    ############################################################################

    process.hltPreQuadPFJet98837115DoublePFBTagDeepJet1p37p7VBF1 = process.hltPreQuadPFJet98837115DoublePFBTagDeepCSV1p37p7VBF1.clone()
    process.HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet927664VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet98837115DoublePFBTagDeepJet1p37p7VBF1+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID71+
        process.hltPFDoubleJetLooseID83+
        process.hltPFSingleJetLooseID98+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet7p68Double6Jets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq200Detaqq1p5+
        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v
    ############################################################################

    process.hltPreQuadPFJet98837115PFBTagDeepJet1p3VBF2 = process.hltPreQuadPFJet98837115PFBTagDeepCSV1p3VBF2.clone()
    process.HLT_QuadPFJet98_83_71_15_PFBTagDeepJet_1p3_VBF2_v8 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sTripleJet927664VBFIorHTTIorDoubleJetCIorSingleJet+
        process.hltPreQuadPFJet98837115PFBTagDeepJet1p3VBF2+
        process.HLTAK4CaloJetsSequence+
        process.hltQuadJet15+
        process.hltTripleJet50+
        process.hltDoubleJet65+
        process.hltSingleJet80+
        process.hltVBFCaloJetEtaSortedMqq150Deta1p5+

        process.HLTFastPrimaryVertexSequence+
        process.HLTBtagDeepCSVSequenceL3+
        process.hltBTagCaloDeepCSV1p56Single+

        process.HLTAK4PFJetsSequence+
        process.hltPFQuadJetLooseID15+
        process.hltPFTripleJetLooseID71+
        process.hltPFDoubleJetLooseID83+
        process.hltPFSingleJetLooseID98+
        process.HLTBtagDeepJetSequencePF+
        process.hltSelector6PFJets+
        process.hltBTagPFDeepJet1p28Single6Jets+
        process.hltVBFPFJetDeepJetSortedMqq460Detaqq3p5+
        process.HLTEndSequence
    )

    ############################################################################
    #### HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
    ############################################################################

    process.hltPreMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZPFDiJet30PFBtagDeepJet1p5 = process.hltPreMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZPFDiJet30PFBtagDeepCSV1p5.clone()
    process.hltBTagPFDeepJet1p5Single = process.hltBTagPFDeepCSV1p5Single.clone(
        JetTags = cms.InputTag("hltDeepJetDiscriminatorsJetTags","BvsAll"),
        Jets = cms.InputTag("hltPFJetForBtag"),
    )
    process.HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v1 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23+
        process.hltPreMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZPFDiJet30PFBtagDeepJet1p5+

        process.HLTMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegSequence+
        process.HLTMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLElectronlegSequence+
        process.hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter+

        process.HLTAK4PFJetsSequence+
        process.hltPFJetFilterTwoC30+
        process.HLTBtagDeepJetSequencePF+
        process.hltBTagPFDeepJet1p5Single+
        process.HLTEndSequence
    )

    if hasattr(process, 'PrescaleService'):
        process.PrescaleService.prescaleTable.insert(-1,
            cms.PSet(
                pathName = cms.string('MC_PFBTagDeepJet_v1'),
                prescales = cms.vuint32(
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    1, 1, 1, 1, 1,
                    1, 0, 0, 0
                )
            ),
        )

    if hasattr(process, "schedule"):
        process.schedule.extend([
            process.MC_PFBTagDeepJet_v1,
            process.HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3,
            process.HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v8,
            process.HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v8,
            process.HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v8,
            process.HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v7,
            process.HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet98_83_71_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v1,
        ])
    elif hasattr(process, "HLTSchedule"):
        process.HLTSchedule.extend([
            process.MC_PFBTagDeepJet_v1,
            process.HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3,
            process.HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v8,
            process.HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v8,
            process.HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v8,
            process.HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v7,
            process.HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8,
            process.HLT_QuadPFJet98_83_71_15_PFBTagDeepJet_1p3_VBF2_v8,
            process.HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v1,
        ])

    return process
