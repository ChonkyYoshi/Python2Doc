from cx_Freeze import setup, Executable

includefiles = ['letters.ini']
includes = []
excludes = []

setup(
    name='Illustrator2Doc',
    version='0.2',
    description='Python GUI App to prep/clean up Illustrator files',
    author='Enzo Agosta',
    author_email='agosta.enzowork@gmail.com',
    options={'build_exe': {'includes': includes, 'excludes': excludes,
             'include_files': includefiles}},
    executables=[Executable('Main.py', base="Win32GUI")]
)
