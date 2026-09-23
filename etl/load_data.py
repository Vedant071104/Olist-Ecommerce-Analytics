import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vedant@123",
    database="olist"
)

cursor = conn.cursor()

if conn.is_connected():
    print("Connected to MySQL successfully!")


# Read CSV

orders = pd.read_csv("data/olist_orders_dataset.csv")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

orders = orders.where(pd.notnull(orders), None)

print(f"Total Records in CSV: {len(orders)}")

cursor.execute("DROP TABLE IF EXISTS orders")
conn.commit()

create_table_query = """
CREATE TABLE orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(50),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME
)
"""

cursor.execute(create_table_query)
conn.commit()
print("order table created succesfully!")

insert_query = """
INSERT INTO orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

data = list(orders.itertuples(name=None,index=False))

print(f"Prepared {len(data)} rows for insertion.")

#print(data[:3])

try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print("All records inserted successfully!")

except Exception as e:
    print("Error:", e)


cursor.execute("SELECT COUNT(*) FROM orders")

count = cursor.fetchone()

print("Total rows in orders table:", count[0])

cursor.close()
conn.close()
print("Connection Closed")
