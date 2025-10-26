from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for validating input
class TaskSchema(BaseModel):
    task_name: str
    task_type: str
    process_name: str = None
    file_path: str = None
    start_time: datetime
    end_time: datetime
    interval_seconds: int = 0

@app.post("/tasks")
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    db_task = models.Task(
        task_name=task.task_name,
        task_type=task.task_type,
        process_name=task.process_name,
        file_path=task.file_path,
        start_time=task.start_time,
        end_time=task.end_time,
        interval_seconds=task.interval_seconds
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"message": "Task saved successfully", "task": {
        "id": db_task.id,
        "task_name": db_task.task_name,
        "status": db_task.status
    }}
