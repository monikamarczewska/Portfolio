from pathlib import Path
import sqlite3

# Uzyskujemy ścieżkę do folderu, w którym znajduje się skrypt
script_dir = Path(__file__).resolve().parent

# Łączymy ścieżkę z folderem, w którym znajduje się baza danych
db_path = script_dir / "../data/game_analytics.db"

# Połączenie z bazą danych
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Pobierz listę tabel
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📋 Tabele w bazie danych:")
for table in tables:
    print("-", table[0])

conn.close()