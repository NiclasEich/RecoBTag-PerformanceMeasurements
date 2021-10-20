process.HLTBtagDeepCSVSequenceL3 = cms.Sequence(process.hltSelectorJets30L1FastJet+
        process.hltSelectorCentralJets30L1FastJeta+
        process.hltSelector8CentralJetsL1FastJet+
        process.HLTTrackReconstructionForBTag+
        process.hltVerticesL3+
        process.hltFastPixelBLifetimeL3Associator+
        process.hltImpactParameterTagInfos+
        process.hltInclusiveVertexFinder+
        process.hltInclusiveSecondaryVertices+
        process.hltTrackVertexArbitrator+
        process.hltInclusiveMergedVertices+
        process.hltInclusiveSecondaryVertexFinderTagInfos+
        process.hltDeepCombinedSecondaryVertexBJetTagsInfosCalo+
        process.hltDeepCombinedSecondaryVertexBJetTagsCalo)
"""

DeepCSVSequenceL3

"""

"""
Filtes
"""
process.hltSelectorJets30L1FastJet = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(30.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsCorrectedIDPassed")
)
process.hltSelectorCentralJets30L1FastJeta = cms.EDFilter("EtaRangeCaloJetSelector",
    etaMax = cms.double(2.4),
    etaMin = cms.double(-2.4),
    src = cms.InputTag("hltSelectorJets30L1FastJet")
)
process.hltSelector8CentralJetsL1FastJet = cms.EDFilter("LargestEtCaloJetSelector",
    filter = cms.bool(False),
    maxNumber = cms.uint32(8),
    src = cms.InputTag("hltSelectorCentralJets30L1FastJeta")
)

process.hltVerticesL3 = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.4),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(999.0),
            dzCutOff = cms.double(4.0),
            uniquetrkweight = cms.double(0.9),
            vertexSize = cms.double(0.15),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(999.0),
        maxEta = cms.double(100.0),
        maxNormalizedChi2 = cms.double(20.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("hltMergedTracksForBTag"),
    TrackTimeResosLabel = cms.InputTag("dummy_default"),
    TrackTimesLabel = cms.InputTag("dummy_default"),
    beamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
    isRecoveryIteration = cms.bool(False),
    recoveryVtxCollection = cms.InputTag(""),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(3.0),
            label = cms.string(''),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(False)
        ),
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(3.0),
            label = cms.string('WithBS'),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(True)
        )
    )
)

process.hltFastPixelBLifetimeL3Associator = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("hltSelector8CentralJetsL1FastJet"),
    pvSrc = cms.InputTag(""),
    tracks = cms.InputTag("hltMergedTracksForBTag"),
    useAssigned = cms.bool(False)
)

process.hltImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("hltFastPixelBLifetimeL3Associator"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("hltVerticesL3","WithBS"),
    useTrackQuality = cms.bool(False)
)

process.hltInclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2.0),
    secondaryVertices = cms.InputTag("hltInclusiveVertexFinder")
)

process.hltTrackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3.0),
    fitterTini = cms.double(256.0),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("hltVerticesL3"),
    secondaryVertices = cms.InputTag("hltInclusiveSecondaryVertices"),
    sigCut = cms.double(5.0),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("hltIter2MergedForBTag")
)

process.hltInclusiveMergedVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("hltTrackVertexArbitrator")
)

process.hltInclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("hltInclusiveMergedVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("hltImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(2),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.hltDeepCombinedSecondaryVertexBJetTagsInfosCalo = cms.EDProducer("TrackDeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5.0),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500.0),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3.0),
            min_pT = cms.double(120.0),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5.0),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500.0),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3.0),
            min_pT = cms.double(120.0),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("hltInclusiveSecondaryVertexFinderTagInfos")
)

process.hltDeepCombinedSecondaryVertexBJetTagsCalo = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfosCalo"),
    toAdd = cms.PSet(
        probbb = cms.string('probb')
    )
)
"""
modules
"""

process.HLTTrackReconstructionForBTag = cms.Sequence(process.HLTDoLocalPixelSequenceRegForBTag+
                                           process.HLTFastRecopixelvertexingSequence+
                                          process.HLTDoLocalStripSequenceRegForBTag+
                                         process.HLTIterativeTrackingIter02ForBTag)
"""
subsequences
"""
process.HLTDoLocalPixelSequenceRegForBTag = cms.Sequence(process.hltSelectorJets20L1FastJet+
        process.hltSelectorCentralJets20L1FastJeta+
        process.hltSiPixelDigisRegForBTag+
        process.hltSiPixelClustersRegForBTag+
        process.hltSiPixelClustersRegForBTagCache+
        process.hltSiPixelRecHitsRegForBTag+
        process.hltPixelLayerQuadrupletsRegForBTag)
process.HLTFastRecopixelvertexingSequence = cms.Sequence(process.hltSelector4CentralJetsL1FastJet+
        process.hltFastPrimaryVertex+
        process.hltFastPVPixelVertexFilter+
        process.hltFastPVPixelTracksFilter+
        process.hltFastPVPixelTracksFitter+
        process.hltFastPVPixelTracksTrackingRegions+
        process.hltFastPVPixelTracksHitDoublets+
        process.hltFastPVPixelTracksHitQuadruplets+
        process.hltFastPVPixelTracks+
        process.hltFastPVJetTracksAssociator+
        process.hltFastPVJetVertexChecker+
        process.hltFastPVPixelTracksRecoverFilter+
        process.hltFastPVPixelTracksRecoverFitter+
        process.hltFastPVPixelTracksTrackingRegionsRecover+
        process.hltFastPVPixelTracksHitDoubletsRecover+
        process.hltFastPVPixelTracksHitQuadrupletsRecover+
        process.hltFastPVPixelTracksRecover+
        process.hltFastPVPixelTracksMerger+
        process.hltFastPVPixelVertices+
        process.hltFastPVPixelVerticesFilter)
process.HLTDoLocalStripSequenceRegForBTag = cms.Sequence(process.hltSiStripExcludedFEDListProducer+
        process.hltSiStripRawToClustersFacility+
        process.hltSiStripClustersRegForBTag)
process.HLTIterativeTrackingIter02ForBTag = cms.Sequence(process.HLTIterativeTrackingIteration0ForBTag+
        process.HLTIterativeTrackingIteration1ForBTag+
        process.hltIter1MergedForBTag+
        process.HLTIterativeTrackingIteration2ForBTag+
        process.hltIter2MergedForBTag+
        process.HLTIterativeTrackingDoubletRecoveryForBTag+
        process.hltMergedTracksForBTag)

