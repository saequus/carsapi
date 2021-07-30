from pydantic import BaseModel


class RateDef(BaseModel):
    rating: int
    car_id: int
