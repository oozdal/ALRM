######## Packages ###########

import os
import shutil
from MyMultiThread import *

######## Current File Paths ########

FullPathForMainDirectories = os.path.abspath("/home/phylab/projects/ALRM_multithread/f")

PathForMainDirectory = os.path.dirname(FullPathForMainDirectories)

#####################################

Thread = MyMultiThread()

NumberofThread = 8

for f_no in range(1,NumberofThread+1):
    PathForfDirectory=PathForMainDirectory+"/e"+str(f_no)

    if  os.path.exists(PathForfDirectory):
#        os.makedirs(PathForfDirectory)            ####
#        print PathForfDirectory + " is created!"  ####

        PathForLHAfiles    = PathForfDirectory+"/LHAfiles"
        PathForOutputFiles = PathForfDirectory+"/outfiles"
#        os.makedirs(PathForLHAfiles)              ####
#        print PathForLHAfiles + " is created!"    ####
#        os.makedirs(PathForOutputFiles)           ####
#        print PathForOutputFiles + " is created!" ####
    
        shutil.copy2("master_gLneqgR.lha",PathForfDirectory) 
        shutil.copy2("run_ALRM_gLneqgR.py",PathForfDirectory)
        shutil.copy2("MyPySLHA.py",PathForfDirectory)
        shutil.copy2("MyMicrOMEGAs.py",PathForfDirectory)

        os.chdir(PathForfDirectory)
        Thread.ScreenBaseName = "e"
        Thread.ScreenFullName = Thread.ScreenBaseName+'_'+str(f_no)

        os.system("screen -S "+ Thread.ScreenFullName +" -dm ipython -i run_ALRM_gLneqgR.py")
        os.chdir("../")


"""
Thread.KillScreen("e_1")
Thread.KillScreen("e_2")
Thread.KillScreen("e_3")
Thread.KillScreen("e_4")
Thread.KillScreen("e_5")
Thread.KillScreen("e_6")
Thread.KillScreen("e_7")
Thread.KillScreen("e_8")
Thread.KillScreen("trial_9")
Thread.KillScreen("trial_10")
"""
