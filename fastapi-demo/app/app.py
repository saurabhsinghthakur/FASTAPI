# Custom Modules
from app.core.libraries.core import Core
from app.core.libraries.response import Response
from app.core import models
from app.core import schemas
from app.databases import Base, engine, get_db

from typing import Union
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi import Depends

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(Response(response=[], errors=exc.errors(), status_code=422).error()),
    )

@app.get("/api/{version}/{product}/")
def get(version: str, product: str, db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    try:
        module_name = Core().load_module('app.services.'+version+'.'+product+'.'+product, product)
        response = module_name.get(db=db, limit=limit, page=page, search=search)
        return Response(response=response, status_code=200).success()
    except Exception as e:
        return Response(response=[], errors={"message": e}, status_code=500).error()

@app.get("/api/{version}/{product}/{id}/")
def get(version: str, product: str):
    return {"version": version, "product": product, "singleget": "singleget"}

@app.post("/api/{version}/{product}/")
def post(version: str, product: str, payload: schemas.ToDo, db: Session = Depends(get_db)):
    try:
        module_name = Core().load_module('app.services.'+version+'.'+product+'.'+product, product)
        response = module_name.post(payload=payload, db=db)
        return Response(response=response, status_code=200).success()
    except Exception as e:
        return Response(response=[], errors={"message": e}, status_code=500).error()

@app.put("/api/{version}/{product}/{id}/")
def put(version: str, product: str):
    return {"version": version, "product": product, "put": "put"}

@app.delete("/api/{version}/{product}/{id}/")
def delete(version: str, product: str):
    return {"version": version, "product": product, "delete": "delete"}
