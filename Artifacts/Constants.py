from VM.Borderlands import Borderland

# Table that stores constants
class C_Table:

    # Using Borderlands to get the size of each datatype
    delimitation = Borderland().area

    # Dictionaries for each kind of datatype
    c_integers = {}
    c_floats = {}
    c_strings = {}
    c_booleans = {}

    # Dictionaries for each kind of datatype

    def addInteger(self, value: str, addr: int) -> bool:
        if value not in self.c_integers:
            self.c_integers[value] = addr
            return True
        else:
            return False

    def getInteger(self, value: str) -> int:
        return self.c_integers[value]

    def addFloat(self, value: str, addr: int) -> bool:
        if value not in self.c_floats:
            self.c_floats[value] = addr
            return True
        else:
            return False

    def getFloat(self, value: str) -> int:
        return self.c_floats[value]

    def addString(self, value: str, addr: int) -> bool:
        if value not in self.c_strings:
            self.c_strings[value] = addr
            return True
        else:
            return False

    def getString(self, value: str) -> int:
        return self.c_strings[value]

    def addBoolean(self, value: str, addr: int) -> bool:
        if value not in self.c_booleans:
            self.c_booleans[value] = addr
            return True
        else:
            return False

    def getBoolean(self, value: str) -> int:
        return self.c_booleans[value]

    # Return table of constants
    def getCTable(self) -> dict:
        table = {
            "integer": self.c_integers,
            "float": self.c_floats,
            "string": self.c_strings,
            "boolean": self.c_booleans
        }
        return table

    # Print table just for debugging
    def printCTable(self):
        print("Integers:")
        print(self.c_integers)
        print()
        print("Floats:")
        print(self.c_floats)
        print()
        print("Strings:")
        print(self.c_strings)
        print()
        print("Booleans:")
        print(self.c_booleans)
        print()