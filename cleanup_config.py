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

"""
HLTDoLocalPixelSequenceRegForBTag
"""
process.HLTDoLocalPixelSequenceRegForBTag = cms.Sequence(process.hltSelectorJets20L1FastJet+
        process.hltSelectorCentralJets20L1FastJeta+
        process.hltSiPixelDigisRegForBTag+
        process.hltSiPixelClustersRegForBTag+
        process.hltSiPixelClustersRegForBTagCache+
        process.hltSiPixelRecHitsRegForBTag+
        process.hltPixelLayerQuadrupletsRegForBTag)
process.hltSelectorJets20L1FastJet = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(20.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsCorrected")
)
process.hltSelectorCentralJets20L1FastJeta = cms.EDFilter("EtaRangeCaloJetSelector",
    etaMax = cms.double(2.4),
    etaMin = cms.double(-2.4),
    src = cms.InputTag("hltSelectorJets20L1FastJet")
)
process.hltSiPixelDigisRegForBTag = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaPhi = cms.vdouble(0.5),
        inputs = cms.VInputTag("hltSelectorCentralJets20L1FastJeta"),
        maxZ = cms.vdouble(24.0)
    ),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)
process.hltSiPixelClustersRegForBTag = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterMode = cms.string('PixelThresholdClusterizer'),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(2000),
    ElectronPerADCGain = cms.double(135.0),
    MissCalibrate = cms.bool(True),
    Phase2Calibration = cms.bool(False),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(1),
    VCaltoElectronGain_L1 = cms.int32(1),
    VCaltoElectronOffset = cms.int32(0),
    VCaltoElectronOffset_L1 = cms.int32(0),
    maxNumberOfClusters = cms.int32(40000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigisRegForBTag")
)
process.hltSiPixelClustersRegForBTagCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClustersRegForBTag")
)
process.hltSiPixelRecHitsRegForBTag = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('hltESPPixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("hltSiPixelClustersRegForBTag")
)
process.hltPixelLayerQuadrupletsRegForBTag = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsRegForBTag'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsRegForBTag'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4',
        'BPix1+BPix2+BPix3+FPix1_pos',
        'BPix1+BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos+FPix2_pos',
        'BPix1+BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
    )
)
"""
HLTFastRecopixelvertexingSequence
"""
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
process.hltSelector4CentralJetsL1FastJet = cms.EDFilter("LargestEtCaloJetSelector",
    filter = cms.bool(False),
    maxNumber = cms.uint32(4),
    src = cms.InputTag("hltSelectorCentralJets20L1FastJeta")
)
process.hltFastPrimaryVertex = cms.EDProducer("FastPrimaryVertexWithWeightsProducer",
    EC_weight = cms.double(0.008),
    PixelCellHeightOverWidth = cms.double(1.8),
    barrel = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusters = cms.InputTag("hltSiPixelClustersRegForBTag"),
    endCap = cms.bool(True),
    jets = cms.InputTag("hltSelector4CentralJetsL1FastJet"),
    maxDeltaPhi = cms.double(0.21),
    maxDeltaPhi_EC = cms.double(0.14),
    maxJetEta = cms.double(2.6),
    maxJetEta_EC = cms.double(2.6),
    maxSizeX = cms.double(2.1),
    maxSizeY_q = cms.double(2.0),
    maxZ = cms.double(19.0),
    minJetEta_EC = cms.double(1.3),
    minJetPt = cms.double(0.0),
    minSizeY_q = cms.double(-0.6),
    njets = cms.int32(999),
    peakSizeY_q = cms.double(1.0),
    pixelCPE = cms.string('hltESPPixelCPEGeneric'),
    ptWeighting = cms.bool(True),
    ptWeighting_offset = cms.double(-1.0),
    ptWeighting_slope = cms.double(0.05),
    weightCut_step2 = cms.double(0.05),
    weightCut_step3 = cms.double(0.1),
    weight_SizeX1 = cms.double(0.88),
    weight_charge_down = cms.double(11000.0),
    weight_charge_peak = cms.double(22000.0),
    weight_charge_up = cms.double(190000.0),
    weight_dPhi = cms.double(0.13888888),
    weight_dPhi_EC = cms.double(0.064516129),
    weight_rho_up = cms.double(22.0),
    zClusterSearchArea_step2 = cms.double(3.0),
    zClusterSearchArea_step3 = cms.double(0.55),
    zClusterWidth_step1 = cms.double(2.0),
    zClusterWidth_step2 = cms.double(0.65),
    zClusterWidth_step3 = cms.double(0.3)
)
process.hltFastPVPixelVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("hltFastPrimaryVertex")
)

process.hltFastPVPixelVerticesFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("hltFastPVPixelVertices")
)
process.hltFastPVPixelVertices = cms.EDProducer("PixelVertexProducer",
    Finder = cms.string('DivisiveVertexFinder'),
    Method2 = cms.bool(True),
    NTrkMin = cms.int32(2),
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForBTag')
    ),
    PtMin = cms.double(1.0),
    TrackCollection = cms.InputTag("hltFastPVPixelTracksMerger"),
    UseError = cms.bool(True),
    Verbosity = cms.int32(0),
    WtAverage = cms.bool(True),
    ZOffset = cms.double(10.0),
    ZSeparation = cms.double(0.07),
    beamSpot = cms.InputTag("hltOnlineBeamSpot")
)
process.hltFastPVPixelTracksMerger = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltFastPVPixelTracks", "hltFastPVPixelTracksRecover"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(False),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltFastPVPixelTracks", "hltFastPVPixelTracksRecover"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)
process.hltFastPVPixelTracksHitDoubletsRecover = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerQuadrupletsRegForBTag"),
    trackingRegions = cms.InputTag("hltFastPVPixelTracksTrackingRegionsRecover"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)
process.hltFastPVPixelTracksTrackingRegionsRecover = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaEta = cms.double(0.5),
        deltaPhi = cms.double(0.5),
        input = cms.InputTag("hltFastPVJetVertexChecker"),
        maxNRegions = cms.int32(10),
        maxNVertices = cms.int32(1),
        measurementTrackerName = cms.InputTag(""),
        mode = cms.string('BeamSpotFixed'),
        nSigmaZBeamSpot = cms.double(0.0),
        nSigmaZVertex = cms.double(0.0),
        originRadius = cms.double(0.3),
        precise = cms.bool(True),
        ptMin = cms.double(0.9),
        searchOpt = cms.bool(False),
        vertexCollection = cms.InputTag(""),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(20.0),
        zErrorVetex = cms.double(0.0)
    )
)
process.hltFastPVPixelTracksRecoverFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)
process.hltFastPVPixelTracksRecover = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = cms.InputTag("hltFastPVPixelTracksRecoverFilter"),
    Fitter = cms.InputTag("hltFastPVPixelTracksRecoverFitter"),
    SeedingHitSets = cms.InputTag("hltFastPVPixelTracksHitQuadrupletsRecover"),
    passLabel = cms.string('')
)
process.hltFastPVPixelTracksHitQuadrupletsRecover = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0.0),
    CAPhiCut = cms.double(0.2),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.002),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersRegForBTagCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltFastPVPixelTracksHitDoubletsRecover"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(False),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2.0),
        value1 = cms.double(200.0),
        value2 = cms.double(50.0)
    ),
    useBendingCorrection = cms.bool(True)
)
process.hltFastPVPixelTracksHitDoubletsRecover = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerQuadrupletsRegForBTag"),
    trackingRegions = cms.InputTag("hltFastPVPixelTracksTrackingRegionsRecover"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)
process.hltFastPVPixelTracksTrackingRegionsRecover = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaEta = cms.double(0.5),
        deltaPhi = cms.double(0.5),
        input = cms.InputTag("hltFastPVJetVertexChecker"),
        maxNRegions = cms.int32(10),
        maxNVertices = cms.int32(1),
        measurementTrackerName = cms.InputTag(""),
        mode = cms.string('BeamSpotFixed'),
        nSigmaZBeamSpot = cms.double(0.0),
        nSigmaZVertex = cms.double(0.0),
        originRadius = cms.double(0.3),
        precise = cms.bool(True),
        ptMin = cms.double(0.9),
        searchOpt = cms.bool(False),
        vertexCollection = cms.InputTag(""),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(20.0),
        zErrorVetex = cms.double(0.0)
    )
)
process.hltFastPVPixelTracksRecoverFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)
process.hltFastPVPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)
process.hltFastPVPixelTracks = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = cms.InputTag("hltFastPVPixelTracksFilter"),
    Fitter = cms.InputTag("hltFastPVPixelTracksFitter"),
    SeedingHitSets = cms.InputTag("hltFastPVPixelTracksHitQuadruplets"),
    passLabel = cms.string('')
)
process.hltFastPVPixelTracksHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0.0),
    CAPhiCut = cms.double(0.2),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.002),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersRegForBTagCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltFastPVPixelTracksHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2.0),
        value1 = cms.double(200.0),
        value2 = cms.double(50.0)
    ),
    useBendingCorrection = cms.bool(True)
)
process.hltFastPVPixelTracksHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerQuadrupletsRegForBTag"),
    trackingRegions = cms.InputTag("hltFastPVPixelTracksTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)
process.hltFastPVPixelTracksTrackingRegions = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
process.hltFastPVPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)
process.hltFastPVPixelTracksFilter = cms.EDProducer("PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double(1000.0),
    nSigmaInvPtTolerance = cms.double(0.0),
    nSigmaTipMaxTolerance = cms.double(0.0),
    ptMin = cms.double(0.0),
    tipMax = cms.double(999.0)
)




















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

