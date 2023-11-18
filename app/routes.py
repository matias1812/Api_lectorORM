from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestUser, Response
from fastapi.responses import JSONResponse

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/create")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    response_data = {"status": "Ok", "code": "200", "message": "User created successfully"}
    return JSONResponse(content=response_data, status_code=200)

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router.patch("/update")
async def update_user(request: RequestUser, db: Session = Depends(get_db)):
    _users = crud.update_user(db, user_id=request.parameter.user_id,
                             userName=request.parameter.userName,  # Ajusta el nombre del argumento
                             password=request.parameter.password)  # Ajusta el nombre del argumento
    return Response(status="Ok", code="200", message="Success update data", result=_users)


@router.delete("/delete")
async def delete_user(request: RequestUser,  db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=request.parameter.user_id)
    response_data = {"status": "Ok", "code": "200", "message": "User created successfully"}
    return JSONResponse(content=response_data, status_code=200)
