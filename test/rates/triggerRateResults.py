import argparse
import os
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_file', type=str,
                    help='an integer for the accumulator')
parser.add_argument('output_dir', type=str,
                    help='an integer for the accumulator')

args = parser.parse_args()

path_dict = {}


with open(args.input_file, "r") as in_file:
    lines = [line.rstrip() for line in in_file]

def fil(line):
    return list(filter(('').__ne__, line.replace(" ", "").split("|")))

keys = fil(lines[0])

path_dict["DeepCSV"] = defaultdict(list)
path_dict["DeepJet"] = defaultdict(list)

for line in lines[1:]:
    d = dict(zip(keys, fil(line)))
    if ("DeepCSV" in d["trigName"]):
        trigName_base = d["trigName"].split("_WP_")
        path_dict["DeepCSV"][trigName_base[0]].append(d)
    elif ("DeepJet" in d["trigName"]):
        trigName_base = d["trigName"].split("_WP_")
        path_dict["DeepJet"][trigName_base[0]].append(d)

"""

Plotting

"""

import matplotlib
import matplotlib.pyplot as plt
import mplhep as hep       
matplotlib.use('Agg')
plt.style.use(hep.style.ROOT)

larger = 28 
large = 26
med = 20

_params = {
	"axes.titlesize": larger,
	"legend.fontsize": med,
	"figure.figsize": (16, 10),
	"axes.labelsize": larger,
	"xtick.labelsize": large,
	"ytick.labelsize": large,
	"figure.titlesize": large,
	"xtick.bottom": True,
	"xtick.direction": "in",
	"ytick.direction": "in",
	"xtick.major.size": 12,
	"ytick.major.size": 12,
	"xtick.minor.size": 8,
	"ytick.minor.size": 8,
	"ytick.left": True,
}
plt.rcParams.update(_params)

"""
DeepCSV
"""
tag = "DeepCSV"
out = os.path.join( args.output_dir, tag)
os.makedirs(out)

for base_path, path_list in path_dict[tag].items():
    wps =  []   
    rates = []
    for path in path_list:
        try:
            wps.append( float(path["trigName"].split("_WP_")[1])/100)
            rates.append(float(path["rateRaw"]))
        except IndexError:
            pass
    print("- - "*20)
    print(base_path)
    print(wps)
    print(rates)

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    hep.cms.label(data=True, loc=1, lumi=1.713e34, year=2018)
    ax.set_xlabel(f"working point")
    ax.set_ylabel("rate")
    # ax.set_xlim(0., 1.)
    ax.set_ylim(0., 1.1*max(rates))
    ax.plot(wps, rates, marker="o", linestyle="dashed", label=base_path)
    ax.legend()
    fig.savefig(os.path.join(out, f"{base_path}.png"))


"""
DeepJet
"""
tag = "DeepJet"
out = os.path.join( args.output_dir, tag)
os.makedirs(out)

for base_path, path_list in path_dict[tag].items():
    wps =  []   
    rates = []
    for path in path_list:
        try:
            wps.append( float(path["trigName"].split("_WP_")[1])/100)
            rates.append(float(path["rateRaw"]))
        except IndexError:
            pass
    print("- - "*20)
    print(base_path)
    print(wps)
    print(rates)

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    hep.cms.label(data=True, loc=1, lumi=1.713e34, year=2018)
    ax.set_xlabel(f"working point")
    ax.set_ylabel("rate")
    # ax.set_xlim(0., 1.)
    ax.set_ylim(0., 1.1*max(rates))
    ax.plot(wps, rates, marker="o", linestyle="dashed", label=base_path)
    ax.legend()
    fig.savefig(os.path.join(out, f"{base_path}.png"))
