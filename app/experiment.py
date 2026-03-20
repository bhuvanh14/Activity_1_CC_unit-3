import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="password123"
)

cur = conn.cursor()

today = datetime.now()

# Insert 1000 records
for i in range(1000):
    cur.execute(
        "INSERT INTO sensor_readings VALUES (%s, %s, %s)",
        (i, 25.5, today)
    )

conn.commit()

# Check which partition is used
cur.execute(
    "EXPLAIN SELECT * FROM sensor_readings WHERE recorded_at = %s",
    (today,)
)

print("Query Plan:", cur.fetchone()[0])

conn.close()