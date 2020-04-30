# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable
import matplotlib

executable = Executable( script = "zeiss_converter.py", base = "Win32GUI", icon='image/icon.ico' )

# Add certificate to the build
options = {
"build_exe": {
"include_files" : ["image/logo_add.png", "image/logo_plot.png", "image/logo_validation.png", "image/icon.png"],
"includes":["mpl_toolkits", "matplotlib.backends.backend_tkagg"]
}
}

setup(
    name = "Algorithm",
    version = "3.1",
    description = "Algorithm help tool.",
    options = options,
    executables = [executable] )