from tasks.base_task import BaseTask
from utils.logger import setup_logger

log = setup_logger()

class EmailTask(BaseTask):
    def run(self):
        details = self.config.get("details",{})
        to = details.get("to","unknown")
        subject = details.get("subject","no subject")
        log.info(f"[Email] sending -> To {to} | Subject {subject}")
        
