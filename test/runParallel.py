import os
import subprocess
import filecmp
import glob
import multiprocessing

def subprocessWrapper(c):
    subprocess.call(c, shell=True)

MINIAODInputFiles = [
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/FlatPU30to80_112X_mcRun3_2021_realistic_v16-v2/110000/4edf2114-0dc8-4277-95c5-e55989d35c9e.root",
    # "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/4bce3e17-c44a-492a-b052-a2f54bf78f23.root",
]

HLTInputFiles = [
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
    "/store/mc/Run3Winter21DRMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/140000/9c37be55-f5ee-4fb3-92c3-5c7d0e31508a.root",
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

offpath = "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/ParkingForPNFS/MINIAODSIM/"
path = "/pnfs/desy.de/cms/tier2/store/user/sewuchte/BTagServiceWork/Run3/ParkTTbar/MINIAODSIM/"

HLTInputFiles = ["file://"+path+f.split("/")[-1] for f in HLTInputFiles]
MINIAODInputFiles = ["file://"+offpath+f.split("/")[-1] for f in MINIAODInputFiles]

HLT_recos = [
            "HLT_GRun",
            "HLT_GRun_PatatrackQuadruplets",
            "HLT_GRun_PatatrackTriplets",
            # "HLT_Run3TRK",
            # "HLT_Run3TRKPixelOnly",
            # "HLT_Run3TRKPixelOnlyCleaned",
            # "HLT_Run3TRKPixelOnlyCleaned2",
            # "HLT_Run3TRKPixelOnlyCleaned3",
            # "HLT_Run3TRKPixelOnlyCleaned4",
            # "HLT_Run3TRKForBTag",
            # "HLT_Run3TRKForBTag_2",
            # "HLT_Run3TRKForBTag_3",
            # "HLT_Run3TRKForBTag_Pt"
            ]

executableHLT = "cmsRun runHLTBTagAnalyzer_cfg.py defaults=Run3 reco=RECOKEY runOnData=False outFilename=OUTNAME globalTag=120X_mcRun3_2021_realistic_v4"
executable = "cmsRun runBTagAnalyzer_cfg.py defaults=Run3 runOnData=False outFilename=OUTNAME"


commandListHLT = []
for reco in HLT_recos:
    outfolderHLT = "OutputOnline_"+reco+"/"
    if not os.path.exists(outfolderHLT):
        os.makedirs(outfolderHLT)
    for i,file in enumerate(HLTInputFiles):
        commandString = executableHLT.replace("OUTNAME",outfolderHLT+"/HLTNtuple_"+str(i)+".root").replace("RECOKEY",reco)
        commandString = commandString+" inputFiles="+file
        commandListHLT.append(commandString)


# commandListHLT_pt = []
# for reco in HLT_recos:
#     for pt in ["0.9","1.2","1.5","2."]:
#         outfolderHLT = "OutputOnline_"+reco+"_"+pt+"/"
#         if not os.path.exists(outfolderHLT):
#             os.makedirs(outfolderHLT)
#         for i,file in enumerate(HLTInputFiles):
#             commandString = executableHLT.replace("OUTNAME",outfolderHLT+"/HLTNtuple_"+str(i)+".root").replace("RECOKEY",reco)
#             commandString = commandString+" inputFiles="+file
#             commandString = commandString+" ptMinThreshold="+pt
#         commandListHLT_pt.append(commandString)


commandListOff = []
outfolder = "OutputOffline/"
if not os.path.exists(outfolder):
    os.makedirs(outfolder)
for i,file in enumerate(MINIAODInputFiles):
    commandString = executable.replace("OUTNAME",outfolder+"/Ntuple_"+str(i)+".root")
    commandString = commandString+" inputFiles="+file
    commandListOff.append(commandString)

# print commandListHLT
# print commandListHLT[0]
# print commandListOff[0]
# print len(commandListHLT)

commandList = commandListHLT+commandListOff
# commandList = commandListHLT
# commandList = commandListOff
# print (commandList)
print len(commandList)

# p = multiprocessing.Pool(20)
# p.map(subprocessWrapper, commandList)


# haddPath = "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/11_08_21_First12X/"
haddPath = "/nfs/dust/cms/user/sewuchte/BTV/Run3/nTuples/11_10_21_12X/"

for reco in HLT_recos:
    infolderHLT = "OutputOnline_"+reco+"/"
    haddcommand = "hadd -f "+haddPath+"/ttbar_"+reco+".root "+infolderHLT+"*.root"
    print haddcommand
    subprocessWrapper(haddcommand)

haddcommandOff = "hadd -f "+haddPath+"/ttbar_Offline.root OutputOffline/*.root"
print haddcommandOff
subprocessWrapper(haddcommandOff)
