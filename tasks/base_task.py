from utils.logger import setup_logger

log = setup_logger()

class BaseTask:
    def __init__(self,config):
        self.config = config
        self.name = config.get("name","unnamed_task")
    
    def run(self):
        raise NotImplementedError
    def execute(self):
        log.info(f"Task Started {self.name}")
        try:
            self.run()
            log.info(f"Task Completed: {self.name}")
            return True
        except Exception as e:
            log.error(f"Task Failed: {self.name} | Error: {e}")
            return False
            