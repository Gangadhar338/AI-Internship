import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="Postgres@1234"
)

print("Connected to PostgreSQL successfully!")

conn.close()
