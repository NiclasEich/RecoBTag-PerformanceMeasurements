import FWCore.ParameterSet.Config as cms

def replaceDisplacedJetInProcess(process):

    # fix the DisplacedJet paths
    # ie relabel all the ForBTag legacy modules via cloning so that we can modify *ForBTag later for Run 3 ROI setup

    process.hltIter0PFLowPixelSeedsFromPixelTracksForDisplaced = process.hltIter0PFLowPixelSeedsFromPixelTracksForBTag.clone()

    process.hltIter0PFlowCkfTrackCandidatesForDisplaced = process.hltIter0PFlowCkfTrackCandidatesForBTag.clone(
        MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersRegForDisplaced" ),
        src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracksForDisplaced" )
    )

    process.hltIter0PFlowCtfWithMaterialTracksForDisplaced = process.hltIter0PFlowCtfWithMaterialTracksForBTag.clone(
        src = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesForDisplaced" ),
        MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersRegForDisplaced" )
    )

    process.hltIter0PFlowTrackCutClassifierForDisplaced = process.hltIter0PFlowTrackCutClassifierForBTag.clone(
        src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksForDisplaced" ),
    )

    process.hltIter0PFlowTrackSelectionHighPurityForDisplaced = process.hltIter0PFlowTrackSelectionHighPurityForBTag.clone(
        originalSource = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksForDisplaced" ),
        originalMVAVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifierForDisplaced','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifierForDisplaced','QualityMasks' ),
    )

    process.HLTIterativeTrackingIteration0ForDisplaced = cms.Sequence(
        process.hltIter0PFLowPixelSeedsFromPixelTracksForDisplaced+
        process.hltIter0PFlowCkfTrackCandidatesForDisplaced+
        process.hltIter0PFlowCtfWithMaterialTracksForDisplaced+
        process.hltIter0PFlowTrackCutClassifierForDisplaced+
        process.hltIter0PFlowTrackSelectionHighPurityForDisplaced
    )

    process.hltSiPixelDigisRegForDisplaced = process.hltSiPixelDigisRegForBTag.clone()

    process.hltSiPixelClustersRegForDisplaced = process.hltSiPixelClustersRegForBTag.clone(
        src = cms.InputTag( "hltSiPixelDigisRegForDisplaced" ),
    )
    process.hltSiPixelClustersRegForDisplacedCache = process.hltSiPixelClustersRegForBTagCache.clone(
        src = cms.InputTag( "hltSiPixelClustersRegForDisplaced" ),
    )

    process.hltSiPixelRecHitsRegForDisplaced = process.hltSiPixelRecHitsRegForBTag.clone(
        src = cms.InputTag( "hltSiPixelClustersRegForDisplaced" ),
    )

    process.hltPixelLayerQuadrupletsRegForDisplaced = process.hltPixelLayerQuadrupletsRegForBTag.clone(
        BPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0027 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.006 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
        FPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0051 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.0036 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
    )

    process.HLTDoLocalPixelSequenceRegForDisplaced = cms.Sequence(
        process.hltSelectorJets20L1FastJet +
        process.hltSelectorCentralJets20L1FastJeta +
        process.hltSiPixelDigisRegForDisplaced +
        process.hltSiPixelClustersRegForDisplaced +
        process.hltSiPixelClustersRegForDisplacedCache +
        process.hltSiPixelRecHitsRegForDisplaced +
        process.hltPixelLayerQuadrupletsRegForDisplaced
    )

    process.hltFastPrimaryVertex.clusters = cms.InputTag( "hltSiPixelClustersRegForDisplaced" )

    process.hltFastPVPixelTracksHitDoublets.seedingLayers = cms.InputTag( "hltPixelLayerQuadrupletsRegForDisplaced" )

    process.hltFastPVPixelTracksHitQuadruplets.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersRegForDisplacedCache" )

    process.hltFastPVPixelTracksHitDoubletsRecover.seedingLayers = cms.InputTag( "hltPixelLayerQuadrupletsRegForDisplaced" )

    process.hltFastPVPixelTracksHitQuadrupletsRecover.SeedComparitorPSet.clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersRegForDisplacedCache" )

    process.hltSiStripClustersRegForDisplaced = process.hltSiStripClustersRegForBTag.clone(
        pixelClusterProducer = cms.string( "hltSiPixelClustersRegForDisplaced" ),
    )

    process.HLTDoLocalStripSequenceRegForDisplaced = cms.Sequence(
        process.hltSiStripExcludedFEDListProducer +
        process.hltSiStripRawToClustersFacility +
        process.hltSiStripClustersRegForDisplaced
    )


    process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets = cms.Sequence(
        process.HLTDoLocalPixelSequenceRegForDisplaced+
        process.HLTFastRecopixelvertexingSequence+
        process.HLTDoLocalStripSequenceRegForDisplaced+
        process.hltSelectorJets30L1FastJet+
        process.hltSelectorCentralJets30L1FastJeta+
        process.hltSelector8CentralJetsL1FastJet
    )

    process.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt.tracks = cms.InputTag("hltIter0PFlowTrackSelectionHighPurityForDisplaced")

    process.hltIter1ClustersRefRemovalForDisplaced = process.hltIter1ClustersRefRemovalForBTag.clone(
        trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForDisplaced" ),
        pixelClusters = cms.InputTag( "hltSiPixelClustersRegForDisplaced" ),
    )

    process.hltIter1MaskedMeasurementTrackerEventForDisplaced = process.hltIter1MaskedMeasurementTrackerEventForBTag.clone(
        src = cms.InputTag( "hltSiStripClustersRegForDisplaced" ),
        clustersToSkip = cms.InputTag( "hltIter1ClustersRefRemovalForDisplaced" )
    )

    process.hltIter1PixelLayerQuadrupletsForDisplaced = process.hltIter1PixelLayerQuadrupletsForBTag.clone(
        BPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0027 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalForDisplaced" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.006 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
        FPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0051 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalForDisplaced" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.0036 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
    )

    process.hltIter1PFlowPixelTrackingRegionsForDisplaced  = process.hltIter1PFlowPixelTrackingRegionsForBTag.clone()
    process.hltIter1PFlowPixelTrackingRegionsForDisplaced.RegionPSet.measurementTrackerName = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForDisplaced" )

    process.hltIter1PFlowPixelClusterCheckForDisplaced = process.hltIter1PFlowPixelClusterCheckForBTag.clone(
        ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForBTag" ),
        PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForBTag" )
    )

    process.hltIter1PFlowPixelHitDoubletsForDisplaced = process.hltIter1PFlowPixelHitDoubletsForBTag.clone(
        seedingLayers = cms.InputTag( "hltIter1PixelLayerQuadrupletsForDisplaced" ),
        trackingRegions = cms.InputTag( "hltIter1PFlowPixelTrackingRegionsForDisplaced" ),
        clusterCheck = cms.InputTag( "hltIter1PFlowPixelClusterCheckForDisplaced" ),
    )

    process.hltIter1PFlowPixelHitQuadrupletsForDisplaced = process.hltIter1PFlowPixelHitQuadrupletsForBTag.clone(
        doublets = cms.InputTag( "hltIter1PFlowPixelHitDoubletsForDisplaced" ),
        SeedComparitorPSet = cms.PSet(
          clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersRegForDisplacedCache" )
        )
    )

    process.hltIter1PixelTracksForDisplaced = process.hltIter1PixelTracksForBTag.clone(
        SeedingHitSets = cms.InputTag( "hltIter1PFlowPixelHitQuadrupletsForDisplaced" ),
    )

    process.hltIter1PFLowPixelSeedsFromPixelTracksForDisplaced = process.hltIter1PFLowPixelSeedsFromPixelTracksForBTag.clone(
        InputCollection = cms.InputTag( "hltIter1PixelTracksForDisplaced" )
    )

    process.hltIter1PFlowCkfTrackCandidatesForDisplaced = process.hltIter1PFlowCkfTrackCandidatesForBTag.clone(
        MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForDisplaced" ),
        src = cms.InputTag( "hltIter1PFLowPixelSeedsFromPixelTracksForDisplaced" ),
    )

    process.hltIter1PFlowCtfWithMaterialTracksForDisplaced = process.hltIter1PFlowCtfWithMaterialTracksForBTag.clone(
    src = cms.InputTag( "hltIter1PFlowCkfTrackCandidatesForDisplaced" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForDisplaced" )
    )

    process.hltIter1PFlowTrackCutClassifierPromptForDisplaced = process.hltIter1PFlowTrackCutClassifierPromptForBTag.clone(
        src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracksForDisplaced" )
    )

    process.hltIter1PFlowTrackCutClassifierDetachedForDisplaced = process.hltIter1PFlowTrackCutClassifierDetachedForBTag.clone(
        src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracksForDisplaced" )
    )

    process.hltIter1PFlowTrackCutClassifierMergedForDisplaced = process.hltIter1PFlowTrackCutClassifierMergedForBTag.clone(
         inputClassifiers = cms.vstring( 'hltIter1PFlowTrackCutClassifierPromptForDisplaced','hltIter1PFlowTrackCutClassifierDetachedForDisplaced' )
    )

    process.hltIter1PFlowTrackSelectionHighPurityForDisplaced = process.hltIter1PFlowTrackSelectionHighPurityForBTag.clone(
        originalSource = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracksForDisplaced" ),
        originalMVAVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMergedForDisplaced','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMergedForDisplaced','QualityMasks' ),
    )

    process.HLTIterativeTrackingIteration1ForDisplaced = cms.Sequence(
        process.hltIter1ClustersRefRemovalForDisplaced+
        process.hltIter1MaskedMeasurementTrackerEventForDisplaced+
        process.hltIter1PixelLayerQuadrupletsForDisplaced+
        process.hltIter1PFlowPixelTrackingRegionsForDisplaced+
        process.hltIter1PFlowPixelClusterCheckForDisplaced+
        process.hltIter1PFlowPixelHitDoubletsForDisplaced+
        process.hltIter1PFlowPixelHitQuadrupletsForDisplaced+
        process.hltIter1PixelTracksForDisplaced+
        process.hltIter1PFLowPixelSeedsFromPixelTracksForDisplaced+
        process.hltIter1PFlowCkfTrackCandidatesForDisplaced+
        process.hltIter1PFlowCtfWithMaterialTracksForDisplaced+
        process.hltIter1PFlowTrackCutClassifierPromptForDisplaced+
        process.hltIter1PFlowTrackCutClassifierDetachedForDisplaced+
        process.hltIter1PFlowTrackCutClassifierMergedForDisplaced+
        process.hltIter1PFlowTrackSelectionHighPurityForDisplaced
    )

    process.hltIter1MergedForDisplaced = process.hltIter1MergedForBTag.clone(
        TrackProducers = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurityForDisplaced", "hltIter1PFlowTrackSelectionHighPurityForDisplaced"),
        selectedTrackQuals = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurityForDisplaced", "hltIter1PFlowTrackSelectionHighPurityForDisplaced")
    )

    process.hltIter2ClustersRefRemovalForDisplaced = process.hltIter2ClustersRefRemovalForBTag.clone(
        trajectories = cms.InputTag( "hltIter1PFlowTrackSelectionHighPurityForDisplaced" ),
        pixelClusters = cms.InputTag( "hltSiPixelClustersRegForDisplaced" ),
        oldClusterRemovalInfo = cms.InputTag( "hltIter1ClustersRefRemovalForDisplaced" ),
    )

    process.hltIter2MaskedMeasurementTrackerEventForDisplaced = process.hltIter2MaskedMeasurementTrackerEventForBTag.clone(
        src = cms.InputTag( "hltSiStripClustersRegForDisplaced" ),
        clustersToSkip = cms.InputTag( "hltIter2ClustersRefRemovalForDisplaced" )
    )

    process.hltIter2PixelLayerTripletsForDisplaced = process.hltIter2PixelLayerTripletsForBTag.clone(
        BPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0027 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalForDisplaced" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.006 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
        FPix = cms.PSet(
          hitErrorRPhi = cms.double( 0.0051 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalForDisplaced" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.0036 ),
          HitProducer = cms.string( "hltSiPixelRecHitsRegForDisplaced" )
        ),
    )

    process.hltIter2PFlowPixelTrackingRegionsForDisplaced  = process.hltIter2PFlowPixelTrackingRegionsForBTag.clone()
    process.hltIter2PFlowPixelTrackingRegionsForDisplaced.RegionPSet.measurementTrackerName = cms.InputTag( "hltIter2MaskedMeasurementTrackerEventForDisplaced" )

    process.hltIter2PFlowPixelClusterCheckForDisplaced = process.hltIter2PFlowPixelClusterCheckForBTag.clone(
        ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForDisplaced" ),
        PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForDisplaced" ),
    )

    process.hltIter2PFlowPixelHitDoubletsForDisplaced = process.hltIter2PFlowPixelHitDoubletsForBTag.clone(
        seedingLayers = cms.InputTag( "hltIter2PixelLayerTripletsForDisplaced" ),
        trackingRegions = cms.InputTag( "hltIter2PFlowPixelTrackingRegionsForDisplaced" ),
        clusterCheck = cms.InputTag( "hltIter2PFlowPixelClusterCheckForDisplaced" ),
    )

    process.hltIter2PFlowPixelHitTripletsForDisplaced = process.hltIter2PFlowPixelHitTripletsForBTag.clone(
        doublets = cms.InputTag( "hltIter2PFlowPixelHitDoubletsForDisplaced" )
    )

    process.hltIter2PFlowPixelSeedsForDisplaced = process.hltIter2PFlowPixelSeedsForBTag.clone(
        seedingHitSets = cms.InputTag( "hltIter2PFlowPixelHitTripletsForDisplaced" )
    )

    process.hltIter2PFlowCkfTrackCandidatesForDisplaced = process.hltIter2PFlowCkfTrackCandidatesForBTag.clone(
        MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEventForDisplaced" ),
        src = cms.InputTag( "hltIter2PFlowPixelSeedsForDisplaced" ),
    )

    process.hltIter2PFlowCtfWithMaterialTracksForDisplaced = process.hltIter2PFlowCtfWithMaterialTracksForBTag.clone(
        src = cms.InputTag( "hltIter2PFlowCkfTrackCandidatesForDisplaced" )
    )

    process.hltIter2PFlowTrackCutClassifierForDisplaced = process.hltIter2PFlowTrackCutClassifierForBTag.clone(
        src = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracksForDisplaced" )
    )

    process.hltIter2PFlowTrackSelectionHighPurityForDisplaced = process.hltIter2PFlowTrackSelectionHighPurityForBTag.clone(
        originalSource = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracksForDisplaced" ),
        originalMVAVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifierForDisplaced','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifierForDisplaced','QualityMasks' ),
    )

    process.HLTIterativeTrackingIteration2ForDisplaced = cms.Sequence(
        process.hltIter2ClustersRefRemovalForDisplaced+
        process.hltIter2MaskedMeasurementTrackerEventForDisplaced+
        process.hltIter2PixelLayerTripletsForDisplaced+
        process.hltIter2PFlowPixelTrackingRegionsForDisplaced+
        process.hltIter2PFlowPixelClusterCheckForDisplaced+
        process.hltIter2PFlowPixelHitDoubletsForDisplaced+
        process.hltIter2PFlowPixelHitTripletsForDisplaced+
        process.hltIter2PFlowPixelSeedsForDisplaced+
        process.hltIter2PFlowCkfTrackCandidatesForDisplaced+
        process.hltIter2PFlowCtfWithMaterialTracksForDisplaced+
        process.hltIter2PFlowTrackCutClassifierForDisplaced+
        process.hltIter2PFlowTrackSelectionHighPurityForDisplaced
    )

    process.hltIter2MergedForDisplaced = process.hltIter2MergedForBTag.clone(
        TrackProducers = cms.VInputTag("hltIter1MergedForDisplaced", "hltIter2PFlowTrackSelectionHighPurityForDisplaced"),
        selectedTrackQuals = cms.VInputTag("hltIter1MergedForDisplaced", "hltIter2PFlowTrackSelectionHighPurityForDisplaced"),
    )

    process.HLTIterativeTrackingIter12ForDisplaced = cms.Sequence(
        process.HLTIterativeTrackingIteration1ForDisplaced+
        process.hltIter1MergedForDisplaced+
        process.HLTIterativeTrackingIteration2ForDisplaced+
        process.hltIter2MergedForDisplaced
    )

    process.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexLowPt.tracks = tracks = cms.InputTag( "hltIter2MergedForDisplaced" )

    process.hltDisplacedhltIter4ClustersRefRemoval.trajectories = cms.InputTag( "hltIter2PFlowTrackSelectionHighPurityForDisplaced" )
    process.hltDisplacedhltIter4ClustersRefRemoval.pixelClusters = cms.InputTag( "hltSiPixelClustersRegForDisplaced" )
    process.hltDisplacedhltIter4ClustersRefRemoval.oldClusterRemovalInfo = cms.InputTag( "hltIter2ClustersRefRemovalForDisplaced" )

    process.hltDisplacedhltIter4MaskedMeasurementTrackerEvent.src = cms.InputTag( "hltSiStripClustersRegForDisplaced" )

    process.hltDisplacedhltIter4PFlowPixelLessClusterCheck.ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForDisplaced" )
    process.hltDisplacedhltIter4PFlowPixelLessClusterCheck.PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForDisplaced" )

    process.hltIter4MergedWithIter012DisplacedJets.TrackProducers = cms.VInputTag( 'hltIter2MergedForDisplaced','hltDisplacedhltIter4PFlowTrackSelectionHighPurity' )
    process.hltIter4MergedWithIter012DisplacedJets.selectedTrackQuals = cms.VInputTag( 'hltIter2MergedForDisplaced','hltDisplacedhltIter4PFlowTrackSelectionHighPurity' )

    process.HLT_HT430_DisplacedDijet40_DisplacedTrack_v13 = cms.Path(
        process.HLTBeginSequence+
        process.hltL1sVoHTT380+
        process.hltPreHT430DisplacedDijet40DisplacedTrack+
        process.hltPixelTrackerHVOn+
        process.hltStripTrackerHVOn+
        process.HLTAK4CaloJetsSequence+
        process.hltHtMht+
        process.hltHT430+
        process.hltEmFraction0p01To0p99CaloJetSelector+
        process.hltDoubleCentralCaloJetpt40+
        process.hltCentralCaloJetptLowPtCollectionProducer+

        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets+

        process.HLTIterativeTrackingIteration0ForDisplaced+

        process.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt+

        process.hltDisplacedHLTCaloJetCollectionProducerLowPt+

        process.HLTIterativeTrackingIter12ForDisplaced+

        process.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt+
        process.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt+
        process.HLTIterativeTrackingIteration4DisplacedJets+
        process.HLTDisplacedTrackRequirementDisplacedJetsLowPt+
        process.HLTEndSequence
    )

    process.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexMidPt.tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForDisplaced" )

    process.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexMidPt.tracks = cms.InputTag( "hltIter2MergedForDisplaced" )

    process.HLT_HT650_DisplacedDijet60_Inclusive_v13 = cms.Path(
        process.HLTBeginSequence +
        process.hltL1sVoHTT380 +
        process.hltPreHT650DisplacedDijet60Inclusive +
        process.hltPixelTrackerHVOn +
        process.hltStripTrackerHVOn +
        process.HLTAK4CaloJetsSequence +
        process.hltHtMht +
        process.hltHT650 +
        process.hltEmFraction0p01To0p99CaloJetSelector +
        process.hltDoubleCentralCaloJetpt60 +
        process.hltCentralCaloJetptMidPtCollectionProducer +
        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets +
        process.HLTIterativeTrackingIteration0ForDisplaced +
        process.HLT2PromptTrackRequirementIter0DisplacedJetsMidPt +
        process.hltDisplacedHLTCaloJetCollectionProducerMidPt +
        process.HLTIterativeTrackingIter12ForDisplaced +
        process.HLT2PromptTrackRequirementIter12DisplacedJetsMidPt +
        process.HLTEndSequence
    )

    process.HLT_HT500_DisplacedDijet40_DisplacedTrack_v13 = cms.Path(
        process.HLTBeginSequence +
        process.hltL1sVoHTT320orHTT340orHTT380 +
        process.hltPreHT500DisplacedDijet40DisplacedTrack +
        process.hltPixelTrackerHVOn +
        process.hltStripTrackerHVOn +
        process.HLTAK4CaloJetsSequence +
        process.hltHtMht +
        process.hltHT500 +
        process.hltEmFraction0p01To0p99CaloJetSelector +
        process.hltDoubleCentralCaloJetpt40 +
        process.hltCentralCaloJetptLowPtCollectionProducer +
        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets +
        process.HLTIterativeTrackingIteration0ForDisplaced +
        process.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt +
        process.hltDisplacedHLTCaloJetCollectionProducerLowPt +
        process.HLTIterativeTrackingIter12ForDisplaced +
        process.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt +
        process.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt +
        process.HLTIterativeTrackingIteration4DisplacedJets +
        process.HLTDisplacedTrackRequirementDisplacedJetsLowPt +
        process.HLTEndSequence
    )

    process.HLT_HT430_DisplacedDijet60_DisplacedTrack_v13 = cms.Path(
        process.HLTBeginSequence +
        process.hltL1sVoHTT380 +
        process.hltPreHT430DisplacedDijet60DisplacedTrack +
        process.hltPixelTrackerHVOn +
        process.hltStripTrackerHVOn +
        process.HLTAK4CaloJetsSequence +
        process.hltHtMht +
        process.hltHT430 +
        process.hltEmFraction0p01To0p99CaloJetSelector +
        process.hltDoubleCentralCaloJetpt60 +
        process.hltCentralCaloJetptMidPtCollectionProducer +
        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets +
        process.HLTIterativeTrackingIteration0ForDisplaced +
        process.HLT2PromptTrackRequirementIter0DisplacedJetsMidPt +
        process.hltDisplacedHLTCaloJetCollectionProducerMidPt +
        process.HLTIterativeTrackingIter12ForDisplaced +
        process.HLT2PromptTrackRequirementIter12DisplacedJetsMidPt +
        process.hltIter02DisplacedHLTCaloJetCollectionProducerMidPt +
        process.HLTIterativeTrackingIteration4DisplacedJets +
        process.HLTDisplacedTrackRequirementDisplacedJetsMidPt +
        process.HLTEndSequence
    )

    process.HLT_HT400_DisplacedDijet40_DisplacedTrack_v13 = cms.Path(
        process.HLTBeginSequence +
        process.hltL1sVoHTT380 +
        process.hltPreHT400DisplacedDijet40DisplacedTrack +
        process.hltPixelTrackerHVOn +
        process.hltStripTrackerHVOn +
        process.HLTAK4CaloJetsSequence +
        process.hltHtMht +
        process.hltHT400 +
        process.hltEmFraction0p01To0p99CaloJetSelector +
        process.hltDoubleCentralCaloJetpt40 +
        process.hltCentralCaloJetptLowPtCollectionProducer +
        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets +
        process.HLTIterativeTrackingIteration0ForDisplaced +
        process.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt +
        process.hltDisplacedHLTCaloJetCollectionProducerLowPt +
        process.HLTIterativeTrackingIter12ForDisplaced +
        process.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt +
        process.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt +
        process.HLTIterativeTrackingIteration4DisplacedJets +
        process.HLTDisplacedTrackRequirementDisplacedJetsLowPt +
        process.HLTEndSequence
    )

    process.HLT_HT550_DisplacedDijet60_Inclusive_v13 = cms.Path(
        process.HLTBeginSequence +
        process.hltL1sVoHTT380 +
        process.hltPreHT550DisplacedDijet60Inclusive +
        process.hltPixelTrackerHVOn +
        process.hltStripTrackerHVOn +
        process.HLTAK4CaloJetsSequence +
        process.hltHtMht +
        process.hltHT550 +
        process.hltEmFraction0p01To0p99CaloJetSelector +
        process.hltDoubleCentralCaloJetpt60 +
        process.hltCentralCaloJetptMidPtCollectionProducer +
        process.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets +
        process.HLTIterativeTrackingIteration0ForDisplaced +
        process.HLT2PromptTrackRequirementIter0DisplacedJetsMidPt +
        process.hltDisplacedHLTCaloJetCollectionProducerMidPt +
        process.HLTIterativeTrackingIter12ForDisplaced +
        process.HLT2PromptTrackRequirementIter12DisplacedJetsMidPt +
        process.HLTEndSequence
    )

    return process
