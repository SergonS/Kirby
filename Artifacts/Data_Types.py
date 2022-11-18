from enum import Enum

class Data_Type(Enum):

    # Datatypes accepted
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"
    INVALID = "invalid"

# Get a string and returning it to a datatype
def strToType(type: str) -> Data_Type:
    if (type == Data_Type.INT):
        return Data_Type.INT
    elif (type == Data_Type.FLOAT):
        return Data_Type.FLOAT
    elif (type == Data_Type.FLOAT):
        return Data_Type.FLOAT
    elif (type == Data_Type.FLOAT):
        return Data_Type.FLOAT
    else: 
        return Data_Type.INVALID
    