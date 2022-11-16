from Artifacts.Data_Types import Data_Type
from Artifacts.Variables import Variable

class Directory_Vars:

    def __init__(self):
        self.directory = {}

    def getVar(self, name: str) -> Variable:
        return self.directory[name]

    def appendToDirectory(self, name: str, data_type: str, addr: int = 0, dimensions: list = None, spaces: int = 0, scope: str = "global"):
        self.directory[name] = Variable(name, data_type, addr, dimensions, spaces, scope)
        

    def getDirectory(self) -> dict:
        return self.directory

    def showDirectory(self):
        if self.directory is not None:
            for var in self.directory:
                #print(self.directory[var].scope + " " + self.directory[var].data_type + " " + self.directory[var].name + " at address " + str(self.directory[var].addr) + " with a value of " + self.directory[var].value) 
                print(self.directory[var])
        else:
            print("Directory is empty.")

    def hasVar(self, name: str) -> bool:
        hasKey = False

        if name in self.directory:
            hasKey = True
        
        return hasKey