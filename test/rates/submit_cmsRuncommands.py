import htcondor
import os
from collections import deque

# files = ['/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/0244D183-F28D-2741-9DBF-1638BEDC734E.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/08D3F006-5E29-7945-B32A-CEF9CA8CA51E.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/0E3CB569-5250-5C4A-848A-1BDA2E32700B.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/102C594B-84FE-7540-AD4D-8BE75F1C8E9D.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/2EF1B5B0-1C31-1C4E-9876-5DC82E000465.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/311502E8-3FD3-204F-AC98-6F0A22F86812.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/3552E1AA-595B-FD48-B1B1-4977E2C10BA7.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/36EB9880-284A-9848-8AD2-5E065353EFB7.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/432749D4-9AEF-5845-B557-302884DC2B78.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/50A28BB4-3ACA-464F-A5E6-60F3D0062547.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/534721E2-EEBE-1F48-84AE-364F55A8CE1A.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/5AA70A8A-6807-0548-9E2E-99726A80C8B4.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/5FB1F56D-A583-3148-B634-06E37459CD87.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/6514D401-ECA9-8F48-B3C1-0ABB3AB99838.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/65EA98C3-88C1-5A43-8152-824F3169174E.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/6CB9E9DA-BEFE-3A4C-903A-C70BAC1542D6.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/720B4B82-1883-F84D-9016-6050BA9F7BB3.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7AAC7654-1C3C-1A40-BD82-7F92B899A048.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7F3D4F09-8335-7047-9420-0F8438E0C606.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/7F8818CF-AB9A-3847-B3B1-31175BC67EEA.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/839E1796-3459-6443-93CF-5B6DDED6ADD2.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/8F75E00C-8209-1A48-AEE8-F37A59D46FFB.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/9B8F48E7-8EB9-CA4E-B545-DDF63D28E4DB.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/A27DFA33-8FCB-BE42-A2D2-1A396EEE2B6E.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/AB95AEB0-C511-114C-B54C-9C0A9B78AF1E.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/AC589D97-A8ED-2B4C-B961-5595C88A8CEF.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/ADEDA3A0-2806-9840-8977-941CDDDEF4CC.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B14F28B7-490B-DA4E-8EA4-AF1B0C07756C.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B1D33CE9-6EDD-BF4C-9FF5-88956C5F7AA5.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B26AAAB6-F701-0C44-860E-CAB8EDC85876.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B71884AE-9951-FF47-915E-2C8C38421AF2.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/B7DBE80D-BF96-6744-BF0A-D7AE6BBE7077.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/BCAD5D59-5C76-9E47-8216-573FA32A7C6F.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C707212D-9264-0F43-9937-A0053CBFEDDE.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C8A17517-E49C-4149-8301-A9523DCF6094.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/C9B068C6-7C5E-5F4C-8556-33D138EB30CB.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/CA095F57-5636-6A4F-BD4B-A6C35C0BBD03.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D20C7DA2-996F-B54E-AAE0-DA110878E4BA.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/D5D2CF9C-2557-4243-B42E-4345100839DA.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/DA29E8B1-6A6A-214D-9405-4CD055D39303.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/DFBCDC7A-4389-9246-96EC-779943404AD1.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/E85A6840-68D8-E141-AAB8-BD6A05F7FE7F.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/F2293A8A-1B29-524B-895C-EFC12F58FF32.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/F83FFC16-0D3B-6E44-B744-29036A93DFCB.root',
#  '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/FBF117EE-5699-F147-BBFC-07815D5A2582.root']

files = ['/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/000C6613-1366-7142-9938-B5B40C2FAD80.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/09A6F74C-4A67-E848-8E7A-C1CC3F56771D.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/0A544437-C671-6941-8E72-AFF62E31F237.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/17ADD12B-52E2-8C4C-B375-8AF943A24212.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/1FE65F64-EB89-9C4B-AC4F-AD8DB687C31D.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/25FB46FF-4011-7F44-B02D-34F4726E389E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/2671C2B5-4F29-AB4A-82ED-8E9FE9B3A5D7.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/26EA44FE-9EE6-FC40-8EE5-7D4E1270F304.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/272D589A-97FA-584E-93A9-09A9341F6222.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/302D81E0-B4F5-9444-9402-82291E535E66.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/32042C72-F828-6245-AC14-6116403FF8B6.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/3B84AD3A-2D0A-5047-840B-414A2492C514.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/3B99362F-9509-A745-B1FC-C237A3CE07D0.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/3D6A6DEF-BE8E-7443-8CF4-1FD725F40FA2.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/53E150DE-BE01-8946-8E9E-8AC35901809E.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/6738A9FC-73D9-8548-A223-C1ECB7C83C1F.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/6BC1AD38-E884-DF4B-BBB0-D110821FD584.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/6BF65710-D026-B14D-95CE-D158621C67DD.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/6FCD4AD7-A6DC-6A48-9149-4470D12CE5CB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/739D902E-07E1-1047-965E-4691DA25760F.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/792C0C6A-6FF6-BE4F-B527-1298F7343881.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/7B06DB11-115D-A04F-A176-3F7756724270.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/7BAA37BF-A68F-564E-A56D-5CBFA2F58A4C.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/8680713A-343B-5647-8CA9-78B8310EE427.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/8C159F5E-D6B8-1945-86CF-0D942F48CFC6.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/90640A30-7265-4449-B5CE-C8D5F6A3D594.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/9578AF50-F84C-B24B-BF70-A40BA251A60D.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/95E652D9-2553-EA47-885C-5E2BCEEBDC2D.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/997298C0-91B8-3E44-B214-E5480EE71469.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/9CC0265A-FC66-1A47-AAD2-658B883299F2.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/9F11941B-D891-4840-9678-F0DAA706576F.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/A385342C-9A37-BB47-86C7-C7988E9B9CC8.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/A501FD83-1D65-674F-9BD2-8C727020B616.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/BB7B27CC-E1C0-344F-B26F-5E948952A41A.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/BEAACF89-97D1-4A4D-AC65-AA07C644D4A1.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/C12A0792-28A7-1D44-B2A8-B12F5003D5BF.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/C1A7FD48-D1F8-4440-BE12-A8C90ED8C7F8.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/C725ED13-935C-B740-8531-69C5E6DB5D4A.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/C904B2AD-A31A-204D-B77C-149D0F953CAB.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/CEE109D5-57F1-1040-9102-7B2E06042E67.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/E32A97C5-75AB-7944-A4C4-8DB58B474E45.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/E8C4D551-2426-9542-9DEB-923B557416C4.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/E9AF0733-4D1F-2744-B6F4-34A51B412348.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/EB19BF02-E042-F540-A730-2CAF16BDEE01.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/F52E90B1-5BF5-134C-8D93-040428544570.root',
 '/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/F590E530-00C9-9B4D-A1E2-59E9879FE091.root']

out_dir = "wp_out/production_21"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(f"{out_dir}/logs", exist_ok=True)
job_queue = deque()

for i, file in enumerate(files):
    executable = "export X509_USER_PROXY=/afs/desy.de/user/n/neich/.vomsproxy/x509 && /cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_3_0_pre6/bin/slc7_amd64_gcc10/cmsRun hltResults_cfg_WP.py lumis=lumi_sections_323775.txt output={0}/output_{1:02d}.root dumpPython={0}/dump_{1:02d} inputFiles={2}".format(out_dir, i, file)
    # executable = "/usr/bin/env touch {0}/test_{1:02d}".format(out_dir, i)

    hostname_job = htcondor.Submit({
        "executable": executable,
        "output": "{0}/logs/job_{1:02d}.out".format(out_dir, i),
        "error": "{0}/logs/job_{1:02d}.err".format(out_dir, i),
        "log": "{0}/logs/job_{1:02d}.log".format(out_dir, i),
        "request_cpus": 1,
        "request_memory": "1GB",
        "getenv": True,
        # "JobFlavrour": "microcentury",
        # "MaxRuntime": int( 3600 * 2),
        # "use_x509userproxy": True,
        # "x509userproxy": "/afs/desy.de/user/n/neich/.vomsproxy/x509"
    })
    job_queue.append(hostname_job)

schedd = htcondor.Schedd()
results = deque()
# import subprocess
for i, job in enumerate(job_queue):
    print("submitting file {0:2d}".format(i))
    results.append( schedd.submit(job) )
    # print("executing locally")
    # subprocess.run(job, shell=True)
