from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Union


router = APIRouter()


@router.get('/')
async def root() -> Dict[str, str]:
    return {'message': 'Hello from FastAPI'}
