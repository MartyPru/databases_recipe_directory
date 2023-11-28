from dataclasses import dataclass

@dataclass
class Recipe:
    id: int
    name: str
    cooking_time_in_mins: int
    rating: int