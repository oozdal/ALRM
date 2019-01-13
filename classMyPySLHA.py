import os
import pyslha

class classMyPySLHA():
    def __init__(self):
        pass        

    def CheckLHAexist(self,LHAPath):
        return os.path.isfile(LHAPath)

    def LoadLHAFile(self, LHAPath):
        self.allcontent = pyslha.read(LHAPath, ignoreblocks=['SPINFO'])

    def WriteNewLHAFile(self, newLHAPath, newLHAcontent, precision_val):
        self.newLHA = pyslha.writeSLHAFile(newLHAPath, newLHAcontent, precision=precision_val)

