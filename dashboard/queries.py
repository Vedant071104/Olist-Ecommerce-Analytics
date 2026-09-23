# ==========================
# Executive Dashboard KPIs
# ==========================

TOTAL_ORDERS = """
SELECT COUNT(*) AS total_orders
FROM orders;
"""

TOTAL_CUSTOMERS = """
SELECT COUNT(*) AS total_customers
FROM customers;
"""

TOTAL_PRODUCTS = """
SELECT COUNT(*) AS total_products
FROM products;
"""

TOTAL_SELLERS = """
SELECT COUNT(*) AS total_sellers
FROM sellers;
"""

TOTAL_REVENUE = """
SELECT ROUND(SUM(payment_value),2) AS total_revenue
FROM order_payments;
"""

AVERAGE_RATING = """
SELECT ROUND(AVG(review_score),2) AS average_rating
FROM order_reviews;
"""
# ==========================
# Filters
# ==========================

YEARS = """
SELECT DISTINCT YEAR(order_purchase_timestamp) AS year
FROM orders
ORDER BY year;
"""

STATES = """
SELECT DISTINCT customer_state
FROM customers
ORDER BY customer_state;
"""

CATEGORIES = """
SELECT DISTINCT product_category_name
FROM products
WHERE product_category_name IS NOT NULL
ORDER BY product_category_name;
"""
# ======================================================
# Monthly Revenue Trend
# ======================================================

MONTHLY_REVENUE = """
SELECT
    DATE_FORMAT(o.order_purchase_timestamp,'%Y-%m') AS month,
    ROUND(SUM(op.payment_value),2) AS revenue

FROM orders o

JOIN order_payments op
ON o.order_id = op.order_id

GROUP BY month

ORDER BY month;
"""
TOP_CATEGORIES = """
SELECT
    p.product_category_name,
    COUNT(oi.order_id) AS total_orders
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_orders DESC
LIMIT 10;
"""

AVERAGE_ORDER_VALUE = """
SELECT ROUND(
    SUM(payment_value) / COUNT(DISTINCT order_id),
    2
) AS avg_order_value
FROM order_payments;
"""

PAYMENT_METHOD = """
SELECT payment_type,
       COUNT(DISTINCT order_id) AS total
FROM order_payments
GROUP BY payment_type
ORDER BY total DESC;
"""

REVENUE_BY_STATE = """
SELECT
c.customer_state,
ROUND(SUM(op.payment_value),2) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN order_payments op
ON o.order_id = op.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;
"""

TOP_CATEGORY_SALES = """
SELECT
p.product_category_name,
ROUND(SUM(oi.price),2) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id=p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
"""

CUSTOMER_GROWTH = """
SELECT DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
       COUNT(DISTINCT c.customer_unique_id) AS customers
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY month
ORDER BY month;
"""
CUSTOMERS_BY_STATE = """
SELECT
customer_state,
COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
"""
TOP_CITIES = """
SELECT
customer_city,
COUNT(*) AS total_customers
FROM customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 10;
"""

NEW_RETURNING_CUSTOMERS = """
SELECT
CASE
    WHEN customer_orders = 1 THEN 'New Customer'
    ELSE 'Returning Customer'
END AS customer_type,
COUNT(*) AS total
FROM
(
    SELECT
        c.customer_unique_id,
        COUNT(o.order_id) AS customer_orders
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
) t
GROUP BY customer_type;
"""

AVERAGE_PRODUCT_PRICE = """
SELECT
ROUND(AVG(price),2) AS avg_price
FROM order_items;
"""

TOP_PRODUCT_CATEGORIES = """
SELECT
p.product_category_name,
ROUND(SUM(oi.price),2) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
"""

AVERAGE_PRICE_BY_CATEGORY = """
SELECT
    p.product_category_name,
    ROUND(AVG(oi.price),2) AS avg_price
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY avg_price DESC
LIMIT 10;
"""

PRICE_RANGE = """
SELECT
    CASE
        WHEN price < 50 THEN '0 - 50'
        WHEN price < 100 THEN '50 - 100'
        WHEN price < 250 THEN '100 - 250'
        WHEN price < 500 THEN '250 - 500'
        WHEN price < 1000 THEN '500 - 1000'
        ELSE '1000+'
    END AS price_range,
    COUNT(DISTINCT product_id) AS total_products
FROM order_items
GROUP BY price_range
ORDER BY
    CASE price_range
        WHEN '0 - 50' THEN 1
        WHEN '50 - 100' THEN 2
        WHEN '100 - 250' THEN 3
        WHEN '250 - 500' THEN 4
        WHEN '500 - 1000' THEN 5
        ELSE 6
    END;
"""

AVERAGE_DELIVERY_DAYS = """
SELECT
ROUND(
AVG(DATEDIFF(order_delivered_customer_date,
order_purchase_timestamp)),2
) AS avg_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;
"""

ORDER_STATUS = """
SELECT
order_status,
COUNT(*) AS total
FROM orders
GROUP BY order_status
ORDER BY total DESC;
"""

REVIEW_SCORE = """
SELECT
review_score,
COUNT(*) AS total
FROM order_reviews
GROUP BY review_score
ORDER BY review_score;
"""

MONTHLY_REVIEWS = """
SELECT
DATE_FORMAT(review_creation_date,'%Y-%m') AS month,
AVG(review_score) AS avg_rating
FROM order_reviews
GROUP BY month
ORDER BY month;
"""

DELIVERY_PERFORMANCE = """
SELECT
CASE
WHEN order_delivered_customer_date <= order_estimated_delivery_date
THEN 'On Time'
ELSE 'Late'
END AS delivery_status,
COUNT(*) AS total
FROM orders
WHERE order_delivered_customer_date IS NOT NULL
GROUP BY delivery_status;
"""