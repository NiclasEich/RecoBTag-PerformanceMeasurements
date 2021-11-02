import FWCore.ParameterSet.Config as cms

def customize_hltPhase2_BTV_paths(reco="HLT_TRKv06p1_TICL",  BTVreco="cutsV2", name='HLTBTVPaths'):

    opt_skimTracks = False

    opt_reco = reco
    if opt_reco.endswith('_skimmedTracks'):
       opt_reco = opt_reco[:-len('_skimmedTracks')]
       opt_skimTracks = True

    if   opt_reco == 'HLT_TRKv00':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv00_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv00_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv02':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv02_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv02_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv06':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv06_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv06p1':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv06p1_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p1_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv06p3':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p3_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv06p3_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv06p3_TICL_cfg import cms, process
    elif opt_reco == 'HLT_TRKv07p2':      from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_cfg      import cms, process
    elif opt_reco == 'HLT_TRKv07p2_TICL': from JMETriggerAnalysis.Common.configs.hltPhase2_TRKv07p2_TICL_cfg import cms, process
    else:
       logmsg = '\n\n'+' '*2+'Valid arguments for option "reco" are'
       for recoArg in [
         'HLT_TRKv00',
         'HLT_TRKv00_TICL',
         'HLT_TRKv02',
         'HLT_TRKv02_TICL',
         'HLT_TRKv06',
         'HLT_TRKv06_TICL',
         'HLT_TRKv06p1',
         'HLT_TRKv06p1_TICL',
         'HLT_TRKv06p3',
         'HLT_TRKv06p3_TICL',
         'HLT_TRKv07p2',
         'HLT_TRKv07p2_TICL',
       ]:
         logmsg += '\n'+' '*4+recoArg
       raise RuntimeError('invalid argument for option "reco": "'+opt_reco+'"'+logmsg+'\n')


    # skimming of tracks
    if opt_skimTracks:
       from JMETriggerAnalysis.Common.hltPhase2_skimmedTracks import customize_hltPhase2_skimmedTracks
       process = customize_hltPhase2_skimmedTracks(process)


    opt_BTVreco = BTVreco
    if opt_BTVreco == 'default':
          from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV import customize_hltPhase2_BTV
          process = customize_hltPhase2_BTV(process)
    elif opt_BTVreco == 'cutsV1':
          from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cuts import customize_hltPhase2_BTV
          process = customize_hltPhase2_BTV(process)
    elif opt_BTVreco == 'cutsV2':
          from RecoBTag.PerformanceMeasurements.Configs.hltPhase2_BTV_cutsV2 import customize_hltPhase2_BTV
          process = customize_hltPhase2_BTV(process)
    else:
        logmsg = '\n\n'+' '*2+'Valid arguments for option "BTVreco" are'
        for recoArg in [
            'default',
            'cutsV1',
            'cutsV2',
        ]:
            logmsg += '\n'+' '*4+recoArg
        raise RuntimeError('invalid argument for option "BTVreco": "'+opt_BTVreco+'"')


    # modify JME settings
    process.source.inputCommands = cms.untracked.vstring([
      'keep *_*_*_*',
      'drop *_*_*_RECO',

      # L1T
      'keep *_pfTracksFromL1TracksBarrel_*_*',
      'keep *_pfTracksFromL1TracksHGCal_*_*',
      'keep *_l1pfCandidates_*_RECO',
      'keep *_TTTracksFromTrackletEmulation_Level1TTTracks_RECO',
      'keep *_TTTracksFromExtendedTrackletEmulation_Level1TTTracks_RECO',
      'keep *_L1TkPrimaryVertex__RECO',
      'keep *_l1pfCandidates_Puppi_RECO',
      'keep *_ak4PFL1Calo__RECO',
      'keep *_ak4PFL1CaloCorrected__RECO',
      'keep *_ak4PFL1PF__RECO',
      'keep *_ak4PFL1PFCorrected__RECO',
      'keep *_ak4PFL1Puppi__RECO',
      'keep *_ak4PFL1PuppiCorrected__RECO',
      'keep *_l1PFMetCalo__RECO',
      'keep *_l1PFMetPF__RECO',
      'keep *_l1PFMetPuppi__RECO',

      # Offline
      'keep *_fixedGridRhoFastjetAll__RECO',
      'keep *_offlineSlimmedPrimaryVertices__RECO',
      'keep *_packedPFCandidates__RECO',
      'keep *_slimmedMuons__RECO',
      'keep *_slimmedJets__RECO',
      'keep *_slimmedJetsPuppi__RECO',
      'keep *_slimmedJetsAK8*_*_RECO',
      'keep *_slimmedMETs__RECO',
      'keep *_slimmedMETsPuppi__RECO',
    ])

    ################################################################################
    ### filter for QCD muon enriched
    ################################################################################
    # process.muGenFilter = cms.EDFilter("MCSmartSingleParticleFilter",
    #     MaxDecayRadius = cms.untracked.vdouble(2000.0, 2000.0),
    #     MaxDecayZ = cms.untracked.vdouble(4000.0, 4000.0),
    #     MaxEta = cms.untracked.vdouble(4.5, 4.5),
    #     MinDecayZ = cms.untracked.vdouble(-4000.0, -4000.0),
    #     MinEta = cms.untracked.vdouble(-4.5, -4.5),
    #     MinPt = cms.untracked.vdouble(5.0, 5.0),
    #     ParticleID = cms.untracked.vint32(13, -13),
    #     Status = cms.untracked.vint32(1, 1),
    #     moduleLabel = cms.untracked.InputTag("generatorSmeared","","SIM")
    # )
    # process.emEnrichingFilter = cms.EDFilter("EMEnrichingFilter",
    #     filterAlgoPSet = cms.PSet(
    #         caloIsoMax = cms.double(10.0),
    #         clusterThreshold = cms.double(20.0),
    #         genParSource = cms.InputTag("genParticles"),
    #         hOverEMax = cms.double(0.5),
    #         isoConeSize = cms.double(0.2),
    #         isoGenParConeSize = cms.double(0.1),
    #         isoGenParETMin = cms.double(20.0),
    #         requireTrackMatch = cms.bool(False),
    #         tkIsoMax = cms.double(5.0)
    #     )
    # )
    # process.bcToEFilter = cms.EDFilter("BCToEFilter",
    #     filterAlgoPSet = cms.PSet(
    #         eTThreshold = cms.double(10),
    #         genParSource = cms.InputTag("genParticles")
    #     )
    # )


    ################################################################################
    ### HLT single filters and producers
    ################################################################################

    process.hltPFPuppiCentralJetQuad30MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 30.0 ),
        MinN = cms.int32( 4 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt1PFPuppiCentralJet75MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 75.0 ),
        MinN = cms.int32( 1 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt1PFPuppiCentralJet70MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 70.0 ),
        MinN = cms.int32( 1 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt2PFPuppiCentralJet60MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 60.0 ),
        MinN = cms.int32( 2 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt2PFPuppiCentralJet40MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 40.0 ),
        MinN = cms.int32( 2 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt3PFPuppiCentralJet45MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 45.0 ),
        MinN = cms.int32( 3 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hlt4PFPuppiCentralJet40MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 40.0 ),
        MinN = cms.int32( 4 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4 = cms.EDProducer( "HLTHtMhtProducer",
        usePt = cms.bool( True ),
        minPtJetHt = cms.double( 30.0 ),
        maxEtaJetMht = cms.double( 2.4 ),
        minNJetMht = cms.int32( 0 ),
        jetsLabel = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        maxEtaJetHt = cms.double( 2.4 ),
        minPtJetMht = cms.double( 0.0 ),
        minNJetHt = cms.int32( 4 ),
        pfCandidatesLabel = cms.InputTag(""),
        excludePFMuons = cms.bool( False )
    )


    process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4 = cms.EDFilter( "HLTHtMhtFilter",
        saveTags = cms.bool( True ),
        mhtLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4'] ),
        meffSlope = cms.vdouble( 1.0 ),
        minHt = cms.vdouble( 330.0 ),
        minMht = cms.vdouble( 0.0 ),
        htLabels = cms.VInputTag( ['hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4'] ),
        minMeff = cms.vdouble( 0.0 )
    )
    process.hltPFPuppiCentralJetsQuad30HT200MaxEta2p4 = process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4.clone(
        minHt = cms.vdouble( 200.0 ),
    )

    # modified sequence
    process.hltDeepBLifetimeTagInfosPFPuppiModEta2p4 = process.hltDeepBLifetimeTagInfosPFPuppi.clone(jets = "hltPFPuppiJetForBtagEta2p4")
    process.hltDeepSecondaryVertexTagInfosPFPuppiModEta2p4 = process.hltDeepSecondaryVertexTagInfosPF.clone(trackIPTagInfos = "hltDeepBLifetimeTagInfosPFPuppiModEta2p4")
    process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4 = process.hltDeepCombinedSecondaryVertexBJetTagsInfos.clone(svTagInfos = "hltDeepSecondaryVertexTagInfosPFPuppiModEta2p4")
    process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4 = process.hltDeepCombinedSecondaryVertexBJetTagsPF.clone(src = "hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4")

    process.hltPrimaryVertexAssociationModEta2p4 = process.hltPrimaryVertexAssociation.clone(jets = cms.InputTag("hltPFPuppiJetForBtagEta2p4"))
    process.hltPfDeepFlavourTagInfosModEta2p4 = process.hltPfDeepFlavourTagInfos.clone(
        jets = cms.InputTag("hltPFPuppiJetForBtagEta2p4"),
        shallow_tag_infos = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4"),
        vertex_associator = cms.InputTag("hltPrimaryVertexAssociationModEta2p4","original"),
    )
    process.hltPfDeepFlavourJetTagsModEta2p4 = process.hltPfDeepFlavourJetTags.clone(
        src = cms.InputTag("hltPfDeepFlavourTagInfosModEta2p4")
    )

    process.HLTBtagDeepCSVSequencePFPuppiModEta2p4 = cms.Sequence(
        process.hltPFPuppiJetForBtagSelectorEta2p4
        +process.hltPFPuppiJetForBtagEta2p4
        +process.hltDeepBLifetimeTagInfosPFPuppiModEta2p4
        +process.hltDeepInclusiveVertexFinderPF
        +process.hltDeepInclusiveSecondaryVerticesPF
        +process.hltDeepTrackVertexArbitratorPF
        +process.hltDeepInclusiveMergedVerticesPF
        +process.hltDeepSecondaryVertexTagInfosPFPuppiModEta2p4
        +process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4
        +process.hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4
    )

    process.HLTBtagDeepFlavourSequencePFPuppiModEta2p4 = cms.Sequence(
        process.hltPFPuppiJetForBtagSelectorEta2p4
        +process.hltPFPuppiJetForBtagEta2p4
        +process.hltDeepBLifetimeTagInfosPFPuppiModEta2p4
        +process.hltDeepInclusiveVertexFinderPF
        +process.hltDeepInclusiveSecondaryVerticesPF
        +process.hltDeepTrackVertexArbitratorPF
        +process.hltDeepInclusiveMergedVerticesPF
        +process.hltDeepSecondaryVertexTagInfosPFPuppiModEta2p4
        +process.hltPrimaryVertexAssociationModEta2p4
        +process.hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4
        +process.hltPfDeepFlavourTagInfosModEta2p4
        +process.hltPfDeepFlavourJetTagsModEta2p4
    )


    process.hltBTagPFPuppiDeepCSV0p31Eta2p4TripleEta2p4 = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltPFPuppiJetForBtagEta2p4" ),
        MinTag = cms.double( 0.31 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepCSV0p38Eta2p4TripleEta2p4 = process.hltBTagPFPuppiDeepCSV0p31Eta2p4TripleEta2p4.clone(
        MinTag = cms.double( 0.38 ),
    )

    process.hltBTagPFPuppiDeepFlavour0p275Eta2p4TripleEta2p4 = cms.EDFilter( "HLTPFJetTag",
        saveTags = cms.bool( True ),
        MinJets = cms.int32( 3 ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTagsModEta2p4','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltPFPuppiJetForBtagEta2p4" ),
        MinTag = cms.double( 0.275 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p375Eta2p4TripleEta2p4 = process.hltBTagPFPuppiDeepFlavour0p275Eta2p4TripleEta2p4.clone(
        MinTag = cms.double( 0.375 ),
    )

    process.hltDoublePFPuppiJets128MaxEta2p4 = cms.EDFilter( "HLT1PFJet",
        saveTags = cms.bool( True ),
        MinPt = cms.double( 128.0 ),
        MinN = cms.int32( 2 ),
        MaxEta = cms.double( 2.4 ),
        MinEta = cms.double( -2.4 ),
        MinMass = cms.double( -1.0 ),
        inputTag = cms.InputTag( "hltAK4PFPuppiJetsCorrected" ),
        MinE = cms.double( -1.0 ),
        triggerType = cms.int32( 86 ),
        MaxMass = cms.double( -1.0 )
    )

    process.hltDoublePFPuppiJets128Eta2p3MaxDeta1p6 =  cms.EDFilter( "HLT2PFJetPFJet",
        saveTags = cms.bool( True ),
        MinMinv = cms.double( 0.0 ),
        originTag2 = cms.VInputTag( 'hltAK4PFPuppiJetsCorrected' ),
        MinDelR = cms.double( 0.0 ),
        MinPt = cms.double( 0.0 ),
        MinN = cms.int32( 1 ),
        originTag1 = cms.VInputTag( 'hltAK4PFPuppiJetsCorrected' ),
        triggerType1 = cms.int32( 86 ),
        triggerType2 = cms.int32( 86 ),
        MaxMinv = cms.double( 1.0E7 ),
        MinDeta = cms.double( -1000.0 ),
        MaxDelR = cms.double( 1000.0 ),
        inputTag1 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta2p4" ),
        inputTag2 = cms.InputTag( "hltDoublePFPuppiJets128MaxEta2p4" ),
        MaxDphi = cms.double( 1.0E7 ),
        MaxDeta = cms.double( 1.6 ),
        MaxPt = cms.double( 1.0E7 ),
        MinDphi = cms.double( 0.0 )
    )

    process.hltBTagPFPuppiDeepCSV0p865DoubleEta2p4 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltPFPuppiJetForBtagEta2p4" ),
        MinTag = cms.double( 0.865 ),
        MaxTag = cms.double( 999999.0 )
    )
    process.hltBTagPFPuppiDeepFlavour0p935DoubleEta2p4 = cms.EDFilter( "HLTPFJetTagWithMatching",
        saveTags = cms.bool( True ),
        deltaR = cms.double( 0.1 ),
        MinJets = cms.int32( 2 ),
        JetTags = cms.InputTag( 'hltPfDeepFlavourJetTagsModEta2p4','probb' ),
        TriggerType = cms.int32( 86 ),
        Jets = cms.InputTag( "hltPFPuppiJetForBtagEta2p4" ),
        MinTag = cms.double( 0.935 ),
        MaxTag = cms.double( 999999.0 )
    )


    ################################################################################
    ## L1 sequences and filters (basic setup cloned from JME)
    ################################################################################
    process.l1tDoublePFPuppiJet112offMaxEta2p4 = cms.EDFilter('L1TJetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      Scalings = cms.PSet(
        barrel = cms.vdouble(11.1254, 1.40627, 0),
        overlap = cms.vdouble(24.8375, 1.4152, 0),
        endcap = cms.vdouble(42.4039, 1.33052, 0),
      ),
      MinPt = cms.double(112.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(2),
      saveTags = cms.bool( True ),
    )

    process.l1tDoublePFPuppiJets128Eta2p3MaxDeta1p6 =  cms.EDFilter( "HLT2CaloJetCaloJet",
        saveTags = cms.bool( True ),
        MinMinv = cms.double( 0.0 ),
        originTag2 = cms.VInputTag(cms.InputTag("l1tSlwPFPuppiJetsCorrected","Phase1L1TJetFromPfCandidates")),
        MinDelR = cms.double( 0.0 ),
        MinPt = cms.double( 0.0 ),
        MinN = cms.int32( 1 ),
        originTag1 = cms.VInputTag(cms.InputTag("l1tSlwPFPuppiJetsCorrected","Phase1L1TJetFromPfCandidates")),
        triggerType1 = cms.int32( -116 ),
        triggerType2 = cms.int32( -116 ),
        MaxMinv = cms.double( 1.0E7 ),
        MinDeta = cms.double( -1000.0 ),
        MaxDelR = cms.double( 1000.0 ),
        inputTag1 = cms.InputTag( "l1tDoublePFPuppiJet112offMaxEta2p4" ),
        inputTag2 = cms.InputTag( "l1tDoublePFPuppiJet112offMaxEta2p4" ),
        MaxDphi = cms.double( 1.0E7 ),
        MaxDeta = cms.double( 1.6 ),
        MaxPt = cms.double( 1.0E7 ),
        MinDphi = cms.double( 0.0 ),
    )

    process.l1t1PFPuppiJet70offMaxEta2p4 = cms.EDFilter('L1TJetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      Scalings = cms.PSet(
        barrel = cms.vdouble(11.1254, 1.40627, 0),
        overlap = cms.vdouble(24.8375, 1.4152, 0),
        endcap = cms.vdouble(42.4039, 1.33052, 0),
      ),
      MinPt = cms.double(70.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(1),
    )

    process.l1t2PFPuppiJet55offMaxEta2p4 = cms.EDFilter('L1TJetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      Scalings = cms.PSet(
        barrel = cms.vdouble(11.1254, 1.40627, 0),
        overlap = cms.vdouble(24.8375, 1.4152, 0),
        endcap = cms.vdouble(42.4039, 1.33052, 0),
      ),
      MinPt = cms.double(55.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(2),
    )

    process.l1t4PFPuppiJet40offMaxEta2p4 = cms.EDFilter('L1TJetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      Scalings = cms.PSet(
        barrel = cms.vdouble(11.1254, 1.40627, 0),
        overlap = cms.vdouble(24.8375, 1.4152, 0),
        endcap = cms.vdouble(42.4039, 1.33052, 0),
      ),
      MinPt = cms.double(40.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(4),
    )

    process.l1t4PFPuppiJet25OnlineMaxEta2p4 = cms.EDFilter('L1TJetFilter',
      inputTag = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      # Scalings = cms.PSet( ## no scaling
      #   barrel = cms.vdouble(11.1254, 1.40627, 0),
      #   overlap = cms.vdouble(24.8375, 1.4152, 0),
      #   endcap = cms.vdouble(42.4039, 1.33052, 0),
      # ),
      MinPt = cms.double(25.),
      MinEta = cms.double(-2.4),
      MaxEta = cms.double(2.4),
      MinN = cms.int32(4),
    )

    # L1T-HT
    process.l1tPFPuppiHTMaxEta2p4 = cms.EDProducer('HLTHtMhtProducer',
      jetsLabel = cms.InputTag('l1tSlwPFPuppiJetsCorrected', 'Phase1L1TJetFromPfCandidates'),
      minPtJetHt = cms.double(30.),
      maxEtaJetHt = cms.double(2.4)
    )

    process.l1tPFPuppiHT400offMaxEta2p4 = cms.EDFilter('L1TEnergySumFilter',
      inputTag = cms.InputTag('l1tPFPuppiHTMaxEta2p4'),
      Scalings = cms.PSet(
        theScalings = cms.vdouble(50.0182, 1.0961, 0), # PFPhase1HT090OfflineEtCut
      ),
      TypeOfSum = cms.string('HT'),
      MinPt = cms.double(400.),
    )



    # final paths
    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.l1t4PFPuppiJet25OnlineMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        +process.HLTBtagDeepCSVSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepCSV0p31Eta2p4TripleEta2p4
    )

    process.HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepCSV_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.l1t4PFPuppiJet25OnlineMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet70MaxEta2p4
        +process.hlt2PFPuppiCentralJet40MaxEta2p4
        # +process.hlt3PFPuppiCentralJet45MaxEta2p4 # not needed
        # +process.hlt4PFPuppiCentralJet40MaxEta2p4 # not needed
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT200MaxEta2p4
        +process.HLTBtagDeepCSVSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepCSV0p38Eta2p4TripleEta2p4
    )



    process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.l1t4PFPuppiJet25OnlineMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet75MaxEta2p4
        +process.hlt2PFPuppiCentralJet60MaxEta2p4
        +process.hlt3PFPuppiCentralJet45MaxEta2p4
        +process.hlt4PFPuppiCentralJet40MaxEta2p4
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT330MaxEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepFlavour0p275Eta2p4TripleEta2p4
    )
    process.HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepFlavour_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.l1t4PFPuppiJet25OnlineMaxEta2p4
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiCentralJetQuad30MaxEta2p4
        +process.hlt1PFPuppiCentralJet70MaxEta2p4
        +process.hlt2PFPuppiCentralJet40MaxEta2p4
        # +process.hlt4PFPuppiCentralJet40MaxEta2p4 # not needed
        # +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiCentralJetsQuad30HT200MaxEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepFlavour0p375Eta2p4TripleEta2p4
    )


    # L1T seed
    process.L1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1 = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tPFPuppiHT400offMaxEta2p4
        +process.l1t1PFPuppiJet70offMaxEta2p4
        +process.l1t2PFPuppiJet55offMaxEta2p4
        +process.l1t4PFPuppiJet40offMaxEta2p4
        +process.l1t4PFPuppiJet25OnlineMaxEta2p4
    )

    # filters for QCD enriched
    # process.QCDMuon = cms.Path(
    #     process.muGenFilter
    # )
    # process.Gen_QCDEmEnrichingNoBCToEFilter = cms.Path(
    #    ~process.bcToEFilter +
    #    process.emEnrichingFilter
    # )
    # process.Gen_QCDEmEnrichingFilter = cms.Path(
    #    process.emEnrichingFilter
    # )
    # process.Gen_QCDBCToEFilter = cms.Path(
    #    process.bcToEFilter
    # )
    # process.Gen_QCDMuGenFilter = cms.Path(
    #    process.muGenFilter
    # )


    process.HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.l1tDoublePFPuppiJets128Eta2p3MaxDeta1p6
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltDoublePFPuppiJets128MaxEta2p4
        +process.hltDoublePFPuppiJets128Eta2p3MaxDeta1p6
        +process.HLTBtagDeepCSVSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepCSV0p865DoubleEta2p4
    )


    process.HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepFlavour_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.l1tDoublePFPuppiJets128Eta2p3MaxDeta1p6
        +process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltDoublePFPuppiJets128MaxEta2p4
        +process.hltDoublePFPuppiJets128Eta2p3MaxDeta1p6
        +process.HLTBtagDeepFlavourSequencePFPuppiModEta2p4
        +process.hltBTagPFPuppiDeepFlavour0p935DoubleEta2p4
    )


    # L1T seed
    process.L1_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_p71_2p4_v1 = cms.Path(
        process.l1tDoublePFPuppiJet112offMaxEta2p4
        +process.l1tDoublePFPuppiJets128Eta2p3MaxDeta1p6
    )

    # to be run for every event
    process.noFilter_PFDeepCSVPuppi = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        # +process.hltPFPuppiJetForBtagSelectorEta2p4
        # +process.hltPFPuppiJetForBtagEta2p4
        +process.HLTBtagDeepCSVSequencePFPuppi
    )

    process.noFilter_PFDeepFlavourPuppi = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        # +process.hltPFPuppiJetForBtagSelectorEta2p4
        # +process.hltPFPuppiJetForBtagEta2p4
        +process.HLTBtagDeepFlavourSequencePFPuppi
    )

    process.L1Objects = cms.Path(
        process.l1tPFPuppiHTMaxEta2p4
        +process.l1tDoublePFPuppiJet112offMaxEta2p4
    )

    process.HLTObjects = cms.Path(
        process.HLTParticleFlowSequence
        +process.HLTAK4PFPuppiJetsReconstruction
        +process.hltPFPuppiHT
        +process.hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4
        +process.hltPFPuppiJetForBtagSelectorEta2p4
        +process.hltPFPuppiJetForBtagEta2p4
    )

    process.schedule_().extend([
      # L1T seeds
      process.L1_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1,
      process.L1_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_p71_2p4_v1,

      # general paths and filters
      process.L1Objects,
      process.HLTObjects,
      # process.QCDMuon,
      # process.Gen_QCDMuGenFilter,
      # process.Gen_QCDEmEnrichingNoBCToEFilter,
      # process.Gen_QCDEmEnrichingFilter,
      # process.Gen_QCDBCToEFilter,
      # process.noFilter_PFDeepCSVPuppi,
      # process.noFilter_PFDeepFlavourPuppi,

      # based on DeepCSV
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepCSV_2p4_v1,
      process.HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepCSV_2p4_v1,
      process.HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepCSV_2p4_v1,

      # based on DeepJet
      process.HLT_PFHT330PT30_QuadPFPuppiJet_75_60_45_40_TriplePFPuppiBTagDeepFlavour_2p4_v1,
      process.HLT_PFHT200PT30_QuadPFPuppiJet_70_40_30_30_TriplePFPuppiBTagDeepFlavour_2p4_v1,
      process.HLT_DoublePFPuppiJets128_DoublePFPuppiBTagDeepFlavour_2p4_v1,
    ])


    return process


###
### command-line arguments
###
import FWCore.ParameterSet.VarParsing as vpo
opts = vpo.VarParsing('analysis')

opts.register('reco', 'HLT_TRKv06_TICL',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'keyword defining reconstruction methods for JME inputs')

opts.register('BTVreco', 'default',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'which reco to load for BTV sequence, default = default')

opts.register('skipEvents', 0,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of events to be skipped')

opts.register('dumpPython', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to python file with content of cms.Process')

opts.register('numThreads', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of threads')

opts.register('numStreams', 1,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.int,
              'number of streams')

opts.register('wantSummary', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'show cmsRun summary at job completion')

opts.register('globalTag', None,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'argument of process.GlobalTag.globaltag')

opts.register('output', 'out.root',
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.string,
              'path to output ROOT file')

opts.register('runTiming', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'run timing instead of rates')

opts.register('runRates', False,
              vpo.VarParsing.multiplicity.singleton,
              vpo.VarParsing.varType.bool,
              'run rates')

opts.parseArguments()

###
### base configuration file
### (choice of reconstruction sequence)
###
if opts.runRates or opts.runTiming:
    process = customize_hltPhase2_BTV_paths(opts.reco, opts.BTVreco)
    ###
    ### job configuration (input, output, GT, etc)
    ###

    # update process.GlobalTag.globaltag
    if opts.globalTag is not None:
       process.GlobalTag.globaltag = opts.globalTag

    # max number of events to be processed
    process.maxEvents.input = opts.maxEvents

    # number of events to be skipped
    process.source.skipEvents = cms.untracked.uint32(opts.skipEvents)

    if opts.runTiming:
        # multi-threading settings
        process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
        process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)
        process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32(10240)
    else:
        # multi-threading settings
        process.options.numberOfThreads = cms.untracked.uint32(opts.numThreads if (opts.numThreads > 1) else 1)
        process.options.numberOfStreams = cms.untracked.uint32(opts.numStreams if (opts.numStreams > 1) else 1)

    # show cmsRun summary at job completion
    process.options.wantSummary = cms.untracked.bool(opts.wantSummary)

    # EDM input
    if opts.inputFiles:
       process.source.fileNames = opts.inputFiles
    else:
       process.source.fileNames = [
         '/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/VBF_HHTo4B_CV_0_5_C2V_1_C3_1_TuneCP5_PSWeights_14TeV-madgraph-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/08904C2F-2A34-1C45-86B3-F05541DB0C00.root',
       ]
    # process.MessageLogger = cms.Service("MessageLogger",
    #        destinations   = cms.untracked.vstring('detailedInfo','debugInfo', 'critical','cerr'),
    #        critical       = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    #        detailedInfo   = cms.untracked.PSet(threshold = cms.untracked.string('INFO')),
    #        debugInfo   = cms.untracked.PSet(threshold = cms.untracked.string('DEBUG')),
    #        cerr           = cms.untracked.PSet(threshold  = cms.untracked.string('WARNING'))
    # )


    if opts.runTiming:
        #timing test
        from HLTrigger.Timer.FastTimer import customise_timer_service_print,customise_timer_service,customise_timer_service_singlejob
        process = customise_timer_service_print(process)
        process = customise_timer_service(process)
        # process = customise_timer_service_singlejob(process)
        process.FastTimerService.dqmTimeRange            = 20000.
        process.FastTimerService.dqmTimeResolution       =    10.
        process.FastTimerService.dqmPathTimeRange        = 10000.
        process.FastTimerService.dqmPathTimeResolution   =     5.
        process.FastTimerService.dqmModuleTimeRange      =  1000.
        process.FastTimerService.dqmModuleTimeResolution =     1.
        # process.dqmOutput.fileName = cms.untracked.string(opts.output)

    # if opts.runRates:


    if opts.runRates:
        # dump content of cms.Process to python file
        if opts.dumpPython is not None:
           open(opts.dumpPython, 'w').write(process.dumpPython())

        print 'process.GlobalTag.globaltag =', process.GlobalTag.globaltag
        print 'dumpPython =', opts.dumpPython
        print 'option: reco =', opts.reco
        # print 'option: reco =', opts.reco, '(skimTracks = '+str(opt_skimTracks)+')'
        print 'option: BTVreco =', opts.BTVreco
