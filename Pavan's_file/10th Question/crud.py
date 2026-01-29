from sqlalchemy.orm import Session
from models import Employee

def create_employee(db: Session, employee):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_all_employees(db: Session, skip: int, limit: int, search: str | None):
    query = db.query(Employee)
    if search:
        query = query.filter(Employee.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def update_employee(db: Session, emp_id: int, employee):
    emp = get_employee(db, emp_id)
    if not emp:
        return None
    for key, value in employee.dict().items():
        setattr(emp, key, value)
    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session, emp_id: int):
    emp = get_employee(db, emp_id)
    if not emp:
        return None
    db.delete(emp)
    db.commit()
    return emp
