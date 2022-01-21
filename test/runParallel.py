import os
import subprocess
import filecmp
import glob
import multiprocessing

def subprocessWrapper(c):
    subprocess.call(c, shell=True)

MINIAODInputFiles_old = [
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4edf2114-0dc8-4277-95c5-e55989d35c9e.root",
]

HLTInputFiles_old = [
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/a32ce6ba-6c9f-408e-9e3f-d9a93712c215.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140001/1c2e04fc-3ecc-4c34-a5a4-388d1a137530.root",

    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/40a66eee-8c49-4ca1-a5f6-73012543f72f.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/5b3dcd6c-99af-4c06-a447-10394b1fbd33.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/6cb2c3f8-1355-45c6-b0bc-9b14f2dcee21.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/743105e7-5848-4f04-9e58-8ea32e7b77e6.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/95153321-49f1-44f8-8b9d-f4fbd08306c5.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/9be50047-83df-4e55-abfe-a69a036c7cee.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/f030184d-7b2b-42db-b160-e16fa55cc255.root",

    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/052ece05-ff48-4fe7-9fdc-d4290f0b1d0b.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/8c918936-49b8-4a0d-907c-d8e9d2a29a36.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/a1b770d3-bf98-468f-bce4-057f0f4ce001.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/aa7e98fe-ddbc-415f-afeb-0bc5f9492cd6.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/dab63b08-97ec-4c1f-ae5a-8da6847f095c.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/edaa7369-785c-4f2b-866d-e4b68994f4c7.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/fd6c9b98-eb10-4b17-97fe-87814ac82c17.root",

    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/2c5880e9-81b8-4ec1-8e34-31764390592d.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/57aafa00-4aa6-4b52-9f7a-dcf93808dc05.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/5f409ffb-ef07-4825-944a-10982d1f7595.root",
    # "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/9c37be55-f5ee-4fb3-92c3-5c7d0e31508a.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/b71f8b97-5831-4602-a157-5aeefa1c7b36.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/cfea9793-91e8-415e-859a-afb876bad76b.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/fff0d30c-e551-4866-b236-391f1e5ef906.root",

    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/163c2e4f-6bbf-42e4-b385-1a21a4dc2070.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/2eb81a25-273d-4706-b986-866a39845097.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/47ec003d-00cd-4432-997c-983585ee3483.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/4ba0fbb9-99b5-45e2-bb17-e5829461c579.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/662543a5-7928-4b23-abf4-d97657cbe63e.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/7d970a90-b490-47c3-857b-b27521da3eb8.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/ddc6fee6-6f9a-4d3b-af15-c229684a39b6.root",

    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/56afbbd8-ffeb-4dcc-8e7c-5fe60b4ea1f6.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/7ff7ad0f-36c4-411d-b889-df8623a1dbf0.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/b59b4429-e89c-47c7-9711-1c855acedd16.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/c9b5efaf-8a64-497c-a1a1-75020b41f6db.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/e7d89bb3-c588-4697-bdf5-d59177fd5443.root",
]

MINIAODInputFiles = {
    # "QCD20t30": [],
    "QCD30t50": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/MINIAODSIM/rndm_120X_mcRun3_2021_realistic_v5-v2/2550000/003f68ab-1291-4be8-b8a5-a75753ac670e.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/MINIAODSIM/rndm_120X_mcRun3_2021_realistic_v5-v2/2550000/01416bc9-85d2-4200-a5bd-aa4b3aca9166.root"
    ],
    "QCD50t80": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/04a66f4c-bd35-4766-9ac5-23011b257e5d.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/05995e59-1a66-420b-849d-78069c35b4b2.root"
    ],
    "QCD80t120": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/061d37c9-b61f-455d-8389-c2d88568cd1f.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/0e067339-4d92-432d-bf33-a2b7ba69e011.root"
    ],
    "QCD120t170": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/12a105fd-be75-4621-bcfd-a2236c2f6e1f.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/1c709f11-747a-4dc0-b864-45e045d002a9.root"
    ],
    "QCD170t300": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/0e21d3d4-eb92-4986-a682-8daf75e4d64b.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/23235054-b81e-4616-a49d-947c99ecf9a8.root"
    ],
    "QCD300t470": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/1fa7f8e0-2509-4f8a-8f28-32575102f391.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2550000/099d51de-b2fb-49e4-a996-77208a898ae0.root"
    ],
    "QCD470t600": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/040930ad-0cbd-4031-8c88-1c0eda5d6dda.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/222e3c6d-c6e0-4fd8-b503-212ae27e2ea6.root"
    ],
    "QCD600tInf": [
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/0297809a-e833-4056-a31d-3e362d83cd71.root",
        "/store/mc/Run3Summer21MiniAOD/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/02a2cb85-310f-42f8-98f9-574ca60b2ea9.root"
    ],
    "TTbar": [
        "/store/mc/Run3Summer21MiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/0a20560f-7b78-41b3-bd7f-85cc6ecbcfc8.root",
        "/store/mc/Run3Summer21MiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/08e8191a-a2de-4237-a47b-780a743b875b.root",
        "/store/mc/Run3Summer21MiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/120X_mcRun3_2021_realistic_v5-v2/2540000/07abdc05-16f2-4ff8-9a32-a2448d160497.root"
    ],
}

HLTInputFiles = {
    # "QCD20t30": [],
    "QCD30t50": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550003/ce8e8df7-02de-45be-af18-89332b261d0e.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/59bb199e-7eea-4bce-943f-62e2393318c6.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/5a3ee565-6d2e-4306-9004-c2b10fdf4da7.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/6df770fd-40b6-4faf-99aa-82bd2103d6a0.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/d4b3e77a-349c-4142-917b-6ba787e16578.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/fa32c8d3-f97c-45cb-b46a-6bf9d5d406ae.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550004/26f9cc53-51e0-4b61-ac33-1ad3715154aa.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550004/e89f06b0-a4d5-48a2-a302-033f57a5bbcb.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/3a9922ed-481e-4300-a27e-ef08d36fe16a.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/523d0d9e-f5ca-4a32-8727-f3e762a868da.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/6f2322eb-02ac-4789-aaf8-9513e9b343b8.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550005/d00fb40d-b58b-4d32-9a3f-038bde6884ef.root"
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/084a7bcb-3e4d-478e-aac8-54b3b709c21d.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/55ca36b1-d325-4601-ad27-c0f26ac41355.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/853f8f28-a26c-4ddf-aefe-841744ca60e3.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/9999d4ec-503d-4740-a5d9-91341eb112b7.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/36d9d3a8-ed31-4dc8-a5cd-b6e710fc4cb1.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/5799c5c9-b52a-47cf-aac1-9512c70ddf11.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/7626e545-4708-4a1f-b48e-d45e7741ab48.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/d2cb993c-0899-49cf-98fc-6286d1eb2ec6.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/e674a02f-b75a-411e-876c-68fa8be124d1.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt_30to50_TuneCP5_14TeV_pythia8/GEN-SIM-DIGI-RAW/rndm_120X_mcRun3_2021_realistic_v6-v2/2550002/f2bfa42c-4280-4477-bb5c-f3b8f5c75d09.root"
    ],
    "QCD50t80": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/66530973-0001-4659-868a-df38b14f3628.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/47907964-4532-4fd5-a846-ea7ef2960453.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/6ba5961a-55ab-4d9e-9bea-89c49420155b.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/8c7b2014-f218-448a-8be1-6fd5c98ef26c.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/fc8f1c2e-8bf7-4cc0-9761-ef50543d0fde.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/54195af8-9828-4e9f-abe7-6fff3e6ca6fe.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/579192e6-776e-4139-aa15-029b7a90ded5.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/8251760f-7197-4bb6-914d-afaa136686a5.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/d3d82f2f-8a05-4ce0-af90-59ce0efc7d1d.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/f228d6c0-1add-4f9e-abcc-74cdc7ab9256.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/099f7dff-2a51-4395-b701-9af5663d3cd7.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/58b7d933-2e74-447c-8368-b057a704b7dc.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/a9f784c0-43c4-4ba9-b76a-75542fc4be59.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/b8edbc91-275a-42d1-a2cc-6d98c3f321cb.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/13bea97a-7d08-4f83-a0e9-a0722c3cea36.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/46931566-5015-4d04-99c9-37a8cb957eb1.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/d289284c-2d61-4389-a287-6136e54c27f2.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/6d05b47b-4f7f-4b9b-903c-5ac97164323b.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/e8ce2ee5-a43c-4306-a7b2-043cacb987ce.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/ed528b7b-d722-41a8-832a-f872d482cf62.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/40d98eef-53e7-490f-acb5-bcf1e7b38b78.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/b3b73ee4-470a-481e-8d31-86778aee8482.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/c55edc4d-2b9a-402c-9ea6-916d1967e5e2.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/ca776840-9448-41cb-957d-42fbee0832fd.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-50To80_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/f0e771f8-efa8-4512-9393-e4606fb2dc95.root",
    ],
    "QCD80t120": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/9f9752af-147f-473e-868e-079f0e3b9c09.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/e6652670-58b6-4926-abb4-4b52ac319379.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/a9594fb6-42a3-4ff6-85ed-e469b723293a.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/c3ca27f2-7edf-4a29-b4ee-0f68560ca6c0.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/9a341077-1ee1-42e1-9d6a-b98832aa6aec.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/f28ffe7f-1f1a-40c6-9cc0-0c7b6d3595d7.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/204704a9-f285-4b11-8097-bb14e25a1312.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/31d89b31-e1fb-45f8-a4d1-52832a3ac8f1.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/8b4f3dbd-fe15-4db3-bb02-0d45f372b5c6.root"
    ],
    "QCD120t170": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/0d5149d8-98e7-4d8c-abc0-4839f2371ea8.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/212ce2aa-4c5d-490b-a447-28123775abb6.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/9f79036e-ee1a-456e-ae31-da891b57b15f.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/eb72edde-bbbe-4789-9775-c915f6f0842b.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/a6fb8ba3-b6f2-4195-a39a-9cfa86872b08.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/d869d89d-0b3a-4b89-85af-5baacfe7ef9a.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/d8cc5d57-015b-4151-8d34-01331b9998db.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/da437a9b-f82f-42c8-b16c-cd372e7989d5.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/ff0f3582-c99e-44e7-be8b-a5281a4da57c.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/8d1dff57-6a4c-4dc3-9553-e452716dfd8f.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/97e31a17-649b-4976-b87a-c555dfec6277.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/07a38352-0f2b-424f-baea-fb21ba50d575.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/3a62c9e1-0c91-4f2e-9cfe-7f9ff7099a80.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/2dea25ca-1ae7-4dd4-bfcc-55a6b3860690.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/e3ed11b1-e776-4e18-bc77-895b9b7d710a.root"
    ],
    "QCD170t300": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/b41862e7-d1f4-4dec-a917-ce7c238111da.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/13e81058-c142-4bf3-ae90-1c2c43dc2edb.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/39133dd0-8daa-4305-b2ca-e457da402c67.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/96ff521b-dcfa-4557-b4d8-0d414ff2fb7d.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/b5389b69-fa7b-46be-983e-5729692f5440.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/f964fd45-2680-4d00-986c-ac13ec2dd849.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-170To300_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/2ec79da6-f15b-465e-92ac-f6d07fef4a92.root",

    ],
    "QCD300t470": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/09be9cf7-2614-4ce6-8c55-81585165c218.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/81d0e447-78bd-457e-beaf-e010ab7e013e.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/4db886c4-c1b1-4888-8977-7733edc74104.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/83b9b202-12cd-498d-8548-c1e07d192e48.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550000/b4f7b1ab-067b-4018-8af1-82d23da23262.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/bb0309c5-b83b-4599-b1bd-7778d90dd392.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-300To470_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2550001/1779228f-d32e-484d-be69-465fff0b8b39.root"
    ],
    "QCD470t600": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540001/0572a329-6f03-4b2b-bf58-0790811c06a9.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540001/1657b710-8491-4782-a4fa-0ce27fe71922.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540001/3abf94d3-eda7-479d-a912-dc21a38fac62.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/8054916c-e760-4b9d-898a-a51dda7842b0.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/cc259889-1eec-4fbd-ac73-c4fb458f0728.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540001/35728559-2b32-45ab-88eb-c5277e614762.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/0fe2eec9-0ef2-468e-b010-39dee14caa1b.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/34848dab-cfe5-465f-bd6a-8975aa0dccd4.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-470To600_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/43df50de-f860-45a4-99de-ed5b4ba15156.root"
    ],
    "QCD600tInf": [
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/6b9bd79e-31f7-4422-95ff-4c23971194e2.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540001/8070f1f1-1282-4cfd-b24f-32f51559f10a.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/86a6726a-034e-4723-a999-da6cf0a7e358.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/c3aa540c-efa2-4db8-8206-fd9e4f1204d9.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/de1c8fd3-def2-4149-b970-6e4363319f42.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/36a557eb-6a31-4b50-8748-fec116d95f0e.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/4aec61ea-fe65-4f41-b687-d2700504bd5d.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/97ab081a-ed41-43d2-ab77-afd87f25ac08.root",
        "/store/mc/Run3Summer21DRPremix/QCD_Pt-600ToInf_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/9d7350bb-5866-4e21-936c-071ce9273b20.root"
    ],
    "TTbar": [
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/4956b6d5-c281-4dd7-b5be-aa07ced8ed3e.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/7288504c-465e-440c-b760-63f7a4e46794.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/d7d3a566-3ebc-4b93-9d00-f0fa37df23ff.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/f5c0d580-4442-4d56-bd1b-07fa6fcaba11.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/f77e03b8-1749-47df-a61f-6d9d68b2357d.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/060b9f2d-0a6c-47ae-af26-37c44434c0fc.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/533ed2f4-74ff-48af-b1f4-9b082594ea38.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/c89ec8ed-e178-4ad7-9db6-090312c9b130.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/2dc0e982-7314-4626-945d-43853da72ed1.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/5e698458-be67-449d-9530-e616163d0a50.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/8793cf37-debf-4393-bb66-bedaefcc163e.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/9b260275-fcc9-4cac-8750-8e921ce538e2.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/24718675-e96d-4965-b4ba-252297804e6e.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/852e1fbe-a2ba-4282-817d-02f18263b21d.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/8da5a334-2a9e-4a40-a6fe-6d59044e58fe.root",
        "/store/mc/Run3Summer21DRPremix/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/120X_mcRun3_2021_realistic_v6-v2/2540000/e9312be6-b1c9-4979-8947-1c4d7e3f93bc.root"
    ],
}

HLT_recos = [
            "HLT_Run3TRK_ROICaloGlobalPF_Mu",
            ]

executableHLT = "cmsRun runHLTBTagAnalyzer_cfg.py defaults=Run3 reco=RECOKEY runOnData=False outFilename=OUTNAME"
executable = "cmsRun runBTagAnalyzer_cfg.py defaults=Run3 runOnData=False outFilename=OUTNAME"


commandListHLT = []
for reco in HLT_recos:
    for sample in HLTInputFiles:
        outfolderHLT = "OutputOnline_"+reco+"/"+sample+"/"
        if not os.path.exists(outfolderHLT):
            os.makedirs(outfolderHLT)
        for i,file in enumerate(HLTInputFiles[sample]):
            commandString = executableHLT.replace("OUTNAME",outfolderHLT+"/HLTNtuple_"+str(i)+".root").replace("RECOKEY",reco)
            commandString = commandString+" inputFiles="+file
            commandListHLT.append(commandString)


commandListOff = []
outfolder = "OutputOffline/"
if not os.path.exists(outfolder):
    os.makedirs(outfolder)
for i,file in enumerate(MINIAODInputFiles):
    commandString = executable.replace("OUTNAME",outfolder+"/Ntuple_"+str(i)+".root")
    commandString = commandString+" inputFiles="+file
    commandListOff.append(commandString)

# commandList = commandListHLT+commandListOff
commandList = commandListHLT
# commandList = commandListOff
print (commandList)
print (len(commandList))

p = multiprocessing.Pool(20)
p.map(subprocessWrapper, commandList)

haddPath = "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/21_01_22_CMSSW_12_3_X/"

if not os.path.exists(haddPath):
    os.makedirs(haddPath)

for reco in HLT_recos:
    for sample in HLTInputFiles:
        infolderHLT = "OutputOnline_"+reco+"/"+sample+"/"
        haddcommand = "hadd -f "+haddPath+"/"+sample+"_"+reco+".root "+infolderHLT+"*.root"
        print (haddcommand)
        subprocessWrapper(haddcommand)

# haddcommandOff = "hadd -f "+haddPath+"/ttbar_Offline.root OutputOffline/*.root"
# print (haddcommandOff)
# subprocessWrapper(haddcommandOff)
