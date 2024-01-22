from enum import Enum


class IdentificationMethod(Enum):
    '''
    Document types that can be used for identification.
    '''
    StudentId = 1
    EmployeeId = 2
    AadharCard = 3
    PANCard = 4
