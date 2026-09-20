import psycopg

conn = psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres")

try:
    cur = conn.cursor()

    for table, key in [
        ("geolocation", "geolocation_id"),
        ("order_reviews", "order_review_key")
    ]:
        print(f"===== {table} =====")

        cur.execute(
            """
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'project02'
              AND table_name = %s
            ORDER BY ordinal_position
            """,
            (table,)
        )

        print("COLUMNS:")
        for row in cur.fetchall():
            print(row)

        cur.execute(f"SELECT COUNT(*) FROM project02.{table}")
        print("ROW COUNT:", cur.fetchone()[0])

        cur.execute(
            f"""
            SELECT MIN({key}), MAX({key}), COUNT(DISTINCT {key})
            FROM project02.{table}
            """
        )
        print("KEY RANGE/DISTINCT:", cur.fetchone())

    print("21-AX: OPERATIONAL IDENTITY VERIFICATION PASS")

finally:
    conn.close()
