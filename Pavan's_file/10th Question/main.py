from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee CRUD API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/employees", response_model=schemas.EmployeeResponse)
def create(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

# READ ALL (Pagination + Search)
@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def read_all(skip: int = 0, limit: int = 10, search: str | None = None,
             db: Session = Depends(get_db)):
    return crud.get_all_employees(db, skip, limit, search)

# READ BY ID
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def read_one(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# UPDATE
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def update(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    emp = crud.update_employee(db, emp_id, employee)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# DELETE
@app.delete("/employees/{emp_id}")
def delete(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
