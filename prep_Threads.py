######## Packages ###########

import os
import shutil
from MyMultiThread import *

######## Current File Paths ########

FullPathForMainDirectories = os.path.abspath("/home/phylab/projects/ALRM_multithread/g")

PathForMainDirectory = os.path.dirname(FullPathForMainDirectories)

#####################################

Thread = MyMultiThread()

NumberofThread = 9

for f_no in range(1,NumberofThread+1):
    PathForfDirectory=PathForMainDirectory+"/g"+str(f_no)
    if os.path.exists(PathForfDirectory):
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
        shutil.copy2("ALRM_calculator.py",PathForfDirectory)

        os.chdir(PathForfDirectory)
        Thread.ScreenBaseName = "g"
        Thread.ScreenFullName = Thread.ScreenBaseName+'_'+str(f_no)

        os.system("screen -S "+ Thread.ScreenFullName +" -dm ipython -i run_ALRM_gLneqgR.py")
        os.chdir("../")

        
"""
Thread.KillScreen("g_1")
Thread.KillScreen("g_2")
Thread.KillScreen("g_3")
Thread.KillScreen("g_4")
Thread.KillScreen("g_5")
Thread.KillScreen("g_6")
Thread.KillScreen("g_7")
Thread.KillScreen("g_8")
Thread.KillScreen("g_9")
"""
