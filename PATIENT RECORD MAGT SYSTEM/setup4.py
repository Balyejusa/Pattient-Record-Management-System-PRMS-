from cx_Freeze import setup, Executable
import sys
#import matplotlib
#import Pmw
import tkinter
#import numpy
import os
os.environ['TCL_LIBRARY'] = r'C:\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python35\tcl\tk8.6'

#includes      = []
#additional_mods = ['numpy.core._methods', 'numpy.lib.format']
include_files =[r"C:\Python35\DLLs\tcl86t.dll",r"C:\Python35\DLLs\tk86t.dll","Agro-chemicals","Banana","Beakers and fungicides","Beans","Cabbages","Maize","Tomato"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["tkinter"], "include_files": include_files}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "win32"
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Agro-chemical solutions",
    version = "1.0",
    description = "Sample cx_Freeze Tkinter script",
    options = {"build_exe": build_exe_options},
    executables = [Executable("project1.py" ,base = base)])

##setup(  name = "diet",
##        version = "1.0",
##        description = "My GUI application!",
##        options = {"build_exe": build_exe_options},
##        executables = [Executable("newstyle.py", base=base)])
