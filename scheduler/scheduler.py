import time
from datetime import datetime
import threading

from scheduler.schedule_parser import schedule_parser
from tasks.task_factory import create_task
from utils.logger import setup_logger

log = setup_logger()

class Scheduler:
    def __init__(self, task_configs):
        
        self.task_configs = task_configs
        self.running = False
        self.thread = None
        self.scheduled = []
        
        self._prepare_tasks()
    
    def _prepare_tasks(self):
        for cfg in self.task_configs:
            schedule = schedule_parser(cfg.get("schedule"))
            task = create_task(cfg)
            
            if schedule and task:
                self.scheduled.append({
                    "task":task,
                    "schedule":schedule,
                    "last_run":0,
                    "last_daily":None
                })
                log.info(f"scheduled: {task.name} ({cfg.get('schedule')})")

    def _should_run(self,item):
        schedule = item["schedule"]
        now = time.time()
        
        if schedule["type"] == "interval":
            gap = now - item["last_run"]
            if gap >= schedule["seconds"]:
                return True
            return False
        if schedule["type"] == "daily":
            current_time = datetime.now().strftime("%H:%M")
            today = datetime.now().strftime("%Y-%m-%d")
            
            if current_time == schedule["time"] and item["last_daily"] != today:
                return True
            return False
        
    def _loop(self):
        log.info("scheduled loop started")
        
        while self.running:
            for item in self.scheduled:
                if self._should_run(item):
                    item["task"].execute()
                    item["last_run"] = time.time()
                    item["last_daily"] = datetime.now().strftime("%Y-%m-%d")
            time.sleep(5)
        log.info("Scheduler loop stopped")
    def _start(self):
        if self.running:
            log.warning("already Schedule's in process")
            return
        self.running = True
        self.thread = threading.Thread(target=self._loop,daemon=True)
        self.thread.start()
        log.info("Scheduler's started")
    def _stop(self):
        self.running = False
        log.info("Scheduler's stopped")