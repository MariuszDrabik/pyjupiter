from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Union


router = APIRouter(
    prefix='/ships'
)


class Ship(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


ships = [
    {
        'name': 'Sokół',
        'description': 'Fajny statek',
        'price': 22,
        'tax': 12,
    },
    {
        'name': 'AAA',
        'description': 'Fajny statek',
        'price': 22,
        'tax': 12,
    },
]


def has_ship(ship: int):
    try:
        ships[ship-1]
    except IndexError:
        raise HTTPException(status_code=404, detail='Nie mamy takiego statku')


@router.get('/')
async def root(page: int = 0) -> Dict[str, str]:
    if page != 0:
        return {'Ship page': f'Ship page {page}'}
    return ships


@router.get('/{id}')
async def root(id: int,) -> Dict[str, str]:
    has_ship(id)
    return ships[id-1]


@router.post('/', status_code=201)
async def root(ship: Ship) -> Dict[str, str]:
    return {'ship': f'Ship {ship} added'}


@router.delete('/{id}')
async def root(id: int,) -> Dict[str, str]:
    has_ship(id)
    del ships[id-1]
    return ships


@router.put('/{id}')
async def root(id: int,) -> Dict[str, str]:
    has_ship(id)
    return {'ship': f'Update data ship {id}'}
