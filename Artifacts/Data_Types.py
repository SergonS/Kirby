from enum import Enum

class Data_Type(Enum):

    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    INVALID = "invalid"

def strToType(type: str) -> Data_Type:
    if (type == Data_Type.INT):
        return Data_Type.INT
    elif (type == Data_Type.FLOAT):
        return Data_Type.FLOAT
    elif (type == Data_Type.STRING):
        return Data_Type.STRING
    elif (type == Data_Type.BOOL):
        return Data_Type.BOOL
    else: 
        return Data_Type.INVALID
    