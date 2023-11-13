# En tu archivo de rutas (por ejemplo, users.py o similar)

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db, get_current_user, get_password_hash
from ..models import User
from ..schemas import UserInDB, UserBase, UserCreate

router = APIRouter()

# Show my profile data
@router.get("/users/me", response_model=UserInDB)
def read_user_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Fetch the current user's profile information.
    """
    return current_user

# List users or members
@router.get("/users/", response_model=List[UserInDB])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of users.
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# List user profile based on his userid
@router.get("/user/{user_id}", response_model=UserInDB)
def get_user(user_id: int, db: Session = Depends(get_db)):
    print("*"*10)
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/create", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Verifica que las contraseñas coincidan
    if user.password != user.password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password,
                   first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user