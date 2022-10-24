:: This batch script disable displaying commands entered in Command Prompt, 
:: change directory to project folder (to access config.ini), run Python script with specified Python interpreter

:: "echo off" disable display for the whole script except itself (add "@" to apply disable display to itself)
@echo off

:: Change directory to project folder
cd "C:\Users\Clement\Desktop\Programming Projects\file_downloads_manager"

:: Run Python script with specified Python interpreter
"C:\Users\Clement\Desktop\Programming Projects\file_downloads_manager\venv\Scripts\python.exe" "C:\Users\Clement\Desktop\Programming Projects\file_downloads_manager\main.py"


