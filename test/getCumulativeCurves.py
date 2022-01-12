import ROOT
from ROOT import *
import numpy
gROOT.SetBatch(1)
import os

files = [
    # "outFull_HLT_Run3TRK_ROICaloROIPF_Mu_oldJECs_data323775_lumijson.root",
    "QCD50to80_oldDeepJet_oldDeepCSV.root",
    "QCD50to80_newDeepJet_oldDeepCSV.root",
    "ttbar_oldDeepJet_oldDeepCSV.root",
    "ttbar_newDeepJet_oldDeepCSV.root",
    ]

def getRateHisto(h):
    outH = h.Clone()
    outH.SetName(h.GetName()+"_int")
    outH.SetDirectory(0)
    for binX in range(0, h.GetNbinsX()+1):
        import ctypes
        err = ctypes.c_double(0.)
        int = h.IntegralAndError(binX, h.GetNbinsX()+2, err)
        # print ("rate", outH.GetName(), binX, int)
        outH.SetBinContent(binX, int)
        outH.SetBinError(binX, err)
    return outH

def getEffHistos(hLight, hHeavy):
    outH = hHeavy.Clone()
    outH.SetName(hHeavy.GetName()+"_eff_b")
    outH.SetDirectory(0)
    outH_l = hLight.Clone()
    outH_l.SetName(hLight.GetName()+"_eff_l")
    outH_l.SetDirectory(0)
    totalInt_light = hLight.Integral(0, hLight.GetNbinsX()+2)
    totalInt_heavy = hHeavy.Integral(0, hHeavy.GetNbinsX()+2)
    for binX in range(0, hLight.GetNbinsX()+1):
        import ctypes
        errLight = ctypes.c_double(0.)
        intLight = hLight.IntegralAndError(binX, hLight.GetNbinsX()+2, errLight)
        errHeavy = ctypes.c_double(0.)
        intHeavy = hHeavy.IntegralAndError(binX, hHeavy.GetNbinsX()+2, errHeavy)
        eff_heavy = intHeavy/(totalInt_heavy) if totalInt_heavy> 0 else 0.
        eff_light = intLight/(totalInt_light) if totalInt_light> 0 else 0.
        # print ("rate", outH_l.GetName(), binX, intLight, totalInt_light, eff_light)
        outH.SetBinContent(binX, eff_heavy)
        outH.SetBinError(binX, 0.)
        outH_l.SetBinContent(binX, eff_light)
        outH_l.SetBinError(binX, 0.)
    return outH,outH_l

for fname in files:
    if not os.path.exists(fname):
        continue
    f = ROOT.TFile(fname, "OPEN")
    tree = f.Get("btagana/ttree")

    if not os.path.exists("SimpleTaggerStudies"):
        os.makedirs("SimpleTaggerStudies/")

    h_b_DeepCSV = ROOT.TH1F("h_b_DeepCSV"+"_"+fname, "h_b_DeepCSV", 110, -1, 1)
    h_b_DeepJet = ROOT.TH1F("h_b_DeepJet"+"_"+fname, "h_b_DeepJet", 110, -1, 1)
    h_l_DeepCSV = ROOT.TH1F("h_l_DeepCSV"+"_"+fname, "h_l_DeepCSV", 110, -1, 1)
    h_l_DeepJet = ROOT.TH1F("h_l_DeepJet"+"_"+fname, "h_l_DeepJet", 110, -1, 1)
    h_all_DeepCSV = ROOT.TH1F("h_all_DeepCSV"+"_"+fname, "h_all_DeepCSV", 110, -1, 1)
    h_all_DeepJet = ROOT.TH1F("h_all_DeepJet"+"_"+fname, "h_all_DeepJet", 110, -1, 1)

    for event in tree:
        # print (event.nJet)
        # print (event.Jet_isB[0])
        for jetIdx in range(event.nJet):
            if event.Jet_pt[jetIdx] < 30. : continue
            if abs(event.Jet_eta[jetIdx]) > 2.5 : continue
            isB = (event.Jet_isB[jetIdx] or
                event.Jet_isBB[jetIdx] or
                event.Jet_isLeptonicB[jetIdx] or
                event.Jet_isLeptonicB_C[jetIdx] or
                event.Jet_isGBB[jetIdx])
            isL = (event.Jet_isUD[jetIdx] or
                event.Jet_isS[jetIdx] or
                event.Jet_isG[jetIdx] or
                event.Jet_isC[jetIdx] or
                event.Jet_isGCC[jetIdx] or
                event.Jet_isCC[jetIdx])
            # isL = (event.Jet_isUD[jetIdx] or
            #     event.Jet_isS[jetIdx] or
            #     event.Jet_isG[jetIdx])
            #     # event.Jet_isC[jetIdx] or
            #     # event.Jet_isGCC[jetIdx] or
            #     # event.Jet_isCC[jetIdx])
            deepcsv = event.Jet_DeepCSVb[jetIdx]
            deepjet = event.Jet_DeepFlavourBDisc[jetIdx]
            # print (deepcsv)
            h_all_DeepCSV.Fill(deepcsv)
            h_all_DeepJet.Fill(deepjet)

            if (isB):
                h_b_DeepCSV.Fill(deepcsv)
                h_b_DeepJet.Fill(deepjet)
            if (isL):
                h_l_DeepCSV.Fill(deepcsv)
                h_l_DeepJet.Fill(deepjet)
            h_all_DeepCSV.Fill(deepcsv)
            h_all_DeepJet.Fill(deepjet)

    outFile = ROOT.TFile("SimpleTaggerStudies/SimpleRate_"+fname,"RECREATE")
    outFile.cd()
    h_b_DeepCSV.Write()
    h_b_DeepJet.Write()
    h_l_DeepCSV.Write()
    h_l_DeepJet.Write()
    h_all_DeepCSV.Write()
    h_all_DeepJet.Write()

    h_all_DeepCSV_sum = getRateHisto(h_all_DeepCSV)
    h_l_DeepCSV_sum = getRateHisto(h_l_DeepCSV)
    h_b_DeepCSV_sum = getRateHisto(h_b_DeepCSV)
    h_all_DeepJet_sum = getRateHisto(h_all_DeepJet)
    h_l_DeepJet_sum = getRateHisto(h_l_DeepJet)
    h_b_DeepJet_sum = getRateHisto(h_b_DeepJet)
    h_all_DeepCSV_sum.Write()
    h_l_DeepCSV_sum.Write()
    h_b_DeepCSV_sum.Write()
    h_all_DeepJet_sum.Write()
    h_l_DeepJet_sum.Write()
    h_b_DeepJet_sum.Write()


    eff_deepcsv_b,eff_deepcsv_l = getEffHistos(h_l_DeepCSV, h_b_DeepCSV)
    eff_deepjet_b,eff_deepjet_l = getEffHistos(h_l_DeepJet, h_b_DeepJet)

    eff_deepcsv_b.SetMaximum(1.1)
    eff_deepjet_b.SetMaximum(1.1)
    eff_deepcsv_l.SetMaximum(1.1)
    eff_deepjet_l.SetMaximum(1.1)
    eff_deepcsv_b.SetMinimum(0.)
    eff_deepjet_b.SetMinimum(0.)
    eff_deepcsv_l.SetMinimum(0.)
    eff_deepjet_l.SetMinimum(0.)

    c = ROOT.TCanvas("Eff"+"_"+fname, "Eff",800,800)
    c.cd()
    eff_deepcsv_b.SetLineColor(ROOT.kBlack)
    eff_deepcsv_b.SetLineWidth(2)
    eff_deepcsv_b.SetLineStyle(1)
    eff_deepcsv_b.Draw("hist")
    eff_deepjet_b.SetLineColor(ROOT.kBlack)
    eff_deepjet_b.SetLineWidth(2)
    eff_deepjet_b.SetLineStyle(2)
    eff_deepjet_b.Draw("hist same")

    eff_deepcsv_l.SetLineColor(ROOT.kRed)
    eff_deepcsv_l.SetLineWidth(2)
    eff_deepcsv_l.SetLineStyle(1)
    eff_deepcsv_l.Draw("hist same")
    eff_deepjet_l.SetLineColor(ROOT.kRed)
    eff_deepjet_l.SetLineWidth(2)
    eff_deepjet_l.SetLineStyle(2)
    eff_deepjet_l.Draw("hist same")


    leg = ROOT.TLegend(0.2,0.2,0.4,0.4)
    leg.AddEntry(eff_deepcsv_l, "DeepCSV light", "l")
    leg.AddEntry(eff_deepcsv_b, "DeepCSV b", "l")
    leg.AddEntry(eff_deepjet_l, "DeepJet light", "l")
    leg.AddEntry(eff_deepjet_b, "DeepJet b", "l")
    leg.Draw()

    c.Write()
    c.Clear()

    c = ROOT.TCanvas("RatePlot_all"+"_"+fname, "RatePlot_all",800,800)
    c.cd()
    h_all_DeepCSV_sum.SetLineColor(ROOT.kBlack)
    h_all_DeepCSV_sum.SetLineWidth(2)
    h_all_DeepCSV_sum.Draw("hist")
    h_all_DeepJet_sum.SetLineColor(ROOT.kRed)
    h_all_DeepJet_sum.SetLineWidth(2)
    h_all_DeepJet_sum.Draw("hist same")
    leg = ROOT.TLegend(0.2,0.2,0.4,0.4)
    leg.AddEntry(h_all_DeepCSV_sum, "DeepCSV all", "l")
    leg.AddEntry(h_all_DeepJet_sum, "DeepJet all", "l")
    leg.Draw()
    c.Write()
    c.Clear()

    c = ROOT.TCanvas("RatePlot_l"+"_"+fname, "RatePlot_l",800,800)
    c.cd()
    h_l_DeepCSV_sum.SetLineColor(ROOT.kBlack)
    h_l_DeepCSV_sum.SetLineWidth(2)
    h_l_DeepCSV_sum.Draw("hist")
    h_l_DeepJet_sum.SetLineColor(ROOT.kRed)
    h_l_DeepJet_sum.SetLineWidth(2)
    h_l_DeepJet_sum.Draw("hist same")
    leg = ROOT.TLegend(0.2,0.2,0.4,0.4)
    leg.AddEntry(h_l_DeepCSV_sum, "DeepCSV l", "l")
    leg.AddEntry(h_l_DeepJet_sum, "DeepJet l", "l")
    leg.Draw()
    c.Write()
    c.Clear()

    c = ROOT.TCanvas("RatePlot_b"+"_"+fname, "RatePlot_b",800,800)
    c.cd()
    h_b_DeepCSV_sum.SetLineColor(ROOT.kBlack)
    h_b_DeepCSV_sum.SetLineWidth(2)
    h_b_DeepCSV_sum.Draw("hist")
    h_b_DeepJet_sum.SetLineColor(ROOT.kRed)
    h_b_DeepJet_sum.SetLineWidth(2)
    h_b_DeepJet_sum.Draw("hist same")
    leg = ROOT.TLegend(0.2,0.2,0.4,0.4)
    leg.AddEntry(h_b_DeepCSV_sum, "DeepCSV b", "l")
    leg.AddEntry(h_b_DeepJet_sum, "DeepJet b", "l")
    leg.Draw()
    c.Write()
    c.Clear()

    outFile.Close()

    del c, leg, h_b_DeepCSV, h_b_DeepJet, h_l_DeepCSV, h_l_DeepJet, h_all_DeepCSV, h_all_DeepJet
    del h_all_DeepCSV_sum, h_all_DeepJet_sum, h_l_DeepCSV_sum, h_l_DeepJet_sum, h_b_DeepCSV_sum, h_b_DeepJet_sum
    del eff_deepcsv_l, eff_deepjet_l, eff_deepcsv_b, eff_deepjet_b

    print ("Saved "+"SimpleRate_"+fname)
