from Artifacts.Variables import Variable

# Class to access easily a function
class Function:
    # Name of function
    name: str
    # Datatype of function (void, int, float, boolean)
    data_type: str
    # Boolean to know if it has a return variable
    returnVar: bool
    # The index of the quad where function starts
    initQuad: int
    # Address where the function is located 
    addr: int

    # Initialize a function 
    def __init__(self, name: str, data_type: str = "void"):
        self.name = name
        self.data_type = data_type

        self.params = {}
        self.vars = {}
        self.initQuad = 0

        if data_type == "void":
            self.returnVar = False
        else:
            self.returnVar = True

        self.addr = 0

    # Add a variable object to the dictionary of parameters
    def addParam(self, var: Variable):
        if var.name in self.params:
            print("Parameter already in function")
        else:
            self.params[var.name] = var

    # Add a variable object to the dictionary of parameters
    def addVar(self, var: Variable):
        if var.name in self.vars:
            print("Variable already in function")
        else:
            self.vars[var.name] = var

    # Set the initial quad
    def addIQuad(self, quad: int):
        self.initQuad = quad
        
    # Print the dictionary of parameters
    def showParams(self):
        if self.params is not None:
            for param in self.params:
                print(param)
    
    # Print the dictionary of variables
    def showVars(self):
        if self.vars is not None:
            for var in self.vars:
                print(var)

    # Get the number of parameters of function
    def getNParams(self) -> int:
        return len(self.params)

    # Print a function in a legible way
    def __repr__(self) -> str:
        return f'Function({self.name}, {self.data_type}, with {len(self.params)} args and {len(self.vars)} vars, starting at Quad #{self.initQuad})'


    