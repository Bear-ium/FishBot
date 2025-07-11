@echo off

set "VENVDIR=venv"
set "VENV_PATH=%CD%\%VENVDIR%"
set "ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "REQPATH=%CD%\requirements.txt"

if NOT EXIST "%ACTIVATE_PATH%" (
    echo Creating VirtualEnvironment...
    py -.12 -m venv "%VENV_PATH%"
) ELSE (
  echo VirtualEnvironment already exists, activating...
)

call "%ACTIVATE_PATH%"

if EXIST "%REQPATH%" (
    echo Installing requirements..
    pip install -r "%REQPATH%"
)

cmd /k