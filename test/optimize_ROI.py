import numpy as np
from skopt import BayesSearchCV
import subprocess
import json
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import euclidean_distances
from skopt.space import Real, Categorical, Integer
import os

targets = [
    0.7,
    0.8,
    4,
    4,
    2.1,
    0.1,
    0.22,
    0.1,
    0.7,
    0.4,
]


class TemplateClassifier(BaseEstimator):
    def __init__(
        self,
        deltaEta=0.5,
        deltaPhi=0.5,
        maxNRegions=8,
        maxNVertices=2,
        nSigmaZBeamSpot=3.0,
        nSigmaZVertex=0.0,
        originRadius=0.3,
        ptMin=0.8,
        zErrorBeamSpot=0.5,
        zErrorVetex=0.3,
    ):
        self.deltaEta = deltaEta
        self.deltaPhi = deltaPhi
        self.maxNRegions = maxNRegions
        self.maxNVertices = maxNVertices
        self.nSigmaZBeamSpot = nSigmaZBeamSpot
        self.nSigmaZVertex = nSigmaZVertex
        self.originRadius = originRadius
        self.ptMin = ptMin
        self.zErrorBeamSpot = zErrorBeamSpot
        self.zErrorVetex = zErrorVetex

        self._short_hash = str(hash(self))[0:15]
        self._fname = "opt_results/HH_HLT_Run3TRK_ROICaloROIPF_22_{}.log".format(self._short_hash)
        self._config_path = "opt_results/config_{}.json".format(self._short_hash)

        os.makedirs("opt_results", exist_ok=True)

    def run_cmssw_command(self, output_hash, fname):
        # files="\
        #     root://xrootd-cms.infn.it//store/mc/Run3Winter21DRMiniAOD/GluGluToHHTo4B_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/130000/008cdc6a-f340-488a-994b-ad0a366bb554.root,\
        #     root://xrootd-cms.infn.it//store/mc/Run3Winter21DRMiniAOD/GluGluToHHTo4B_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/130000/018caa66-83c3-4535-bd31-4af4ff5476fa.root,\
        #     root://xrootd-cms.infn.it//store/mc/Run3Winter21DRMiniAOD/GluGluToHHTo4B_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/130000/01f42c32-32fe-4cd3-b44e-88b350521e99.root"

        with open(self._config_path, "w") as f:
            json_config = json.dump(self.get_params(), f)

        files="\
            file:///nfs/dust/cms/user/sewuchte/ForNiclas/HH/018caa66-83c3-4535-bd31-4af4ff5476fa.root,\
            file:///nfs/dust/cms/user/sewuchte/ForNiclas/HH/06fc95e7-a2d7-4bbd-8440-ce57f4298131.root,\
            file:///nfs/dust/cms/user/sewuchte/ForNiclas/HH/045537d7-6d4b-4458-bc5b-5941a66d894d.root"
        args = [
            "cmsRun",
            "runHLTPaths_HHStudy_cfg.py",
            "reco=HLT_Run3TRK_ROICaloROIPF_Mu_optimized",
            "runOnData=False",
            'inputFiles={}'.format(files),
            "numStreams=4",
            "numThreads=4",
            "maxEvents=-1",
            "globalTag=122X_mcRun3_2021_realistic_v1",
            "runTiming=True",
            "dumpPython=opt_results/testdump_{}.py".format(output_hash),
            "loadROIparamsJson={}".format(self._config_path)
            # ">",
            # "{}".format(fname, output_hash),
        ]
        print("Running:")
        print(" ".join(args))
        finished_proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        with open(fname, "w") as f:
            f.write(finished_proc.stdout.decode("utf-8"))

    def fit(self, X, y):

        check_X_y(X, y)

        # self._fname = "/tmp/results_{}.txt".format(self._short_hash)

        random_score = np.random.uniform(0, 1)
        self.run_cmssw_command(self._short_hash, self._fname)
        # args = ["python3", "test_executable.py", "{}".format(random_score), self._fname]

        # subprocess.run(args)

        return self

    def score(self, X, y=None):

        with open(self._fname, "r") as f:
            result = f.read()

        self._result_name = "opt_results/results_{}.txt".format(self._short_hash)

        match = result.find("0 hltSelector6PFJetsROIForBTag")
        line_begin = result[:match][::-1].find("\n")
        lines = result[match-line_begin:].split("\n")[0:2]

        entries = [a for a in lines[0].split(' ') if a != '']
        score = float(entries[3])

        lines = result.split("\n")
        hits = 0
        for i,line in enumerate(lines):
            if "HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v8" in line:
                hits += 1
            if hits ==5:
                target_line = i
                break

        time_score = float([a for a in line.split(' ') if a != ''][1])
        score_time = -50. * time_score

        final_score = score+score_time

        # enter embed here to test Stuff for reading out the files

        with open(self._result_name, "w") as f:
            f.write("Score: {0:1.8f}\n".format(final_score))
            f.write("TimeScore: {0:1.8f}\n".format(score_time))
            f.write("EffScore: {0:1.8f}\n".format(score))
            params = "\n".join( [ "{0}:\t{1:2.6f}".format(key, val) for key, val in self.get_params().items()])
            f.write(params)

        return final_score

    def predict(self, X, y=None):
        return X


def run_optimization_test():

    N_iter = 100
    # log-uniform: understand as search over p = exp(x) by varying x
    opt = BayesSearchCV(
        TemplateClassifier(),
        {
            "deltaEta": Real(0.0, 4.0, prior="uniform"),
            "deltaPhi": Real(0.0, 4.0, prior="uniform"),
            "maxNRegions": Integer(2, 100),
            "maxNVertices": Integer(1, 5),
            "nSigmaZBeamSpot": Real(0.0, 30.0, prior="uniform"),
            "nSigmaZVertex": Real(-1.0, 1.0, prior="uniform"),
            "originRadius": Real(0.0, 1.0, prior="uniform"),
            "ptMin": Real(0.0, 2.0, prior="uniform"),
            "zErrorBeamSpot": Real(0.0, 1.0, prior="uniform"),
            "zErrorVetex": Real(0.0, 1.0, prior="uniform"),
        },
        n_iter=N_iter,
        cv=[(slice(None), slice(None))],
        verbose=1,
        # scoring="accuracy"
    )

    opt.fit(np.zeros((100, 1)), np.zeros((100)))

    print("After {} iterations:".format(N_iter))
    print("val. score: %s" % opt.best_score_)
    print("test score: %s" % opt.score(0.0, 0.0))
    print("Final params:")
    params = opt.best_estimator_.get_params()
    for i, (param, val) in enumerate(params.items()):
        print("{0}:\t{1:2.2f} vs {2:2.2f}".format(param, val, targets[i]))

    # print(opt.get_params(deep=True))


if __name__ == "__main__":
    run_optimization_test()
