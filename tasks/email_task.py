from tasks.base_task import BaseTask
from utils.logger import setup_logger
from utils.emailer import send_mail
log = setup_logger()

class EmailTask(BaseTask):
    def run(self):
        details = self.config.get("details",{})
        to = details.get("to","")
        subject = details.get("subject","No Subject")
        body = details.get("body","")
        if not to:
            log.error(f"[To] address not provided, skip:{self.name}")
            return
        success = send_mail(to,subject,body)
        if not success:
            raise Exception("Failed to send email")
        
        
