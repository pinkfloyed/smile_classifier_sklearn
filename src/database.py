import time
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os

db_config = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "database": os.getenv("DATABASE_NAME", "smiledatabase"),
    "user": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", ""),
}

def init_db():
    retries = 5
    for attempt in range(retries):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    image TEXT NOT NULL,
                    classification VARCHAR(50) NOT NULL,
                    date_time DATETIME NOT NULL
                )
            """)
            conn.commit()
            print("Database initialized successfully!")
            conn.close()
            break
        except Error as e:
            print(f"Database connection attempt {attempt + 1}/{retries} failed: {e}")
            time.sleep(5)
    else:
        raise Exception("Could not connect to the database after multiple attempts.")

def insert_history(image, classification, date_time=None):
    date_time = date_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO history (image, classification, date_time)
        VALUES (%s, %s, %s)
    """, (image, classification, date_time))
    conn.commit()
    print("Record inserted successfully!")
    conn.close()

def get_history():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT image, classification, date_time FROM history")
    records = cursor.fetchall()
    conn.close()
    return [
        {"image": row[0], "classification": row[1], "date_time": row[2].strftime("%Y-%m-%d %H:%M:%S")}
        for row in records
    ]


if __name__ == "__main__":
    init_db()
