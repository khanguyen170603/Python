from .data import seed_movies, get_movies, find_movie, book_seat

# Initialize sample data on import
seed_movies()

__all__ = ["get_movies", "find_movie", "book_seat"]
