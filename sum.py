import ctypes
import os

folder = os.getcwd()
folder_modified = folder.replace("\\", "/")

cpplibrary = ctypes.CDLL(f"{folder_modified}/sum.dll")
clibrary = ctypes.CDLL(f"{folder_modified}/subtract.dll")

sum = cpplibrary.sum(2, 2)

diff = clibrary.subtract(10, 5)

print(sum)
print(diff)