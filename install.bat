@echo off
title Install ZoomBoard for Windows

echo Installing Python 3.8.5
cd python
echo.
echo If you have already installed Python close the installer
echo Click the box next to Add Python 3.8 to PATH
echo and uncheck the box next to Install launcher for all users (Recommended)
echo Then click Install Now
py385.exe

echo Installing Requirements...
pip install -r requirements.txt

echo Now type the URL of the subject after the comma in the subject.csv file and make sure you start edit-csv.bat
echo and not the file itself

notepad.exe subject.csv