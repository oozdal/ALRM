import os
import pyslha
from MyPySLHA import *
import fnmatch
from scipy.interpolate import interp1d

######## File Paths #################

maindirpath = os.path.abspath("/home/phylab/projects/ALRM_multithread")
datafilepath = os.path.abspath("/home/phylab/projects/ALRM_multithread/data/Accepted_gLNEQgR_6.txt")

excludedfilepath = os.path.abspath("/home/phylab/projects/ALRM_multithread/data/Excluded_gLNEQgR_6.txt")
#####################################

numberofoutputdir = len(fnmatch.filter(os.listdir(maindirpath), 'e*'))

#for i in range(1,numberofoutputdir+1):
for i in range(1,8):    
    f_filename = "/e"+str(i)
    print f_filename
    f_filepath = maindirpath + f_filename

    outputdir = f_filepath + "/outfiles"
    numberofoutput = len(fnmatch.filter(os.listdir(outputdir), 'DM_ALRM.*'))

    for j in range(1,numberofoutput):
        outputfilefullpath = os.path.abspath(outputdir+"/DM_ALRM."+str(j)) 
        LHA = MyPySLHA()
        if os.path.isfile(outputfilefullpath):
            LHA.LoadLHAFile(outputfilefullpath)
            LHA.Parameters()
            LHA.NormalizeDMResults()
            LHA.MassesFromMicrOMEGAs()
            LHA.CheckMinimization()
            LHA.CheckHiggsMasses()
            LHA.CheckHiggsMixing()
            LHA.CheckZpMassLimit()

#            if LHA.CheckMicrOMEGABlock() == True and LHA.MZp >= 5000:
            if LHA.CheckMicrOMEGABlock() == True and LHA.CheckZpMassLimit() == True:
#                print "LHA Constraints are satisfied!"
                g= open(datafilepath,"a+")
                g.write("%.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E" % (LHA.vp, LHA.MZp, LHA.MWp, LHA.Scot_DM, LHA.Scot_mu, LHA.Scot_tau, LHA.MDD, LHA.MDS, LHA.MDB, LHA.Relic_Density, LHA.NormSI_proton, LHA.NormSI_neutron, LHA.SD_proton, LHA.SD_neutron, LHA.sigmaV, LHA.SI_proton, LHA.SI_neutron, LHA.lm3, LHA.mu3, LHA.mh1, LHA.mh2, LHA.mh3, LHA.mA2, LHA.al1, LHA.al2, LHA.THP0, LHA.THP2, LHA.THL2, LHA.THR2, LHA.THP3, LHA.THL3, LHA.THR3))
                g.write('\n')
                g.close()

            elif LHA.CheckMicrOMEGABlock() == True and LHA.CheckZpMassLimit() == False:
                h= open(excludedfilepath,"a+")
                h.write("%.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E" % (LHA.vp, LHA.MZp, LHA.MWp, LHA.Scot_DM, LHA.Scot_mu, LHA.Scot_tau, LHA.MDD, LHA.MDS, LHA.MDB, LHA.Relic_Density, LHA.NormSI_proton, LHA.NormSI_neutron, LHA.SD_proton, LHA.SD_neutron, LHA.sigmaV, LHA.SI_proton, LHA.SI_neutron, LHA.lm3, LHA.mu3, LHA.mh1, LHA.mh2, LHA.mh3, LHA.mA2, LHA.al1, LHA.al2, LHA.THP0, LHA.THP2, LHA.THL2, LHA.THR2, LHA.THP3, LHA.THL3, LHA.THR3))
                h.write('\n')
                h.close()                

    
