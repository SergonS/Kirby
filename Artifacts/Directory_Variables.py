from Artifacts.Data_Types import Data_Type
from Artifacts.Variables import Variable

# Dictionary for variables
class Directory_Vars:

    # Initialize an empty dictionary
    def __init__(self):
        self.directory = {}

    # Receives a name and searches the dictionary for a variable with said name
    def getVar(self, name: str) -> Variable:
        return self.directory[name]

    # Add a variable object to the dictionary with its name as its key
    def appendToDirectory(self, name: str, data_type: str, addr: int = 0, dimensions: list = None, spaces: int = 0, scope: str = "global"):
        self.directory[name] = Variable(name, data_type, addr, dimensions, spaces, scope)
        
    # Get the whole dictionary
    def getDirectory(self) -> dict:
        return self.directory

    # Print the dictionary with its parameters if any
    def showDirectory(self):
        if self.directory is not None:
            for var in self.directory:
                #print(self.directory[var].scope + " " + self.directory[var].data_type + " " + self.directory[var].name + " at address " + str(self.directory[var].addr) + " with a value of " + self.directory[var].value) 
                print(self.directory[var])
        else:
            print("Directory is empty.")

    # Verify if there is a variable with a name given by the parameter
    def hasVar(self, name: str) -> bool:
        hasKey = False

        if name in self.directory:
            hasKey = True
        
        return hasKey