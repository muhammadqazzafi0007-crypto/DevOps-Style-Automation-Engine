import os
import shutil
from tasks.base_task import BaseTask
from utils.logger import setup_logger

log = setup_logger()
class FileTask(BaseTask):
    
    def run(self):
        details = self.config.get("details",{})
        watch_folder = details.get("watch_folder","")
        destination = details.get("detination","")
        
        if not os.path.isdir(watch_folder):
            log.warning(f"[File] folder not found: {watch_folder}")
            return
        
        os.makedirs(destination,exist_ok=True)
        files = os.listdir(watch_folder)
        
        if not files:
            log.info(f"[file] Folder's empty, Nothing to do.")
            return
        
        for filename in files:
            src = os.path.join(watch_folder,filename)
            if os.path.isfile(src):
                dst = os.path.join(destination,filename)
                shutil.move(src,dst)
                log.info(f"[File] File Moved {filename} -> {destination}")