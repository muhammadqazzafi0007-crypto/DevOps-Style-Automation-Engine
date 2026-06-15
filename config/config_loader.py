
import yaml
from utils.logger import setup_logger

log = setup_logger()

def load_config(path="config/sample_config.yaml"):
    try:
        with open(path, "r") as file:
            data = yaml.safe_load(file)
        if not data or "tasks" not in data:
            log.error(f"No Task found in config: {path}")
            return[]
        
        tasks = data["tasks"]
        
        valid_tasks = validate_tasks(tasks)
        
        log.info(f"config loaded: {len(valid_tasks)} valid tasks founded")
        return valid_tasks
    
    except FileNotFoundError:
        log.error(f"config file not found: {path}")
        return []
    except yaml.YAMLError as e:
        log.error(f"YAML load failure: {e}")
        return []
    
def validate_tasks(tasks):
    required_fields = ["name","type","schedule"]
    valid = []
    
    for task in tasks:
        missing = [field for field in required_fields if field not in task]
        if missing:
            log.warning(f"Task Skipped (missing {missing}): {task}")
            continue
        if task.get("enabled",True) is False:
            log.info(f"Task's disabled, skip: {task['name']}")
            continue
        valid.append(task)
        
    return valid