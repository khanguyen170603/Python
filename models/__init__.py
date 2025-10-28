from dataclasses import dataclass, field
from typing import List

@dataclass
class Seat:
    id: int
    row: int
    number: int
    available: bool = True

@dataclass
class Screening:
    id: int
    time: str
    seats: List[Seat] = field(default_factory=list)

@dataclass
class Movie:
    id: int
    title: str
    duration: int  # minutes
    screenings: List[Screening] = field(default_factory=list)

@dataclass
class Booking:
    movie_id: int
    screening_id: int
    seat_id: int
    user_name: str
