import os
import pyslha
from MyPySLHA import *
import fnmatch

######## File Paths #################

maindirpath = os.path.abspath("/home/phylab/projects/ALRM_multithread")
datafilepath = os.path.abspath("/home/phylab/projects/ALRM_multithread/data/Accepted_gLNEQgR_4.txt")

#####################################

numberofoutputdir = len(fnmatch.filter(os.listdir(maindirpath), 'f*'))

#for i in range(1,numberofoutputdir+1):
for i in range(1,6):    
    f_filename = "/f"+str(i)
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

            if LHA.CheckMicrOMEGABlock() == True and LHA.MZp >= 5000:            
#                print "LHA Constraints are satisfied!"
                g= open(datafilepath,"a+")
                g.write("%.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E %.6E" % (LHA.vp, LHA.MZp, LHA.MWp, LHA.Scot_DM, LHA.Scot_mu, LHA.Scot_tau, LHA.MDD, LHA.MDS, LHA.MDB, LHA.Relic_Density, LHA.NormSI_proton, LHA.NormSI_neutron, LHA.SD_proton, LHA.SD_neutron, LHA.sigmaV, LHA.SI_proton, LHA.SI_neutron, LHA.lm3, LHA.mu3, LHA.mh1, LHA.mh2, LHA.mh3, LHA.mA2, LHA.al1, LHA.al2, LHA.THP0))
                g.write('\n')
                g.close()

            else:
                continue

    
