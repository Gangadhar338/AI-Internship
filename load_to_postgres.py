import pandas as pd
import psycopg

# Read cleaned Excel file
df = pd.read_excel("use_case_2/cleaned_data.xlsx")

# Connect to PostgreSQL
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="ai_internship",
    user="postgres",
    password="Postgres@1234"
)

with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee_data (
            name VARCHAR(100),
            age INTEGER,
            email VARCHAR(150),
            salary INTEGER
        )
    """)

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO employee_data (name, age, email, salary)
            VALUES (%s, %s, %s, %s)
            """,
            (
                row["Name"],
                int(row["Age"]),
                row["Email"],
                int(row["Salary"])
            )
        )

conn.commit()
conn.close()

print("Cleaned Excel data loaded into PostgreSQL successfully!")
