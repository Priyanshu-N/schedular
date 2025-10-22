from fastapi import FastAPI
from pydantic import BaseModel
import threading
import time
import psutil

app = FastAPI()
timers = {}  # process_name -> remaining_seconds

# Pydantic model for POST request
class ProcessTimer(BaseModel):
    name: str
    seconds: int

# Background loop to monitor processes
def monitor_loop():
    while True:
        for name, remaining in list(timers.items()):  # use list to avoid RuntimeError
            procs = [p for p in psutil.process_iter(["name"]) if name.lower() in (p.info["name"] or "").lower()]
            if procs and remaining > 0:
                timers[name] -= 1
                if timers[name] <= 0:
                    for p in procs:
                        try:
                            p.terminate()
                        except Exception as e:
                            print(f"Failed to terminate {p.info['name']}: {e}")
                    timers.pop(name)  # remove timer after termination
        time.sleep(1)

threading.Thread(target=monitor_loop, daemon=True).start()

# GET all timers
@app.get("/processes")
def get_processes():
    return timers

# POST a new process timer using JSON
@app.post("/processes")
def add_process(timer: ProcessTimer):
    timers[timer.name] = timer.seconds
    return {"status": "added", "name": timer.name, "time": timer.seconds}
