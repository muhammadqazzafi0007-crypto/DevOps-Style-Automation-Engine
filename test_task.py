from config.config_loader import load_config
from tasks.task_factory import create_task

# config se tasks padho
configs = load_config()

# har config ko task object mein badlo aur chalao
for cfg in configs:
    task = create_task(cfg)
    if task:
        task.execute()