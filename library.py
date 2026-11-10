import os
import psycopg2
import dotenv

dotenv.load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
)

cur = conn.cursor()

print("--- All Books in Library ---")
cur.execute("SELECT book_id, title, available_copies FROM books;")
for row in cur.fetchall():
    print(row)

print("\n--- Borrowed Books ---")
cur.execute("SELECT * FROM borrowings;")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
print("\nDone! Database is connected to python.")
