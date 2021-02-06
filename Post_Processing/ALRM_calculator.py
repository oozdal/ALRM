from math import *
from scipy.interpolate import interp1d

class ALRM_calculator:
    def __init__(self):
        pass

    def parameters(self,gR,vp,tb,lm2,lm3,al1,al2,al3,mu3):
        self.aEWM1 = 127.9
        self.aEW   = 1.0/self.aEWM1
        self.ee    = sqrt(4*pi*self.aEW)

        self.gL = 0.646482210
        self.gR = gR

        self.sw = self.ee/self.gL
        self.cw = sqrt(1-self.sw**2)

        self.gY  = self.ee/self.cw
        self.gBL = (self.gY*self.gR)/(sqrt(self.gR**2-self.gY**2))

        self.sp  = self.gY/self.gR
        self.cp  = self.gY/self.gBL

        self.MW  = 80.385
        self.vev = (2*self.MW*self.sw)/self.ee

        self.vp   = vp
        self.tb   = tb
        self.sb   = self.tb/(sqrt(1+self.tb**2))
        self.cb   = sqrt(1-self.sb**2)

        self.k    = self.vev*self.sb
        self.vL   = self.vev*self.cb
        self.vR   = sqrt(self.vp**2-self.k**2)

        self.tz   = self.k/self.vR

        self.lm2  = lm2
        self.lm3  = lm3

        self.al1  = al1
        self.al2  = al2
        self.al3  = al3

        self.mu3  = mu3

    def CheckWMasses(self):
        self.MW2_Theory = ((self.gL**2)*(self.vev**2))/4
        self.MW_Theory  = sqrt(self.MW2_Theory)

        self.MWp2 = ((self.gR**2)*(self.vp**2))/4
        self.MWp  = sqrt(self.MWp2)


    def CheckWMasses(self):
        self.MW2_Theory = ((self.gL**2)*(self.vev**2))/4
        self.MW_Theory  = sqrt(self.MW2_Theory)

        self.MWp2 = ((self.gR**2)*(self.vp**2))/4
        self.MWp  = sqrt(self.MWp2)

    def CheckZZMixing(self):
        self.MLL = ((self.gL**2)*(self.vev**2))/(4*self.cw**2)

        self.MRR_vL_term = ((self.vL**2)/4.0)*((self.gBL**2)*(self.sp**2))        
        self.MRR = (self.gR**2/4.0)*(((self.k**2)*(self.cp**2)) + (self.vR**2/self.cp**2)) + self.MRR_vL_term 

        self.MLR = ((self.gL*self.gR)*((self.vev*self.sp)**2 - self.k**2))/(4*self.cw*self.cp)

        self.MLL_Feyn = (self.MW**2)/(1-self.sw**2)
        self.MLR_Feyn = ((self.MW**2)*((self.tb**2)-(self.sw**2)*(1+2*self.tb**2)))/(sqrt(1-2*self.sw**2)*(-1+self.sw**2)*(1+self.tb**2))
        self.MRR_Feyn = ((self.MWp**2)*((-1+self.sw**2)**2)*(1+self.tb**2)+(self.MW**2)*(self.sw**2)*(self.sw**2+(-2+3*self.sw**2)*self.tb**2))/((-1+self.sw**2)*(-1+2*self.sw**2)*(1+self.tb**2))

        self.MLL_Thesis = ((self.gL**2)*(self.vev**2))/(4*self.cw**2)
        self.MLR_Thesis = ((self.gL**2)*(((self.vev**2)*(self.sw**2))-((self.k**2)*(self.cw**2))))/(4*(self.cw**2)*(sqrt(self.cw**2-self.sw**2)))
        self.MRR_Thesis = ((self.gL**2)*(2*(self.vev**2)*self.sw**4 + 2*(self.vp**2)*self.cw**4 - (self.k**2)*(2*self.sw*self.cw)**2))/(8*(self.cp**2)*(self.cw**2 - self.sw**2))

        self.MLR_Thesis2 = ((self.gL*self.gR)*(((self.vev**2)*(self.sw**2))-((self.k**2)*(self.cw**2))))/(4*(self.cw**2)*(sqrt(self.cw**2-self.sw**2)))

        self.t2t = abs((2*self.MLR)/(self.MLL-self.MRR))

#        self.ct = -(self.MRR-self.MLL+sqrt(4*self.MLR**2+(self.MRR-self.MLL)**2))/(2*self.MLR*sqrt(1+(self.MRR-self.MLL+sqrt(4*self.MLR**2+(self.MRR-self.MLL)**2))**2/(4*self.MLR*2)))
        self.st = 1.0/sqrt(1+(self.MRR-self.MLL+sqrt(4*self.MLR**2+(self.MRR-self.MLL)**2))**2/(4*self.MLR**2))

        self.ct_check = cos(atan(self.t2t)/2.0)
        self.st_check = sin(atan(self.t2t)/2.0)

    def CheckZMasses(self):
        self.MZ  = 91.1876 
        self.MZp = sqrt(self.MLL+self.MRR-self.MZ**2)

#        self.MZ_Check  = sqrt((1.0/2.0)*(self.MLL+self.MRR - (self.MRR-self.MLL)*sqrt(1+self.t2t**2)))
        self.MZp_Check = sqrt((1.0/2.0)*(self.MLL+self.MRR + (self.MRR-self.MLL)*sqrt(1+self.t2t**2)))

        self.MZp_Check_2 = sqrt(((self.gR**2/4.0)*((self.k*self.cp)**2 + (self.vR**2/self.cp**2))) + ((self.gBL*self.sp)**2/4.0)*(self.vL)**2)

        self.MZp_Check_3 = sqrt((self.gR**2/4.0)*((self.vev*self.cp)**2 + (self.vR**2/self.cp**2) - ((self.vL**2)*(self.cp**2-self.sp**2))/self.cp**2))

    def CheckHiggsMasses(self):

        try:
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

        except ValueError:
            self.mh1=None; self.ma1=None; self.mh2=None; self.mh3=None; self.ma2=None; self.mhp1=None; self.mhm2=None

    def CheckHiggsMixing(self):
        self.fx = (2*(self.mh0**4)*self.vL*self.vR+(self.mh0**2)*(self.vL**2+self.vR**2)*(sqrt(2)*self.k*self.mu3-4*self.vL*self.vR*self.lm3)-2*sqrt(2)*self.k*((self.vL**2-self.vR**2)**2)*self.lm3*self.mu3)/(self.vR*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))

        self.gx = (self.vL*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vR**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vR**2)*self.lm3)*(self.vL**2-self.vR**2)*self.mu3))/(self.vR*((self.mh0**2)*(4*self.k*self.vL*self.vR*(self.al1+self.al2)+sqrt(2)*(self.vL**2)*self.mu3)+2*sqrt(2)*((self.k**2)*(self.al1+self.al2)+(self.vL**2)*self.lm3)*(self.vR**2-self.vL**2)*self.mu3))

        self.THP0 = self.fx/sqrt(1+self.fx**2+self.gx**2)
        self.THL0 = self.gx/sqrt(1+self.fx**2+self.gx**2)
        self.THR0 = 1.0/sqrt(1+self.fx**2+self.gx**2)


    def Check_MassBounds(self):

        self.MZp_Bound = None
        self.Mh2_Bound = None
        self.Mh3_Bound = None

        if self.MZp > 1000.0 and self.MZp < 5500.0:
            self.MZp_Bound = True
        if self.mh2 < 500.0:
            self.Mh2_Bound = True
        if self.mh3 < 2500.0:
            self.Mh3_Bound = True

        self.CheckConstraints = self.MZp_Bound and self.Mh3_Bound and self.Mh2_Bound
        return self.CheckConstraints

    def Check_Minimization(self):

        self.al32  = self.al3 - self.al2
        self.al23  = self.al2 - self.al3
        self.al12  = self.al1 + self.al2
        self.al13  = self.al1 + self.al3

        if self.al32 >= 0. and self.al12 >= 0. and self.al13 >= 0. : self.alphaCheck = True
        else                    : self.alphaCheck = False

        if self.lm2 <= 0.0 and self.lm3 >= 0.0: self.lambdaCheck = True
        else                                  : self.lambdaCheck = False

        self.CheckMini = self.lambdaCheck and self.alphaCheck
        return True

    def ZpMassLimit(self):
        self.given_gR = self.gR

        self.gR_values_given = [0.37, self.gL]
        self.Zp_values_given = [5000., 4000.]

        self.y1 = interp1d(self.gR_values_given, self.Zp_values_given)
        self.Zp_limit = self.y1(self.given_gR)
        self.Zp_limit = self.Zp_limit.tolist()

        return self.Zp_limit

    def Check_ZpMassLimit(self):
        self.ZpMassLimit()

        self.LogicZpMassLimit = None

        if self.MZp < self.ZpMassLimit():
            self.LogicZpMassLimit = False
        elif self.MZp >= self.ZpMassLimit():
            self.LogicZpMassLimit = True

        return self.LogicZpMassLimit

