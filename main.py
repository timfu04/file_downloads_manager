# Import modules
import os
import time
import shutil
from configparser import ConfigParser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx

# Setup configuration file parser
file = 'config.ini'
config = ConfigParser()
config.read(file)

# Get "Downloads" folder path with Windows Registry UUIDs
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    source_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0] 


def is_file(file_dir:str)->bool:
    """ Check whether string is file or directory

    Args:
        file_dir (str): file or directory names

    Returns:
        bool: returns True if string is file, returns False if string is not file
    """
    
    file_path = fr"{source_path}\{file_dir}"
    return os.path.isfile(file_path)

extensions = {"images":[".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", 
                       ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", 
                       ".svgz", ".ai", ".eps", ".ico"],
              "videos":[".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"],
              "documents":[".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
              "compressed":[".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".gz", ".z", ".zip"],
              "torrents":[".torrent"]}

# Subclass of FileSystemEventHandler
class MonitorFolder(FileSystemEventHandler):
    def on_modified(self, event):
        all_files_dirs = os.listdir(source_path)
        files = list(filter(is_file, all_files_dirs))
        
        for file in files:
            file_ext_no_dot = file.rsplit(".",1)[-1]
            file_ext_start_index = file.index(file_ext_no_dot)-1
            file_ext_with_dot = file[file_ext_start_index:].lower()
            
            for category, extension in extensions.items():
                if file_ext_with_dot in extension:
                    src_file_path = os.path.join(source_path, file)
                    dest_folder_path = config["dest_path"][category]
                    dest_file_path = os.path.join(dest_folder_path, file)
            
                    if os.path.exists(dest_file_path):
                        os.remove(dest_file_path)
                        shutil.move(src_file_path, dest_folder_path)
                    else:
                        shutil.move(src_file_path, dest_folder_path)
        
if __name__ == "__main__":
    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, source_path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()       


        