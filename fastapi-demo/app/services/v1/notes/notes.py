from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()

# [...] create record
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    new_note = models.Note(**payload.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {"status": "success", "note": new_note}

