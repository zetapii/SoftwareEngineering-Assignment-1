from enum import Enum 

class VehicleCondition(Enum):
    '''
    Types of vehicle conditions.
    '''
    ReadyToUse = 1
    NeedRepair = 2
    NeedReplacement = 3