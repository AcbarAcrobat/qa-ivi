from pydantic import BaseModel
from typing import List, Optional, Union


class Character(BaseModel):
    education: Optional[str]
    height: Optional[Union[int, float, str]]
    identity: Optional[str]
    name: Optional[str]
    other_aliases: Optional[str]
    universe: Optional[str]
    weight: Optional[Union[int, float, str]]


class Characters(BaseModel):
    result: List[Character]
