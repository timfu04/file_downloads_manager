from distutils import extension
import os
import sys
import time
from configparser import ConfigParser
from turtle import down
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx



file = 'config.ini'
config = ConfigParser()
config.read(file)


# print(config['dest_path']['images'])


# Get "Downloads" folder path with Windows Registry UUIDs
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    source_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0] 

def is_file(file_dir):
    file_path = fr"{source_path}\{file_dir}"
    return os.path.isfile(file_path)
    
extensions = {"image":[".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                       ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", 
                       ".svgz", ".ai", ".eps", ".ico"],
              "document":[".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
              "compressed":[".7z", ".rar", ".zip"]}


all_files_dirs = os.listdir(source_path)
files = list(filter(is_file, all_files_dirs))


print(files)


for file in files:
    file_ext = f'.{file.rsplit(".",1)[-1].lower()}'
    
    for category, extension in extensions.items():
        if file_ext in extension:
            print(category)
            
        
    
    

    

    

    






class MonitorFolder(FileSystemEventHandler):
    
    def on_created(self, event):
         print(event.src_path, event.event_type)
   
    def on_modified(self, event):
        pass
        
        
        
        
        
        
            
            
        
        
        print(event.src_path, event.event_type)
    
    def on_deleted(self, event):
        print(event.src_path, event.event_type)
               


        


# if __name__ == "__main__":
#     event_handler = MonitorFolder()
#     observer = Observer()
#     observer.schedule(event_handler, source_path, recursive=True)
#     observer.start()
#     try:
#         while observer.is_alive():
#             observer.join(1)
#     finally:
#         observer.stop()
#         observer.join()       
        