from pathlib import Path
import pandas as pd
import sqlite3

# Uzyskujemy ścieżkę do folderu, w którym znajduje się skrypt
script_dir = Path(__file__).resolve().parent

# Łączymy ścieżkę z folderem, w którym znajduje się baza danych
db_path = script_dir / "../data/game_analytics.db"

# Połączenie z bazą danych
conn = sqlite3.connect(db_path)

# Wczytaj CSV jako DataFrame
activity_df = pd.read_csv(script_dir / "../data/final_data_daily_activity.csv")
purchase_df = pd.read_csv(script_dir / "../data/final_data_in_app_purchases.csv")

# Zapisz do tabel
activity_df.to_sql("daily_activity", conn, if_exists="replace", index=False)
purchase_df.to_sql("in_app_purchases", conn, if_exists="replace", index=False)

print("✅ Data has been added to database game_analytics.db")