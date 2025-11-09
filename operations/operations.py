import ctypes
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
folder_modified = script_directory.replace("\\", "/")

cpplibrary = ctypes.CDLL(f"{folder_modified}/sum.dll")
clibrary = ctypes.CDLL(f"{folder_modified}/difference.dll")

def add(a, b):
    """
    This function calls a C++ library called 'sum.dll' to
    add a and b in python at the speed of C++
    """
    
    result = cpplibrary.sum(a, b)
    
    return result


def subtract(a, b):
    
    """
    This function calls a C library called 'subtract.dll'
    to subtract a and b in python at the speed of C. 
    """

    result = clibrary.difference(a, b)
    
    return result

