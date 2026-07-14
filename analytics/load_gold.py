import duckdb

# Connect to DuckDB
con = duckdb.connect("analytics/orders.db")

tables = {
    "daily_revenue": "data/gold/daily_revenue/*.parquet",
    "category_sales": "data/gold/category_sales/*.parquet",
    "city_sales": "data/gold/city_sales/*.parquet",
    "top_products": "data/gold/top_products/*.parquet",
    "top_customers": "data/gold/top_customers/*.parquet",
}

for table_name, parquet_path in tables.items():
    print(f"Loading {table_name}...")

    con.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_parquet('{parquet_path}')
    """)

print("\n✅ Gold layer loaded successfully!")

# Show all tables
print("\nTables in DuckDB:")
print(con.execute("SHOW TABLES").fetchall())

con.close()