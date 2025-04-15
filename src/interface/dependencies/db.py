from infrastructure.database.config import get_db
from fastapi import Depends

def get_db_session():
    return Depends(get_db)