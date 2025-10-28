from typing import List
from models import Movie, Screening, Seat

_MOVIES: List[Movie] = []

def seed_movies():
    """Seed a few movies with screenings and seats into in-memory store."""
    global _MOVIES
    if _MOVIES:
        return

    def make_seats(rows=5, per_row=8):
        seats = []
        sid = 1
        for r in range(1, rows+1):
            for n in range(1, per_row+1):
                seats.append(Seat(id=sid, row=r, number=n, available=True))
                sid += 1
        return seats

    m1 = Movie(id=1, title="Space Adventure", duration=120, screenings=[
        Screening(id=1, time="14:00", seats=make_seats()),
        Screening(id=2, time="18:30", seats=make_seats()),
    ])

    m2 = Movie(id=2, title="Romantic Comedy", duration=95, screenings=[
        Screening(id=3, time="15:30", seats=make_seats()),
        Screening(id=4, time="20:00", seats=make_seats()),
    ])

    _MOVIES = [m1, m2]

def get_movies():
    return _MOVIES

def find_movie(movie_id: int):
    for m in _MOVIES:
        if m.id == movie_id:
            return m
    return None

def book_seat(movie_id: int, screening_id: int, seat_id: int, user_name: str):
    movie = find_movie(movie_id)
    if not movie:
        raise ValueError("Movie not found")
    screening = next((s for s in movie.screenings if s.id == screening_id), None)
    if not screening:
        raise ValueError("Screening not found")
    seat = next((s for s in screening.seats if s.id == seat_id), None)
    if not seat:
        raise ValueError("Seat not found")
    if not seat.available:
        raise ValueError("Seat already booked")
    seat.available = False
    return {"movie_id": movie_id, "screening_id": screening_id, "seat_id": seat_id, "user_name": user_name}
