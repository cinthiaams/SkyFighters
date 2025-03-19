from cx_Freeze import Executable, setup

executables = [Executable("main.py")]

setup(
    name="SkyFighters",
    version="1.0",
    description="Sky Shooter App",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
