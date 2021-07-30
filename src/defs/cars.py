from typing import Union

from pydantic import BaseModel


class CarWithAvgRatingDef(BaseModel):
    id: int
    make: str
    model: str
    avg_rating: Union[float, int]


class CarWithRatingsCountDef(BaseModel):
    id: int
    make: str
    model: str
    rates_number: int


class CarDef(BaseModel):
    model: str
    make: str
