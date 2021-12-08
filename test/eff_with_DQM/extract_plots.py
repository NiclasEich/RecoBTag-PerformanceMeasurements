from ROOT import *
import os

f = TFile("DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root")


folder_BTagDiMu_Jet = ["BTagDiMu_Jet/BTagMu_AK8Jet170_DoubleMu5/"]

folder_BTagMu_DiJet = ["BTagMu_DiJet/BTagMu_AK4DiJet20_Mu5/", "BTagMu_DiJet/BTagMu_AK4DiJet40_Mu5/", "BTagMu_DiJet/BTagMu_AK4DiJet70_Mu5/", "BTagMu_DiJet/BTagMu_AK4DiJet110_Mu5/", "BTagMu_DiJet/BTagMu_AK4DiJet170_Mu5/", "BTagMu_DiJet/BTagMu_AK8DiJet170_Mu5/"]

folder_BTagMu_Jet = ["BTagMu_Jet/BTagMu_AK4Jet300_Mu5/", "BTagMu_Jet/BTagMu_AK8Jet300_Mu5/"]

for i in range(0,len(folder_BTagDiMu_Jet)):
        os.system('mkdir -p '+folder_BTagDiMu_Jet[i])
for i in range(0,len(folder_BTagMu_DiJet)):
	os.system('mkdir -p '+folder_BTagMu_DiJet[i])
for i in range(0,len(folder_BTagMu_Jet)):
	os.system('mkdir -p '+folder_BTagMu_Jet[i])

parent_folder = "DQMData/Run 1/HLT/Run summary/BTV/"


histo_names = ["effic_bjetCSV_1", "effic_bjetEta_1_variableBinning", "effic_bjetPt_1_variableBinning"]


for i in range(0,len(folder_BTagDiMu_Jet)):
	for j in range(0,len(histo_names)):
		c = TCanvas()
		print(parent_folder+folder_BTagDiMu_Jet[i]+histo_names[j])
		h = f.Get(parent_folder+folder_BTagDiMu_Jet[i]+histo_names[j])
		if histo_names[j] == "effic_bjetPt_1_variableBinning":
			h.GetXaxis().SetRangeUser(0,500)
		h.Draw("EP")
		c.SaveAs(folder_BTagDiMu_Jet[i]+histo_names[j]+".pdf")


for i in range(0,len(folder_BTagMu_DiJet)):
        for j in range(0,len(histo_names)):
                c = TCanvas()
                print(parent_folder+folder_BTagMu_DiJet[i]+histo_names[j])
                h = f.Get(parent_folder+folder_BTagMu_DiJet[i]+histo_names[j])
                if histo_names[j] == "effic_bjetPt_1_variableBinning":
                        h.GetXaxis().SetRangeUser(0,500)
                h.Draw("EP")
                c.SaveAs(folder_BTagMu_DiJet[i]+histo_names[j]+".pdf")


for i in range(0,len(folder_BTagMu_Jet)):
        for j in range(0,len(histo_names)):
                c = TCanvas()
                print(parent_folder+folder_BTagMu_Jet[i]+histo_names[j])
                h = f.Get(parent_folder+folder_BTagMu_Jet[i]+histo_names[j])
                if histo_names[j] == "effic_bjetPt_1_variableBinning":
                        h.GetXaxis().SetRangeUser(0,500)
                h.Draw("EP")
                c.SaveAs(folder_BTagMu_Jet[i]+histo_names[j]+".pdf")
