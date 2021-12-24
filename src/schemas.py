from typing import List, Optional

from pydantic import BaseModel


class PlayerCreate(BaseModel):
    username: str
    oculus_id: str


class DartCreate(BaseModel):
    dart_name: str
    price: int

class Player(BaseModel):
    id: int
    username: str
    oculus_id: str
    highscore: str
    fastest_time: str
    coin: int

class Dart(BaseModel):
    id: int
    dart_name: str
    price: int
    is_owned: bool
    player_id: int
