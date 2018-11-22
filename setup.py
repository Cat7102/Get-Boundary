from cx_Freeze import setup, Executable
import sys
import os
os.environ['TCL_LIBRARY'] = 'F:\\Language\\Python3\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'F:\\Language\\Python3\\tcl\\tk8.6'

build_exe_options = {'packages': ['numpy'], 'excludes': []}

setup(  name = 'Get Boundary',
        version = '1.0',
        description = 'Image processing and get information from image.',
        options = {'build_exe': build_exe_options},
        executables = [Executable('imagedraw.py',base = "Win32GUI")])