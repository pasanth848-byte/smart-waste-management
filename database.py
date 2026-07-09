import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS predictions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

image_name TEXT,

waste_type TEXT,

confidence REAL,

date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")

conn.commit()


def save_prediction(image_name,waste_type,confidence):

    cursor.execute(

        "INSERT INTO predictions(image_name,waste_type,confidence) VALUES(?,?,?)",

        (image_name,waste_type,confidence)

    )

    conn.commit()


def get_all_predictions():

    cursor.execute(

        "SELECT * FROM predictions ORDER BY id DESC"

    )

    return cursor.fetchall()