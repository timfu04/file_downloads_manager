# File Downloads Manager
An automation Python script that moves and sorts downloaded files to their specified destination folder. The script runs at startup with the use of Windows batch file and VBScript. Windows notification will be shown once script has started successfully.


# Installation
1. Create Virtual Environment in Python
   ```
   python -m venv venv
   ```
2. Install all dependencies from requirement.txt
   ```
   pip install -r requirements.txt
   ```
3. Create String Value in Registry Editor ([Video Reference](https://www.youtube.com/watch?v=XWV9tatoPQI&ab_channel=CodeBear))
   1. Go to Registry Editor
   2. Go to Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
   3. New &rarr; String Value &rarr; fill any name &rarr; fill value data (full path of VBS)

# Instructions
1. Add new destination folder paths in ***config.ini***
2. Add new supported file extensions in `extensions` dictionary in ***main.py***.
