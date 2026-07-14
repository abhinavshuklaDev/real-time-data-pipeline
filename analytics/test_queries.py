import duckdb

con = duckdb.connect("analytics/orders.db")

tables = [
    "daily_revenue",
    "category_sales",
    "city_sales",
    "top_products",
    "top_customers"
]

for table in tables:
    print("\n" + "=" * 60)
    print(f"TABLE: {table}")
    print("=" * 60)

    print(con.execute(f"SELECT * FROM {table} LIMIT 5").fetchdf())

con.close()