import tkinter as tk
from tkinter import messagebox
from services.data import get_movies, book_seat

class MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("Movie Ticket Booking")
        root.geometry("900x600")

        self.movies = get_movies()

        # Left: list of movies
        left = tk.Frame(root, padx=10, pady=10)
        left.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(left, text="Movies", font=(None, 14, 'bold')).pack(anchor='w')
        self.lb = tk.Listbox(left, width=30)
        self.lb.pack(fill=tk.Y, expand=False)
        for m in self.movies:
            self.lb.insert(tk.END, f"{m.id}: {m.title} ({m.duration}m)")
        self.lb.bind("<<ListboxSelect>>", self.on_movie_select)

        # Right: details and booking
        right = tk.Frame(root, padx=10, pady=10)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.details = tk.Label(right, text="Select a movie", justify=tk.LEFT)
        self.details.pack(anchor='nw')

        self.screenings_box = tk.Listbox(right, height=4)
        self.screenings_box.pack(fill=tk.X)
        self.screenings_box.bind("<<ListboxSelect>>", self.on_screening_select)

        self.seats_box = tk.Listbox(right)
        self.seats_box.pack(fill=tk.BOTH, expand=True)

        self.book_button = tk.Button(right, text="Book Selected Seat", command=self.book_selected)
        self.book_button.pack(pady=8)

        self.selected_movie = None
        self.selected_screening = None

    def on_movie_select(self, event):
        sel = self.lb.curselection()
        if not sel:
            return
        idx = sel[0]
        self.selected_movie = self.movies[idx]
        self.details.config(text=f"{self.selected_movie.title} — {self.selected_movie.duration} minutes")

        self.screenings_box.delete(0, tk.END)
        for s in self.selected_movie.screenings:
            self.screenings_box.insert(tk.END, f"{s.id}: {s.time}")
        self.seats_box.delete(0, tk.END)

    def on_screening_select(self, event):
        sel = self.screenings_box.curselection()
        if not sel or not self.selected_movie:
            return
        idx = sel[0]
        self.selected_screening = self.selected_movie.screenings[idx]
        self._refresh_seats()

    def _refresh_seats(self):
        self.seats_box.delete(0, tk.END)
        for seat in self.selected_screening.seats:
            label = f"Seat {seat.id} (R{seat.row}#{seat.number}) - {'OK' if seat.available else 'X'}"
            self.seats_box.insert(tk.END, label)

    def book_selected(self):
        sel = self.seats_box.curselection()
        if not sel or not self.selected_movie or not self.selected_screening:
            messagebox.showwarning("No selection", "Please select a movie, screening and seat first.")
            return
        idx = sel[0]
        seat = self.selected_screening.seats[idx]
        try:
            # For scaffold, use a placeholder user name
            booking = book_seat(self.selected_movie.id, self.selected_screening.id, seat.id, user_name="Guest")
            messagebox.showinfo("Booked", f"Booked seat {seat.id} for {self.selected_movie.title}.")
            self._refresh_seats()
        except Exception as e:
            messagebox.showerror("Error", str(e))
