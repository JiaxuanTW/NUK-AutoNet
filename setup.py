from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None

executables = [Executable("source.py", base=base, icon='icon.ico')]

packages = []
include_files=['icon.png']
options = {
    'build_exe': {
        'packages':packages,
        'include_files': include_files
    },

}

setup(
    name = "NUK AutoNet",
    options = options,
    version = "1.1",
    description = 'Automatically login the domitory network system',
    executables = executables
)