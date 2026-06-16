from utils.logger import setup_logger

log = setup_logger()

def schedule_parser(sch_str):
    if not sch_str:
        log.warning("Empty Schedule Skip")
        return None
    s = sch_str.lower().strip()
    if s.startswith("every"):
        parts = s.split()
        
        try:
            number = int(parts[1])
            unit = parts[2]
        except (IndexError,ValueError):
            log.error(f"wrong interval format {sch_str}")
            return None
        if "seconds" in unit:
            seconds = number
        elif "minutes" in unit:
            seconds = number * 60
        elif "hour" in unit:
            seconds = number * 3600
        else:
            log.error(f"unknown time unit {unit}")
            return None
        return {"type":"interval","seconds":seconds}
    
    if s.startswith("daily at"):
        parts = s.split()
        
        try:
            time_str = parts[2]
            hours,minute = time_str.split(":")
            int(hours)
            int(minute)
        except (IndexError,ValueError):
            log.error(f"wrong daily format {time_str}")
            return None
        return {"type":"daily","time":time_str}
    
    log.error(f"invalid schedule {sch_str}")
    return None