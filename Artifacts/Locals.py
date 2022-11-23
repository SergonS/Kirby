from VM.Borderlands import Borderland

# Table that stores locals
class L_Table:

    # Using Borderlands to get the size of each datatype
    delimitation = Borderland().area

    # Dictionaries for each kind of datatype
    l_integers = {}
    l_floats = {}
    l_strings = {}
    l_booleans = {}

    # Dictionaries for each kind of datatype

    def addInteger(self, value: str, addr: int) -> bool:
        if value not in self.l_integers:
            self.l_integers[value] = addr
            return True
        else:
            return False

    def getInteger(self, value: str) -> int:
        return self.l_integers[value]

    def addFloat(self, value: str, addr: int) -> bool:
        if value not in self.l_floats:
            self.l_floats[value] = addr
            return True
        else:
            return False

    def getFloat(self, value: str) -> int:
        return self.l_floats[value]

    def addString(self, value: str, addr: int) -> bool:
        if value not in self.l_strings:
            self.l_strings[value] = addr
            return True
        else:
            return False
    
    def getString(self, value: str) -> int:
        return self.l_strings[value]

    def addBoolean(self, value: str, addr: int) -> bool:
        if value not in self.l_booleans:
            self.l_booleans[value] = addr
            return True
        else:
            return False

    def getBoolean(self, value: str) -> int:
        return self.l_booleans[value]

    # Return table of locals
    def getLTable(self) -> dict:
        table = {
            "integer": self.l_integers,
            "float": self.l_floats,
            "string": self.l_strings,
            "boolean": self.l_booleans
        }
        return table

    # Reset every local counter to 0
    def resetLocals(self):
        self.l_integers.clear()
        self.l_floats.clear()
        self.l_strings.clear()
        self.l_booleans.clear()

    # Print table just for debugging
    def printLTable(self):
        print("Integers:")
        print(self.l_integers)
        print()
        print("Floats:")
        print(self.l_floats)
        print()
        print("Strings:")
        print(self.l_strings)
        print()
        print("Booleans:")
        print(self.l_booleans)
        print()