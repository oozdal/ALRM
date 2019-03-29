import os
import shutil

class MyMicrOMEGAs():
    def __init__(self):
        pass

    def RenameAndCopy(self,currentLHAFilePath, newLHAFilePath):
        self.currentLHAFullPath  = os.path.abspath(currentLHAFilePath)
        self.currentLHAdirPath   = os.path.dirname(self.currentLHAFullPath)
        self.currentLHAFileName  = os.path.basename(self.currentLHAFullPath)

        self.newLHAFullPath      = os.path.abspath(newLHAFilePath)
        self.newLHAdirPath       = os.path.dirname(self.newLHAFullPath)
        self.newLHAFileName      = os.path.basename(self.newLHAFullPath)
    
        self.old_file = os.path.join(self.currentLHAdirPath, self.currentLHAFileName)
        self.new_file = os.path.join(self.newLHAdirPath, self.newLHAFileName)
        shutil.copy2(self.old_file, self.new_file)

    def RunMicrOMEGAs(self, LHAInput):
         os.system("./../../../hepwork/micromegas_5.0.8/ALRM_gRfree_coanni/myOmega "+str(LHAInput))
#        try:
#            os.system("./../../hepwork/micromegas_5.0.8/ALRM_gRfree_coanni/myOmega "+str(LHAInput))
#        except KeyError and AttributeError:
#            print "can not calculate a particular parameter!"

    def LHAwithDM(self, PathLHAfile, PathMicrOMEGAsResult, PathLHAfileWithDM):
        filenames = [PathLHAfile, PathMicrOMEGAsResult]
        with open(PathLHAfileWithDM, 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

