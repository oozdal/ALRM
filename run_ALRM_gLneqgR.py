######## Packages ###########

import fnmatch
import numpy as np
import os
import pyslha
import pandas as pd

from MyPySLHA import *
from MyMicrOMEGAs import *

######## Current File Paths ########

LHAFileFullPath = os.path.abspath("master_gLneqgR.lha")

LHAFiledirPath = os.path.dirname(LHAFileFullPath)

LHAFileName = os.path.basename(LHAFileFullPath)

######## Desired File Paths #########

Pathforvars1lha = os.path.abspath("vars1.lha")
PathforMicrOMEGAsResult = os.path.abspath("Block_micrOMEGAs.out")
PathforChannelsOutput = os.path.abspath("Channels.out")

PathForLHAfiles = os.path.abspath("LHAfiles")
dirPathLHAFileWithDM = os.path.dirname("outfiles/DM_ALRM.")

#####################################

NumberofEvent = 20000
TotalFocusedRun = 50

list_RD_diff = []

for iter in range(1,NumberofEvent):
    currentLHA = MyPySLHA()
    sigma = 0.10
    if currentLHA.CheckLHAexist(LHAFileFullPath) == True:
        currentLHA.LoadLHAFile(LHAFileFullPath)            # Load all content to PySLHA
        currentLHA.Parameters()

        currentLHA.allcontent.blocks["ALRMINPUTS"][1] = 0.0    #lm2
#        currentLHA.allcontent.blocks["ALRMINPUTS"][2] = np.random.uniform(0.010,0.030)  #lm3
        currentLHA.allcontent.blocks["ALRMINPUTS"][2] = np.random.uniform(0.001,0.050)  #lm3

        currentLHA.allcontent.blocks["ALRMINPUTS"][3] = np.random.normal(0.3,sigma)  #al1
        currentLHA.allcontent.blocks["ALRMINPUTS"][4] = np.random.normal(-0.2,sigma) #al2
        currentLHA.allcontent.blocks["ALRMINPUTS"][5] = currentLHA.allcontent.blocks["ALRMINPUTS"][3]   #al3        

        currentLHA.allcontent.blocks["ALRMINPUTS"][6] = np.random.uniform(1.0,50.0)    #tb
        currentLHA.allcontent.blocks["ALRMINPUTS"][7] = np.random.uniform(-0.8, -0.3)  #mu3
#        currentLHA.allcontent.blocks["ALRMINPUTS"][8] = 6850. #vp
        currentLHA.allcontent.blocks["ALRMINPUTS"][8] = np.random.uniform(6500., 11000.) #vp

#        currentLHA.allcontent.blocks["ALRMINPUTS"][9] = 0.370000000000000
        currentLHA.allcontent.blocks["ALRMINPUTS"][9] = np.random.uniform(0.37, currentLHA.gL)

        currentLHA.allcontent.blocks["MASS"][103] = np.random.uniform(10,900)
        currentLHA.allcontent.blocks["MASS"][104] = np.random.uniform(currentLHA.allcontent.blocks["MASS"][103],currentLHA.allcontent.blocks["MASS"][103] + 1500.)
        currentLHA.allcontent.blocks["MASS"][105] = np.random.uniform(currentLHA.allcontent.blocks["MASS"][104],currentLHA.allcontent.blocks["MASS"][104] + 2000.)

        currentLHA.allcontent.blocks["MASS"][106] = np.random.uniform(500,2000)
        currentLHA.allcontent.blocks["MASS"][107] = np.random.uniform(currentLHA.allcontent.blocks["MASS"][106],2500)
        currentLHA.allcontent.blocks["MASS"][108] = np.random.uniform(currentLHA.allcontent.blocks["MASS"][107],3000)

        currentLHA.allcontent.blocks["YUKAWA"][17] = currentLHA.allcontent.blocks["MASS"][103]
        currentLHA.allcontent.blocks["YUKAWA"][18] = currentLHA.allcontent.blocks["MASS"][104]
        currentLHA.allcontent.blocks["YUKAWA"][19] = currentLHA.allcontent.blocks["MASS"][105]

        currentLHA.allcontent.blocks["YUKAWA"][7] = currentLHA.allcontent.blocks["MASS"][106]
        currentLHA.allcontent.blocks["YUKAWA"][8] = currentLHA.allcontent.blocks["MASS"][107]
        currentLHA.allcontent.blocks["YUKAWA"][9] = currentLHA.allcontent.blocks["MASS"][108]

        fileno = len(fnmatch.filter(os.listdir(PathForLHAfiles), 'ALRM.*'))
        newfileno = fileno + 1
        currentLHA.NewLHAFileName = "ALRM."+str(newfileno)
        currentLHA.NewLHAFileFullPath = LHAFiledirPath + "/LHAfiles/" + currentLHA.NewLHAFileName
        currentLHA.WriteNewLHAFile(currentLHA.NewLHAFileFullPath, currentLHA.allcontent, 10)

################# MicrOMEGAs Part ###########################################
        if currentLHA.CheckMinimization() == True:
            MicrOMEGAs = MyMicrOMEGAs()
            MicrOMEGAs.RenameAndCopy(currentLHA.NewLHAFileFullPath, Pathforvars1lha)
            MicrOMEGAs.RunMicrOMEGAs(Pathforvars1lha)

            MicrOMEGAs.LHAFileWithDM = os.path.basename("DM_ALRM."+str(newfileno))
            MicrOMEGAs.FullDestForLHAFileWithDM = dirPathLHAFileWithDM+"/"+MicrOMEGAs.LHAFileWithDM
            MicrOMEGA_Result_exist = os.path.isfile(PathforMicrOMEGAsResult)

            MicrOMEGAs.ChannelsNewFileName = os.path.basename("Channels."+str(newfileno))
            MicrOMEGAs.FullDestForChannels = dirPathLHAFileWithDM+"/"+MicrOMEGAs.ChannelsNewFileName
            Channels_exist = os.path.isfile(PathforChannelsOutput)

            if (MicrOMEGA_Result_exist and Channels_exist) == True:
                MicrOMEGAs.LHAwithDM(currentLHA.NewLHAFileFullPath, PathforMicrOMEGAsResult, MicrOMEGAs.FullDestForLHAFileWithDM)
                MicrOMEGAs.RenameAndCopy(PathforChannelsOutput, MicrOMEGAs.FullDestForChannels)
                currentLHA.Erase(PathforMicrOMEGAsResult)
                currentLHA.Erase(PathforChannelsOutput)

################# Reading MicrOMEGAs Output ###################################

            exist_FullDestForLHAFileWithDM = os.path.isfile(MicrOMEGAs.FullDestForLHAFileWithDM)
            exist_ChannelsNewFileName      = os.path.isfile(MicrOMEGAs.ChannelsNewFileName)

            if (exist_FullDestForLHAFileWithDM and exist_ChannelsNewFileName) == True:
                currentLHA.LoadLHAFile(MicrOMEGAs.FullDestForLHAFileWithDM)
                if currentLHA.CheckMicrOMEGABlock() == True:
                    currentLHA.Parameters()
                    currentLHA.NormalizeDMResults()
                    currentLHA.MassesFromMicrOMEGAs()
                    currentLHA.ReadChannels(MicrOMEGAs.FullDestForChannels)
                    currentLHA.CheckHiggsFunnel()                
                    list_RD_diff.append(currentLHA.RD_difference())

#                    if (currentLHA.MassConstraints() and currentLHA.RelicDensity_Constraint()) == False:
                    if (currentLHA.MassConstraints() and currentLHA.Check_RD_diff(list_RD_diff)) == False:
                        currentLHA.Erase(currentLHA.NewLHAFileFullPath)                        
                        currentLHA.Erase(MicrOMEGAs.FullDestForLHAFileWithDM)
                        currentLHA.Erase(MicrOMEGAs.FullDestForChannels)

################# Running over a specific solution ############################

#                    if currentLHA.MassConstraints() == True and currentLHA.Relic_Density_Bound == True and currentLHA.HiggsFunnelPercentage >= 10:
#                    elif (currentLHA.MassConstraints() and currentLHA.RelicDensity_Constraint()) == True:
                    elif (currentLHA.MassConstraints() and currentLHA.Check_RD_diff(list_RD_diff)) == True:                    
                        for i in range(1,TotalFocusedRun):

                            currentLHA.allcontent.blocks["ALRMINPUTS"][1] = 0.0    #lm2
                            currentLHA.allcontent.blocks["ALRMINPUTS"][2] = currentLHA.allcontent.blocks["ALRMINPUTS"][2]   #lm3

                            currentLHA.allcontent.blocks["ALRMINPUTS"][3] = np.random.normal(currentLHA.allcontent.blocks["ALRMINPUTS"][3],sigma)   #al1
                            currentLHA.allcontent.blocks["ALRMINPUTS"][4] = np.random.normal(currentLHA.allcontent.blocks["ALRMINPUTS"][4],sigma)   #al2
                            currentLHA.allcontent.blocks["ALRMINPUTS"][5] = currentLHA.allcontent.blocks["ALRMINPUTS"][3]   #al3

                            currentLHA.allcontent.blocks["ALRMINPUTS"][6] = np.random.normal(currentLHA.allcontent.blocks["ALRMINPUTS"][6],sigma) #tb
                            currentLHA.allcontent.blocks["ALRMINPUTS"][7] = np.random.normal(currentLHA.allcontent.blocks["ALRMINPUTS"][7],sigma) #mu3
                            currentLHA.allcontent.blocks["ALRMINPUTS"][8] = currentLHA.allcontent.blocks["ALRMINPUTS"][8] #vp

                            currentLHA.allcontent.blocks["ALRMINPUTS"][9] = currentLHA.allcontent.blocks["ALRMINPUTS"][9]

                            currentLHA.allcontent.blocks["MASS"][103] = np.random.normal(currentLHA.allcontent.blocks["MASS"][103],10)
                            currentLHA.allcontent.blocks["MASS"][104] = np.random.normal(currentLHA.allcontent.blocks["MASS"][104],10)
                            currentLHA.allcontent.blocks["MASS"][105] = np.random.normal(currentLHA.allcontent.blocks["MASS"][105],10)

                            currentLHA.allcontent.blocks["MASS"][106] = np.random.normal(currentLHA.allcontent.blocks["MASS"][106],10)
                            currentLHA.allcontent.blocks["MASS"][107] = np.random.normal(currentLHA.allcontent.blocks["MASS"][107],10)
                            currentLHA.allcontent.blocks["MASS"][108] = np.random.normal(currentLHA.allcontent.blocks["MASS"][108],10)

                            currentLHA.allcontent.blocks["YUKAWA"][17] = currentLHA.allcontent.blocks["MASS"][103]
                            currentLHA.allcontent.blocks["YUKAWA"][18] = currentLHA.allcontent.blocks["MASS"][104]
                            currentLHA.allcontent.blocks["YUKAWA"][19] = currentLHA.allcontent.blocks["MASS"][105]

                            currentLHA.allcontent.blocks["YUKAWA"][7] = currentLHA.allcontent.blocks["MASS"][106]
                            currentLHA.allcontent.blocks["YUKAWA"][8] = currentLHA.allcontent.blocks["MASS"][107]
                            currentLHA.allcontent.blocks["YUKAWA"][9] = currentLHA.allcontent.blocks["MASS"][108]


                            fileno = len(fnmatch.filter(os.listdir(PathForLHAfiles), 'ALRM.*'))
                            newfileno = fileno + 1
                            currentLHA.NewLHAFileName = "ALRM."+str(newfileno)
                            currentLHA.NewLHAFileFullPath = LHAFiledirPath + "/LHAfiles/" + currentLHA.NewLHAFileName
                            currentLHA.WriteNewLHAFile(currentLHA.NewLHAFileFullPath, currentLHA.allcontent, 10)

################# MicrOMEGAs Part ###########################################

                            Micro_small = MyMicrOMEGAs()
                            Micro_small.RenameAndCopy(currentLHA.NewLHAFileFullPath, Pathforvars1lha)
                            Micro_small.RunMicrOMEGAs(Pathforvars1lha)

                            Micro_small.LHAFileWithDM = os.path.basename("DM_ALRM."+str(newfileno))
                            Micro_small.FullDestForLHAFileWithDM = dirPathLHAFileWithDM+"/"+Micro_small.LHAFileWithDM
                            MicrOMEGA_Result_exist = os.path.isfile(PathforMicrOMEGAsResult)

                            Micro_small.ChannelsNewFileName = os.path.basename("Channels."+str(newfileno))
                            Micro_small.FullDestForChannels = dirPathLHAFileWithDM+"/"+Micro_small.ChannelsNewFileName
                            Channels_exist = os.path.isfile(PathforChannelsOutput)
                        
                            if (MicrOMEGA_Result_exist and Channels_exist) == True:
                                Micro_small.LHAwithDM(currentLHA.NewLHAFileFullPath, PathforMicrOMEGAsResult, Micro_small.FullDestForLHAFileWithDM)
                                Micro_small.RenameAndCopy(PathforChannelsOutput, Micro_small.FullDestForChannels)
                                currentLHA.Erase(PathforMicrOMEGAsResult)
                                currentLHA.Erase(PathforChannelsOutput)

################# Reading MicrOMEGAs Output ###################################

                            exist_FullDestForLHAFileWithDM = os.path.isfile(Micro_small.FullDestForLHAFileWithDM)
                            exist_ChannelsNewFileName      = os.path.isfile(Micro_small.ChannelsNewFileName)

                            if (exist_FullDestForLHAFileWithDM and exist_ChannelsNewFileName) == True:
                                currentLHA.LoadLHAFile(Micro_small.FullDestForLHAFileWithDM)
                                if currentLHA.CheckMicrOMEGABlock() == True:
                                    currentLHA.Parameters()
                                    currentLHA.NormalizeDMResults()
                                    currentLHA.MassesFromMicrOMEGAs()
                                    currentLHA.ReadChannels(Micro_small.FullDestForChannels)
                                    currentLHA.CheckHiggsFunnel()
                                    list_RD_diff.append(currentLHA.RD_difference())
                                
                                    if (currentLHA.MassConstraints() and currentLHA.Check_RD_diff(list_RD_diff)) == False:
                                        currentLHA.Erase(currentLHA.NewLHAFileFullPath)
                                        currentLHA.Erase(Micro_small.FullDestForLHAFileWithDM)
                                        currentLHA.Erase(Micro_small.FullDestForChannels)

        elif currentLHA.CheckMinimization() == False:
            currentLHA.Erase(currentLHA.NewLHAFileFullPath)
