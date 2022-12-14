from VM.Borderlands import Borderland

# Table that stores globals
class G_Table:

    # Using Borderlands to get the size of each datatype
    delimitation = Borderland().area

    # Dictionaries for each kind of datatype
    g_integers = {}
    g_floats = {}
    g_strings = {}
    g_booleans = {}

    # Simple Setters and Getters for each datatype

    def addInteger(self, value: str, addr: int) -> bool:
        if value not in self.g_integers:
            self.g_integers[value] = addr
            return True
        else:
            return False

    def getInteger(self, value: str) -> int:
        return self.g_integers[value]

    def addFloat(self, value: str, addr: int) -> bool:
        if value not in self.g_floats:
            self.g_floats[value] = addr
            return True
        else:
            return False

    def getFloat(self, value: str) -> int:
        return self.g_floats[value]

    def addString(self, value: str, addr: int) -> bool:
        if value not in self.g_strings:
            self.g_strings[value] = addr
            return True
        else:
            return False
    
    def getString(self, value: str) -> int:
        return self.g_strings[value]

    def addBoolean(self, value: str, addr: int) -> bool:
        if value not in self.g_booleans:
            self.g_booleans[value] = addr
            return True
        else:
            return False

    def getBoolean(self, value: str) -> int:
        return self.g_booleans[value]

    # Return table of globals
    def getGTable(self) -> dict:
        table = {
            "integer": self.g_integers,
            "float": self.g_floats,
            "string": self.g_strings,
            "boolean": self.g_booleans
        }
        return table

    # Print table just for debugging
    def printGTable(self):
        print("Integers:")
        print(self.g_integers)
        print()
        print("Floats:")
        print(self.g_floats)
        print()
        print("Strings:")
        print(self.g_strings)
        print()
        print("Booleans:")
        print(self.g_booleans)
        print()