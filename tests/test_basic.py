import unittest
from services.data import seed_movies, get_movies, book_seat

class BasicTests(unittest.TestCase):
    def setUp(self):
        seed_movies()

    def test_get_movies(self):
        movies = get_movies()
        self.assertTrue(len(movies) >= 1)

    def test_booking_flow(self):
        movies = get_movies()
        m = movies[0]
        s = m.screenings[0]
        seat = s.seats[0]
        # book seat
        res = book_seat(m.id, s.id, seat.id, 'Tester')
        self.assertEqual(res['movie_id'], m.id)
        self.assertFalse(seat.available)

if __name__ == '__main__':
    unittest.main()
