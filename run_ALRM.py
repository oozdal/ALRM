######## Packages ###########

import os
import pyslha
import pandas as pd

from classMyPySLHA import *

######## File Paths ########

LHAFileFullPath = os.path.abspath("/home/phylab/projects/ALRM/analysis/vars1.lha")

LHAFiledirPath = os.path.dirname(LHAFileFullPath)

LHAFileName = os.path.basename(LHAFileFullPath)


############################

Scotino_Mass = 10.0

currentLHA = classMyPySLHA()

for iter in range(1,101):
    if currentLHA.CheckLHAexist(LHAFileFullPath) == True:
        currentLHA.LoadLHAFile(LHAFileFullPath)                   # Load all content to PySLHA
        currentLHA.allcontent.blocks["MASS"][103] = Scotino_Mass  # Assign new value
        currentLHA.NewLHAFileName = "ALRM."+str(iter)
        currentLHA.NewLHAFileFullPath = LHAFiledirPath + "/LHA_outputs/" + currentLHA.NewLHAFileName
        currentLHA.WriteNewLHAFile(currentLHA.NewLHAFileFullPath, currentLHA.allcontent, 10)

        Scotino_Mass = Scotino_Mass + 10.0




