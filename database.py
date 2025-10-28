import sqlite3

def init_db():
    conn = sqlite3.connect("movie_booking.db")
    cur = conn.cursor()

    # Tạo bảng
    cur.execute("""
        CREATE TABLE IF NOT EXISTS User(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Movie(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            duration INTEGER,
            genre TEXT,
            image_path TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Room(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            seat_count INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Showtime(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            room_id INTEGER,
            start_time TEXT,
            end_time TEXT,
            FOREIGN KEY(movie_id) REFERENCES Movie(id),
            FOREIGN KEY(room_id) REFERENCES Room(id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Seat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            seat_number TEXT,
            is_booked INTEGER,
            FOREIGN KEY(room_id) REFERENCES Room(id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Ticket(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            showtime_id INTEGER,
            seat_id INTEGER,
            price REAL,
            booking_time TEXT,
            FOREIGN KEY(user_id) REFERENCES User(id),
            FOREIGN KEY(showtime_id) REFERENCES Showtime(id),
            FOREIGN KEY(seat_id) REFERENCES Seat(id)
        )
    """)

    conn.commit()
    conn.close()

# Gọi khởi tạo
if __name__ == "__main__":
    init_db()
    print("✅ Database đã được khởi tạo thành công!")
