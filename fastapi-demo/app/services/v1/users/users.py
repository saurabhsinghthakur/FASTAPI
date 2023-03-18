from app.core import models
from app.core import schemas
from app.databases import Base, engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends


class Users():
    def __init__(self) -> None:
        print("Response: ")
    
    def post(self, payload, db):
        new_note = models.ToDo(**payload.dict())
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return new_note
    
    def get(self, db, page, limit, search):
        skip = (page - 1) * limit
        notes = db.query(models.ToDo).filter(
            models.ToDo.task.contains(search)).limit(limit).offset(skip).all()        
        return {"data": notes, "count": len(notes)}
