from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestUser, Response, RequestPrueba
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


@router.post("/create")
async def create_prueba_service(request: RequestPrueba, db: Session = Depends(get_db)):
    crud.create_prueba(db, prueba=request.parameter)
    response_data = {"status": "Ok", "code": "200", "message": "Prueba created successfully"}
    return JSONResponse(content=response_data, status_code=200)

@router.patch("/update/{prueba_id}")
async def update_prueba(prueba_id: int, request: RequestPrueba, db: Session = Depends(get_db)):
    _prueba = crud.update_prueba(db, prueba_id=prueba_id, prueba=request.parameter.prueba, nota=request.parameter.nota, qr=request.parameter.qr)
    return Response(status="Ok", code="200", message="Success update data", result=_prueba)

@router.get("/{prueba_id}")
async def get_prueba_by_id(prueba_id: int, db: Session = Depends(get_db)):
    _prueba = crud.get_prueba_by_id(db, prueba_id=prueba_id)
    if _prueba is None:
        raise HTTPException(status_code=404, detail="Prueba not found")
    return Response(status="Ok", code="200", message="Success fetch data", result=_prueba)

@router.delete("/prueba/delete/{prueba_id}")
async def delete_prueba(prueba_id: int, db: Session = Depends(get_db)):
    _prueba = crud.get_prueba_by_id(db, prueba_id=prueba_id)
    if _prueba is None:
        raise HTTPException(status_code=404, detail="Prueba not found")
    crud.remove_prueba(db, prueba_id=prueba_id)
    response_data = {"status": "Ok", "code": "200", "message": "Prueba deleted successfully"}
    return JSONResponse(content=response_data, status_code=200)