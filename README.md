# Movie Ticket Booking (Tkinter)

Simple scaffold for a Tkinter-based movie ticket booking app.

How to run

1. Create a virtual environment (optional):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install optional dependencies (Pillow for images):

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

Project layout

- `app.py` - entrypoint that launches the Tkinter UI
- `models/` - dataclasses for Movie, Screening, Seat, Booking
- `services/` - in-memory data and booking logic
- `ui/` - Tkinter UI components
- `tests/` - basic unit tests
