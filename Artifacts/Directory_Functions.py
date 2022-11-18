from Artifacts.Directory_Variables import Directory_Vars
from Artifacts.Functions import Function

# Dictionary for Functions
class Directory_Func:
    
    # Initialize an empty dictionary
    def __init__(self):
        self.directory = {}

    # Receives a name and searches the dictionary for a function with said name
    def getFunc(self, name: str) -> Function:
        return self.directory[name]

    # Add a function object to the dictionary with its name as its key
    def addFunc(self, function: Function):
        self.directory[str(function.name)] = function

    # Get the whole dictionary
    def getDirectory(self) -> dict:
        return self.directory

    # Print the dictionary with its parameters if any
    def showDirectory(self):
        if self.directory is not None:
            for func in self.directory:
                print(self.directory[func])
                self.directory[func].showParams()

    # Verify if there is a function with a name given by the parameter
    def hasFunc(self, name: str) -> bool:
        hasKey = False

        if name in self.directory:
            hasKey = True
        
        return hasKey