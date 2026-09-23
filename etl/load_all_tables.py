from database.connection import get_connection
from load_table import load_table

conn = get_connection()

cursor = conn.cursor()

print("Connected Successfully!")

create_order_items_query = """
CREATE TABLE order_items(
    order_id VARCHAR(50),
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),

    PRIMARY KEY(order_id, order_item_id),

    CONSTRAINT fk_order_items_orders
        FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_order_items_products
        FOREIGN KEY(product_id)
        REFERENCES products(product_id),

    CONSTRAINT fk_order_items_sellers
        FOREIGN KEY(seller_id)
        REFERENCES sellers(seller_id)
)
"""
insert_order_items_query = """
INSERT INTO order_items(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
)
VALUES(%s,%s,%s,%s,%s,%s,%s)
"""

load_table(
    conn=conn,
    cursor=cursor,
    csv_path="data/olist_order_items_dataset.csv",
    table_name="order_items",
    create_query=create_order_items_query,
    insert_query=insert_order_items_query,
    date_columns=[
        "shipping_limit_date"
    ]
)

cursor.close()
conn.close()

print("Connection Closed")