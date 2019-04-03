import pandas as pd
import numpy as np
import os
import pyslha
from math import *
from scipy.interpolate import interp1d

class MyPySLHA():
    def __init__(self):
        pass        

    def CheckLHAexist(self,LHAPath):
        return os.path.isfile(LHAPath)

    def LoadLHAFile(self, LHAPath):
        self.allcontent = pyslha.read(LHAPath, ignoreblocks=['SPINFO'])

    def WriteNewLHAFile(self, newLHAPath, newLHAcontent, precision_val):
        self.newLHA = pyslha.writeSLHAFile(newLHAPath, newLHAcontent, precision=precision_val)

    def Read_Block(self, BlockName, id1=None, id2=None, id3=None):
        self.BlockName       = BlockName
        self.id1             = id1
        self.id2             = id2
        self.id3             = id3

        self.list_all_blocks = self.allcontent.blocks
        self.pyslha_Block    = self.allcontent.blocks[self.BlockName]

        if self.id1 != None and self.id2 == None and self.id3 == None:
            self.VarValue1   = self.pyslha_Block[self.id1]
            return self.VarValue1

        elif self.id1 != None and self.id2 != None and self.id3 == None:
            self.VarValue2   = self.pyslha_Block[self.id1,self.id2]
            return self.VarValue2

        else:
            self.VarValue3   = self.pyslha_Block[self.id1,self.id2,self.id3]
            return self.VarValue3



    def Read_Decays(self, PySLHAparticleID, DecayProduct = None):

        self.PySLHAparticle = self.allcontent.decays[PySLHAparticleID]

        self.DecayProduct = DecayProduct

        self.list_decaysmodes = self.PySLHAparticle.decays
        self.totalwidth       = self.PySLHAparticle.totalwidth
        self.ParticleMass     = self.PySLHAparticle.mass

        for i in range(len(self.list_decaysmodes)):
            self.decaymode = self.list_decaysmodes[i]
            if self.decaymode.ids == self.DecayProduct:
                return self.decaymode.br


    def CheckMicrOMEGABlock(self):
        if self.allcontent.blocks.has_key("MICROMEGAS") == True:
            self.MicrOMEGASblock = self.allcontent.blocks["MICROMEGAS"]
            if self.MicrOMEGASblock.items() != []:
                return True
            else:
                return False
        else:
            return False

    def NormalizeDMResults(self):
        
        self.PlanckResult  = 0.1187

        
        if self.CheckMicrOMEGABlock() == True:

            self.Relic_Density = self.Read_Block("MICROMEGAS",700)
            self.RD_difference = abs(self.Relic_Density-self.PlanckResult)

            self.SI_proton     = self.Read_Block("MICROMEGAS",201)
            self.SI_neutron    = self.Read_Block("MICROMEGAS",203)

            self.SD_proton     = self.Read_Block("MICROMEGAS",202)
            self.SD_neutron    = self.Read_Block("MICROMEGAS",204)

            self.sigmaV        = self.Read_Block("MICROMEGAS",306)


            self.DirectDetec_NormFactor   = min(1,self.Relic_Density/self.PlanckResult)
            self.IndirecDetec_NormFactor  = (self.Relic_Density/self.PlanckResult)**2


            self.NormSI_proton     = self.SI_proton*self.DirectDetec_NormFactor
            self.NormSI_neutron    = self.SI_neutron*self.DirectDetec_NormFactor

            self.SD_proton     = self.SD_proton*self.DirectDetec_NormFactor
            self.SD_neutron    = self.SD_neutron*self.DirectDetec_NormFactor

            self.sigmaV        = self.sigmaV*self.IndirecDetec_NormFactor



    def MassesFromMicrOMEGAs(self):

        if self.CheckMicrOMEGABlock() == True:
            self.MZp  = self.Read_Block("MICROMEGAS",401)
            self.MWp  = self.Read_Block("MICROMEGAS",402)

            self.Scot_DM  = self.Read_Block("MICROMEGAS",403)
            self.Scot_mu  = self.Read_Block("MICROMEGAS",404)
            self.Scot_tau = self.Read_Block("MICROMEGAS",405)

            self.MDD  = self.Read_Block("MICROMEGAS",406)
            self.MDS  = self.Read_Block("MICROMEGAS",407)
            self.MDB  = self.Read_Block("MICROMEGAS",408)
            
            self.mh1  = self.Read_Block("MICROMEGAS",409)
            self.mh2  = self.Read_Block("MICROMEGAS",410) 
            self.mh3  = self.Read_Block("MICROMEGAS",411)    

            self.mA1  = self.Read_Block("MICROMEGAS",412) 
            self.mA2  = self.Read_Block("MICROMEGAS",413)      

            self.mhp  = self.Read_Block("MICROMEGAS",414)
            self.mhm  = self.Read_Block("MICROMEGAS",415)            

    def MassConstraints(self):

        self.MZp_Bound = False
        self.Mh2_Bound = False
        self.Mh3_Bound = False

        if self.CheckMicrOMEGABlock() == True:
            if self.Read_Block("MICROMEGAS",401) > 1000.0 and self.Read_Block("MICROMEGAS",401) < 5500.0: 
                self.MZp_Bound = True
            if self.Read_Block("MICROMEGAS",410) < 500.0:
                self.Mh2_Bound = True
            if self.Read_Block("MICROMEGAS",411) < 2500.0:
                self.Mh3_Bound = True

#        self.CheckConstraints = self.MZp_Bound and self.Mh2_Bound
        self.CheckConstraints = self.MZp_Bound and self.Mh3_Bound and self.Mh2_Bound
#        self.CheckConstraints = self.Mh3_Bound and self.Mh2_Bound
        return self.CheckConstraints

    def RelicDensity_Constraint(self):

        if self.CheckMicrOMEGABlock() == True:
            self.Relic_Density = self.Read_Block("MICROMEGAS",700)
            if self.Relic_Density <= 5.0:
                self.Relic_Density_Bound = True
            else:
                self.Relic_Density_Bound = False

        else:
            self.Relic_Density_Bound = False

        return self.Relic_Density_Bound    

    def Parameters(self):
        self.ALRMINPUTSblock = self.allcontent.blocks["ALRMINPUTS"]

        self.aEWM1 = 127.9               # Inverse of the EW coupling constant at the Z pole
        self.aEW   = 1./self.aEWM1       # Electroweak coupling contant
        self.ee    = sqrt(4*pi*self.aEW) # Electric coupling constant

        self.gL    = 0.646482210
        self.sw    = self.ee/self.gL
        self.cw    = sqrt(1-self.sw**2)

        self.MW    = self.Read_Block("MASS",24)
        self.MZ    = self.Read_Block("MASS",23)
        self.vev   = (2*self.MW*self.sw)/self.ee

        self.tb    = self.Read_Block("ALRMINPUTS",6)
        self.sb    = self.tb/sqrt(1+self.tb**2)
        self.cb    = sqrt(1-self.sb**2)

        self.k     = (self.vev)*(self.sb)
        self.vL   = self.vev*self.cb

        self.vp    = self.Read_Block("ALRMINPUTS",8)
        self.vR    = sqrt(self.vp**2-self.k**2)

        if self.ALRMINPUTSblock.has_key(9) == True:
            self.gR    = self.Read_Block("ALRMINPUTS",9)
        else:
            self.gR    = self.gL

        self.gY    = self.ee/self.cw

        self.gBL   = (self.gY*self.gR)/sqrt(self.gR**2-self.gY**2)
        self.gL    = self.ee/self.sw

        self.sinPhi= self.gBL/sqrt((self.gBL**2)+(self.gR**2)) 
        self.cosPhi= self.gR/sqrt((self.gBL**2)+(self.gR**2))

        self.mu3   = self.Read_Block("ALRMINPUTS",7)

    def CheckZpMass(self, test_no):
        self.test_no = test_no

        if self.test_no == "test_0":

            self.MZpTerm1      = (self.gR**2/4)
            self.MZpTerm2      = (((self.gBL**2+self.gR**2)*self.k**2)/self.gR**2)
            self.MZpTerm3      = (((self.gR**2)*(self.vR**2))/((self.gBL**2)+(self.gR**2)))

            self.ZpMassSquared = self.MZpTerm1*(self.MZpTerm2 + self.MZpTerm3)
            self.ZpMass        = sqrt(self.ZpMassSquared)

            if self.ZpMass > 1000. and self.ZpMass < 5500.:
                ZpMassGuess = True
                return self.ZpMassGuess
            else:
                ZpMassGuess = False
                return self.ZpMassGuess

        if self.CheckMicrOMEGABlock() == True and self.test_no == "test_1":

            self.MZpTerm1      = (self.gR**2/4)
            self.MZpTerm2      = (((self.gBL**2+self.gR**2)*self.k**2)/self.gR**2)
            self.MZpTerm3      = (((self.gR**2)*(self.vR**2))/((self.gBL**2)+(self.gR**2)))

            self.ZpMassSquared = self.MZpTerm1*(self.MZpTerm2 + self.MZpTerm3)
            self.ZpMass        = sqrt(self.ZpMassSquared) 

            if self.CheckMicrOMEGABlock() == True:
#                return self.CalErrorPercent(self.MZp,self.ZpMass)
                return self.ZpMass,self.MZp
       
        if self.CheckMicrOMEGABlock() == True and self.test_no == "test_2":

            self.MLLSquared    = ((self.gL**2)*(self.vev**2))/(4*self.cw**2)
            self.MLRSquared    = -(self.gL*self.gR*(self.k**2)*self.cosPhi)/(2*self.cw)
            self.MRRSquared    = (self.gR**2/4)*(((self.k**2)*(self.cosPhi**2)) + ((self.vR**2)/(self.cosPhi**2)))

            self.tan2w         = (2*self.MLRSquared)/(self.MLLSquared-self.MRRSquared)

            self.sinw          = np.sin(np.arctan(self.tan2w)/2)

            self.cosw          = np.cos(np.arctan(self.tan2w)/2)

            self.sinw_Thesis   = abs(self.MLRSquared)/(sqrt(4*self.MLRSquared**2+(self.MRRSquared-self.MLLSquared+sqrt(4*self.MLRSquared**2+(self.MRRSquared-self.MLLSquared)**2)**2)))

            self.cosw_Thesis   = sqrt(1-self.sinw**2)

            self.sinw_Feyn     = 1./sqrt(1+(self.MRRSquared-self.MLLSquared+sqrt(4*self.MLRSquared**2+(self.MRRSquared-self.MLLSquared)**2))**2/(4*self.MLRSquared**2))

            self.cosw_Feyn     = -(self.MRRSquared-self.MLLSquared+sqrt(4*self.MLRSquared**2+(self.MRRSquared-self.MLLSquared)**2))/(2*self.MLRSquared*sqrt(1+(self.MRRSquared-self.MLLSquared+sqrt(4*self.MLRSquared**2+(self.MRRSquared-self.MLLSquared)**2))**2/(4*self.MLRSquared**2)))

            self.ZMassSquared  = (1./2)*(self.MLLSquared+self.MRRSquared-((self.MRRSquared-self.MLLSquared)*sqrt(1+self.tan2w**2)))
            self.ZpMassSquared = (1./2)*(self.MLLSquared+self.MRRSquared+((self.MRRSquared-self.MLLSquared)*sqrt(1+self.tan2w**2)))

            self.ZMass         = sqrt(self.ZMassSquared)
            self.ZpMass        = sqrt(self.ZpMassSquared)

#            return self.ZMass, self.MZ 
            return self.ZpMass,self.MZp

    def CalErrorPercent(self,experimental_val, theoretical_val):
        self.experimental_val = experimental_val
        self.theoretical_val  = theoretical_val
        
        self.ErrorPercent = abs((self.experimental_val-self.theoretical_val)/self.theoretical_val)*100

        return self.ErrorPercent

    def CheckWpMass(self):

        if self.CheckMicrOMEGABlock() == True:
            self.WpMass    = (self.gR/2)*(sqrt(self.vR**2 + self.k**2))        
            return self.WpMass, self.MWp

    def CheckMinimization(self):
        self.al1   = self.Read_Block("ALRMINPUTS",3)
        self.al2   = self.Read_Block("ALRMINPUTS",4)
        self.al3   = self.Read_Block("ALRMINPUTS",5) 

        self.al32  = self.al3 - self.al2
        self.al23  = self.al2 - self.al3
        self.al12  = self.al1 + self.al2 
        self.al13  = self.al1 + self.al3  

#        if self.al23 >= 0. and self.al12 >= 0. and self.al13 >= 0. : self.alphaCheck = True
#        if self.al12 >= 0. and self.al13 >= 0. : self.alphaCheck = True
#        if self.al23 >= 0.      : self.alphaCheck = True
        if self.al32 >= 0. and self.al12 >= 0. and self.al13 >= 0. : self.alphaCheck = True
        else                    : self.alphaCheck = False


        self.lm2   = self.Read_Block("ALRMINPUTS",1)
        self.lm3   = self.Read_Block("ALRMINPUTS",2)

        if self.lm2 <= 0.0 and self.lm3 >= 0.0: self.lambdaCheck = True
        else                                  : self.lambdaCheck = False

        self.CheckMini = self.lambdaCheck and self.alphaCheck
        return True

    def ReadChannels(self, ChannelFileName):
        self.ChannelFileName = ChannelFileName
        self.LoadChannelFile = pd.read_csv(self.ChannelFileName, skipinitialspace=True, header=1,sep="%", names=["Percent","Channels"])
        self.LoadChannelFile = self.LoadChannelFile.set_index(["Percent","Channels"])

    def CheckHiggsFunnel(self):
        HiggsFunnelExist = "~ne ~ne~ ->H0 H0 " in self.LoadChannelFile.index.levels[1]
        if HiggsFunnelExist == True:
            self.ChannelswithIndex = self.LoadChannelFile.index
            for index in range(len(self.ChannelswithIndex)):
                if self.ChannelswithIndex[index][1] == "~ne ~ne~ ->H0 H0 ":
                    self.HiggsFunnelPercentage = self.ChannelswithIndex[index][0]
            return self.HiggsFunnelPercentage 
        else:
            self.HiggsFunnelPercentage = None
            return self.HiggsFunnelPercentage

    def Erase(self,FilePathToErase):
        self.FilePathToErase = FilePathToErase
        os.remove(self.FilePathToErase)
        print "LHA File Removed!"

    def RD_difference(self):
        self.PlanckResult  = 0.1187        
        self.diff_RD = abs(self.Relic_Density-self.PlanckResult)

        return self.diff_RD

    def Check_RD_diff(self, RD_diff_list):
        self.RD_diff_list = RD_diff_list
        if len(self.RD_diff_list) >= 2:
            if self.RD_diff_list[-1] < self.RD_diff_list[-2]:
                self.Logic_RD_diff = True
                self.RD_diff_list.pop(0)
            else: self.Logic_RD_diff = False
        elif len(self.RD_diff_list) == 1:
            self.Logic_RD_diff = True

        return self.Logic_RD_diff

    def CheckHiggsMasses(self):

        self.mh0  = 125.0
        self.ma1  = sqrt((2*self.k**2)*self.lm2-(self.vL**2+self.vR**2)*(self.al2-self.al3)-((self.vL*self.vR*self.mu3)/(sqrt(2)*self.k)))
        self.mh1  = self.ma1


        self.a0    = 2*(self.vL**2+self.vR**2)*self.lm3-(((self.vL**2)*(self.vR**2)+(self.k**2)*(self.vL**2+self.vR**2))*self.mu3)/(sqrt(2)*self.vL*self.vR*self.k)
        self.a1    = 2*self.k**2

        self.b0    = ((self.vL**2+self.vR**2)*(4*(self.k**3)*self.vL*self.vR*(self.al1+self.al2)**2+sqrt(2)*(self.vL**2)*(self.vR**2)*self.lm3*self.mu3)+sqrt(2)*(self.k**2)*(4*(self.vL**2)*(self.vR**2)*(self.al1+self.al2)+((self.vL**2-self.vR**2)**2)*self.lm3)*self.mu3)/(self.k*self.vL*self.vR)
        self.b1    = (self.vL**2+self.vR**2)*(4*(self.k**3)*self.vL*self.vR*(-self.lm3)+sqrt(2)*(self.k**4)*self.mu3)/(self.k*self.vL*self.vR)

        self.c0    = 2*sqrt(2)*(self.k**3)*((self.vL**2-self.vR**2)**2)*((self.al1+self.al2)**2)*self.mu3/(self.vL*self.vR)
        self.c1    = -2*sqrt(2)*(self.k**3)*((self.vL**2-self.vR**2)**2)*self.lm3*self.mu3/(self.vL*self.vR)

        self.lm1   = -(-(self.mh0**6)+(self.a0)*(self.mh0**4)+self.b0*(self.mh0**2)+self.c0)/(self.a1*(self.mh0**4)+self.b1*(self.mh0**2)+self.c1)

        self.a     = (self.a1*self.lm1) + self.a0
        self.b     = (self.b1*self.lm1) + self.b0

        self.mh2  = (1.0/sqrt(2))*sqrt((self.a-(self.mh0**2)-sqrt((self.a-(self.mh0**2))**2+4*(self.b+(self.mh0**2)*(self.a-self.mh0**2)))))
        self.mh3  = sqrt(self.a-(self.mh0**2)-(self.mh2**2))
        self.ma2  = sqrt(-(((self.vL**2)*self.vR**2+(self.k**2)*(self.vL**2+self.vR**2))*self.mu3)/(sqrt(2)*self.k*self.vL*self.vR))
        self.mhp1 = sqrt(-(self.k*self.vL*(self.al2-self.al3)+(self.mu3*self.vR)/sqrt(2))*(self.vev**2/(self.k*self.vL)))
        self.mhm2 = sqrt(-(self.k*self.vR*(self.al2-self.al3)+(self.mu3*self.vL)/sqrt(2))*(self.vp**2/(self.k*self.vR)))

    def CheckHiggsMixing(self):
        self.fx = (2*(self.mh0**4)*self.vL*self.vR+(self.mh0**2)*(self.vL**2+self.vR**2)*(sqrt(2)*self.k*self.mu3-4*self.vL*self.vR*self.lm3)-2*sqrt(2)*self.k*((self.vL**2-self.vR**2)**2)*self.lm3*self.mu3)/(self.vR*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))

        self.gx = (self.vL*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vR**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vR**2)*self.lm3)*(self.vL**2-self.vR**2)*self.mu3))/(self.vR*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))

        self.THP0 = self.fx/sqrt(1+self.fx**2+self.gx**2)
        self.THL0 = self.gx/sqrt(1+self.fx**2+self.gx**2)
        self.THR0 = 1.0/sqrt(1+self.fx**2+self.gx**2)

        self.fx2   = (2*(self.mh2**4)*self.vL*self.vR+(self.mh2**2)*(self.vL**2+self.vR**2)*(sqrt(2)*self.k*self.mu3-4*self.vL*self.vR*self.lm3)-2*sqrt(2)*self.k*((self.vL**2-self.vR**2)**2)*self.lm3*self.mu3)/(self.vR*((self.mh2**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))
        self.gx2   = (self.vL*((self.mh2**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vR**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vR**2)*self.lm3)*(self.vL**2-self.vR**2)*self.mu3))/(self.vR*((self.mh2**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))

        self.THP2 = (self.fx2*(1+self.gx**2)-self.fx*(1+self.gx*self.gx2))/sqrt((1+self.fx**2+self.gx**2)*((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2)))
        self.THL2 = (-(1+self.fx*self.fx2)*self.gx+self.gx2+(self.fx**2)*self.gx2)/sqrt((1+self.fx**2+self.gx**2)*((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2)))
        self.THR2 = (self.fx**2-self.fx*self.fx2+self.gx*(self.gx-self.gx2))/sqrt((1+self.fx**2+self.gx**2)*((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2)))

        self.fx3  = (2*(self.mh3**4)*self.vL*self.vR+(self.mh3**2)*(self.vL**2+self.vR**2)*(sqrt(2)*self.k*self.mu3-4*self.vL*self.vR*self.lm3)-2*sqrt(2)*self.k*((self.vL**2-self.vR*2)**2)*self.lm3*self.mu3)/(self.vR*((self.mh3**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3)) 
        self.gx3  = (self.vL*((self.mh3**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vR**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vR**2)*self.lm3)*(self.vL**2-self.vR**2)*self.mu3))/(self.vR*((self.mh3**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))
        self.sgn  = abs(self.fx2*self.gx-self.fx3*self.gx-self.fx*self.gx2+self.fx3*self.gx2+self.fx*self.gx3-self.fx2*self.gx3)/(self.fx2*self.gx-self.fx3*self.gx-self.fx*self.gx2+self.fx3*self.gx2+self.fx*self.gx3-self.fx2*self.gx3)

        self.THP3 = self.sgn*(-self.gx+self.gx2)/sqrt((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2))
        self.THL3 = -self.sgn*(-self.fx+self.fx2)/sqrt((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2))
        self.THR3 = self.sgn*(self.fx2*self.gx-self.fx*self.gx2)/sqrt((self.fx2**2)*(1+self.gx**2)+(self.gx-self.gx2)**2-2*self.fx*(self.fx2+self.fx2*self.gx*self.gx2)+(self.fx**2)*(1+self.gx2**2))


    def ZpMassLimit(self):
        self.given_gR = self.gR 

        self.gR_values_given = [0.37, self.gL]
        self.Zp_values_given = [5000., 4000.]

        self.y1 = interp1d(self.gR_values_given, self.Zp_values_given)
        self.Zp_limit = self.y1(self.given_gR)
        self.Zp_limit = self.Zp_limit.tolist()

        return self.Zp_limit

    def CheckZpMassLimit(self):
        self.ZpMassLimit()

        if self.CheckMicrOMEGABlock() == True:
            if self.MZp < self.ZpMassLimit():
                self.LogicZpMassLimit = False
            elif self.MZp >= self.ZpMassLimit():
                self.LogicZpMassLimit = True
        else:
            self.LogicZpMassLimit = False

        return self.LogicZpMassLimit
