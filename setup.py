import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'include_files':['icone.ico']}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, icon="icone.ico", target_name="PDF-to-Word-Converter")
]

setup(name='PDF-to-Word-Converter',
      version = '1.0',
      description = 'A simple PDF to Word converter developed in Python.',
      options = {'build_exe': build_options},
      executables = executables)
