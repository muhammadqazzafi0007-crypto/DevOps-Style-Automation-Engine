from tasks.email_task import EmailTask
from tasks.file_task import FileTask
from utils.logger import setup_logger

log = setup_logger()

TASK_TYPES = {
    "email":EmailTask,
    "file":FileTask
}

def create_task(config):
    task_type = config.get("type")
    if task_type not in TASK_TYPES:
        log.warning(f"Unknown Task Type: {task_type} (Skip)")
        return None
    
    task_class = TASK_TYPES[task_type]
    return task_class(config)

    