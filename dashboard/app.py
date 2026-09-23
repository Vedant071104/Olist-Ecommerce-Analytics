import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database.connection import get_connection
from queries import (
    TOTAL_ORDERS,
    TOTAL_CUSTOMERS,
    TOTAL_PRODUCTS,
    TOTAL_SELLERS,
    TOTAL_REVENUE,
    AVERAGE_RATING,
    YEARS,
    STATES,
    CATEGORIES,
    MONTHLY_REVENUE,
    TOP_CATEGORIES,
    AVERAGE_ORDER_VALUE,
    PAYMENT_METHOD,
    REVENUE_BY_STATE,
    TOP_CATEGORY_SALES,
    CUSTOMER_GROWTH,
    CUSTOMERS_BY_STATE,
    TOP_CITIES,
    NEW_RETURNING_CUSTOMERS,
    AVERAGE_PRICE_BY_CATEGORY,
    AVERAGE_PRODUCT_PRICE,
    TOP_PRODUCT_CATEGORIES,
    PRICE_RANGE,
    AVERAGE_DELIVERY_DAYS,
    ORDER_STATUS,
    REVIEW_SCORE,
    MONTHLY_REVIEWS,
    DELIVERY_PERFORMANCE,
)
from ai_assistant import ask_ai

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    /* ===========================
    Main Background
    =========================== */

    .stApp{
        background-color:#0B0F19;
        color:white;
    }

    /* ===========================
    Sidebar
    =========================== */

    /* ===========================
    Sidebar
    =========================== */

    section[data-testid="stSidebar"]{

        background: linear-gradient(
            180deg,
            #0B1020 0%,
            #111827 100%
        );

        border-right:2px solid #00E5FF;

        box-shadow:5px 0px 30px rgba(0,229,255,0.18);

    }
                /* Radio Labels */

    div[role="radiogroup"] label{

        padding:12px 16px;

        border-radius:12px;

        margin-bottom:8px;

        transition:0.3s;

        font-size:16px;

        font-weight:500;

    }
    /* Navigation Hover Effect */

    div[role="radiogroup"] label:hover{

        background:linear-gradient(
            90deg,
            rgba(0,229,255,0.15),
            rgba(0,229,255,0.05)
        );

        border-left:4px solid #00E5FF;

        border-radius:12px;

        transform:translateX(8px);

        transition:all .3s ease;

        box-shadow:0 0 15px rgba(0,229,255,.25);

    }

    /* ===========================
    Headers
    =========================== */

    h1,h2,h3{
        color:#00E5FF;
        font-family:Arial;
    }

    /* ===========================
    Metric Cards
    =========================== */

    div[data-testid="stMetric"]{

        background:#151A28;

        border:1px solid #00E5FF;

        border-radius:15px;

        padding:18px;

        box-shadow:0px 0px 12px rgba(0,229,255,0.25);

    }

    /* ===========================
    Metric Value
    =========================== */

    div[data-testid="stMetricValue"]{

        color:white;

        font-size:30px;

        font-weight:bold;

    }

    /* ===========================
    Metric Label
    =========================== */

    div[data-testid="stMetricLabel"]{

        color:#B0BEC5;

    }

    /* ===========================
    Buttons
    =========================== */

    .stButton>button{

        background:#00E5FF;

        color:black;

        border:none;

        border-radius:10px;

    }

    /* ===========================
    Selectbox
    =========================== */

    .stSelectbox{

        background:#151A28;

    }

    /* ===========================
    Divider
    =========================== */

    hr{

        border:1px solid #00E5FF;

    }

    </style>
    """,unsafe_allow_html=True)


    # -----------------------------
    # Sidebar
    # -----------------------------

st.sidebar.markdown("""
    <h1 style="
    color:#00E5FF;
    font-size:34px;
    margin-bottom:0;
    ">
    🛒 OLIST
    </h1>

    <p style="
    color:#B0BEC5;
    font-size:16px;
    margin-top:0;
    letter-spacing:1px;
    ">
    Analytics Platform
    </p>
    """, unsafe_allow_html=True)
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Olist Analytics Platform",
    page_icon="🛒",
    layout="wide"
)
st.title("📊 Olist Analytics Platform")

page = st.sidebar.radio(
    "📂 Navigation",
    [
        "📊 Executive Dashboard",
        "📈 Sales Analytics",
        "👥 Customer Analytics",
        "📦 Product Analytics",
        "🚚 Delivery & Reviews",
        "🤖 AI Business Assistant"
        ]
    )

st.sidebar.markdown("---")

st.sidebar.info(
        "💡 Brazilian E-Commerce Dashboard\n\nVersion 1.0"
    )

st.sidebar.markdown("---")

st.sidebar.caption("Developed by troubleshooters")




# -----------------------------
# Database Connection
# -----------------------------

@st.cache_resource
def get_db_connection():
    return get_connection()

conn = get_db_connection()
# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #121826, #1A2338);
    padding:25px;
    border-radius:18px;
    border:2px solid #00E5FF;
    box-shadow:0px 0px 20px rgba(0,229,255,0.35);
    margin-bottom:25px;
">

<h1 style="
    color:#00E5FF;
    margin-bottom:0px;
    font-size:42px;
">
🛒 OLIST ANALYTICS PLATFORM
</h1>

<p style="
    color:#B0BEC5;
    font-size:18px;
    margin-top:8px;
">
Brazilian E-Commerce Business Intelligence Dashboard
</p>

</div>
""", unsafe_allow_html=True)




# -----------------------------
# Executive Dashboard
# -----------------------------

if page == "📊 Executive Dashboard":

    st.subheader("📊 Executive Dashboard")

    # Load Filter Data
    years = pd.read_sql(YEARS, conn)
    states = pd.read_sql(STATES, conn)
    categories = pd.read_sql(CATEGORIES, conn)

    # Filters
    filter1, filter2, filter3, filter4 = st.columns(4)

    with filter1:
        selected_year = st.selectbox(
            "📅 Year",
            ["All"] + years["year"].astype(str).tolist()
        )

        #D:\OneDrive\Desktop\Olist_Project\dashboard\app.py 

    with filter2:
        selected_month = st.selectbox(
            "📅 Month",
            [
                "All",
                "January", "February", "March",
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"
            ]
        )

    with filter3:
        selected_state = st.selectbox(
            "🌎 State",
            ["All"] + states["customer_state"].tolist()
        )

    with filter4:
        selected_category = st.selectbox(
            "📦 Category",
            ["All"] + categories["product_category_name"].tolist()
        )

    # -----------------------------
    # Build Dashboard Filters
    # -----------------------------

    filter_conditions = []
    filter_params = []

    if selected_year != "All":
        filter_conditions.append(
            "YEAR(o.order_purchase_timestamp) = %s"
        )
        filter_params.append(int(selected_year))

    if selected_month != "All":
        month_number = [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ].index(selected_month) + 1

        filter_conditions.append(
            "MONTH(o.order_purchase_timestamp) = %s"
        )
        filter_params.append(month_number)

    if selected_state != "All":
        filter_conditions.append(
            "c.customer_state = %s"
        )
        filter_params.append(selected_state)

    if selected_category != "All":
        filter_conditions.append("""
            EXISTS (
                SELECT 1
                FROM order_items oi_filter
                JOIN products p_filter
                    ON oi_filter.product_id = p_filter.product_id
                WHERE oi_filter.order_id = o.order_id
                AND p_filter.product_category_name = %s
            )
        """)
        filter_params.append(selected_category)

    where_clause = ""

    if filter_conditions:
        where_clause = "WHERE " + " AND ".join(filter_conditions)

    # Fetch KPI Data

    # Filtered Orders
    orders_query = f"""
    SELECT COUNT(DISTINCT o.order_id) AS total_orders
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    {where_clause};
    """

    orders = pd.read_sql(
        orders_query,
        conn,
        params=filter_params
    )


    # Filtered Revenue
    revenue_query = f"""
    SELECT ROUND(SUM(op.payment_value), 2) AS total_revenue
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN order_payments op
        ON o.order_id = op.order_id
    {where_clause};
    """

    revenue = pd.read_sql(
        revenue_query,
        conn,
        params=filter_params
    )

    # Filtered Customers
    customers_query = f"""
    SELECT COUNT(DISTINCT c.customer_unique_id) AS total_customers
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    {where_clause};
    """

    customers = pd.read_sql(
        customers_query,
        conn,
        params=filter_params
    )
    # Keep these unchanged
   
    # Filtered Products
    products_query = f"""
    SELECT COUNT(DISTINCT p.product_id) AS total_products
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    {where_clause};
    """

    products = pd.read_sql(
        products_query,
        conn,
        params=filter_params
    )

    
    # Filtered Sellers
    sellers_query = f"""
    SELECT COUNT(DISTINCT oi.seller_id) AS total_sellers
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    {where_clause};
    """

    sellers = pd.read_sql(
        sellers_query,
        conn,
        params=filter_params
    )

    # Filtered Average Rating
    rating_query = f"""
    SELECT ROUND(AVG(r.review_score), 2) AS average_rating
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN order_reviews r
        ON o.order_id = r.order_id
    {where_clause};
    """

    rating = pd.read_sql(
        rating_query,
        conn,
        params=filter_params
    )

    # Filtered Monthly Revenue
    monthly_revenue_query = f"""
    SELECT DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
        ROUND(SUM(op.payment_value), 2) AS revenue
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN order_payments op
        ON o.order_id = op.order_id
    {where_clause}
    GROUP BY month
    ORDER BY month;
    """

    monthly_revenue = pd.read_sql(
        monthly_revenue_query,
        conn,
        params=filter_params
    )
    top_categories = pd.read_sql(TOP_CATEGORIES, conn)

    # ==========================
    # KPI Cards
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:
     st.metric(
        "📦 Orders",
        f"{orders.iloc[0,0]:,}"
    )

    with col2:
        st.metric("👥 Customers", f"{customers.iloc[0,0]:,}")

    revenue_value = revenue.iloc[0, 0]

    if pd.isna(revenue_value):
        revenue_value = 0

    st.metric("💰 Revenue", f"R$ {revenue_value:,.2f}")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("📦 Products", f"{products.iloc[0,0]:,}")

    with col5:
        st.metric("🏪 Sellers", f"{sellers.iloc[0,0]:,}")

    with col6:
        st.metric("⭐ Average Rating", f"{rating.iloc[0,0]}")

    # ==========================
    # Monthly Revenue Trend
    # ==========================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📈 Monthly Revenue Trend")

    monthly_revenue = monthly_revenue.set_index("month")

    st.line_chart(
        monthly_revenue["revenue"],
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📌 Business Highlights")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.success(
            f"💰 Total Revenue : R$ {revenue_value:,.2f}"
        )

        st.info(
            f"📦 Total Orders : {orders.iloc[0,0]:,}"
        )

    with insight2:

        st.warning(
            f"🏪 Total Sellers : {sellers.iloc[0,0]:,}"
        )

        st.success(
            f"⭐ Average Rating : {rating.iloc[0,0]}"
        )

# ==========================================================
# SALES ANALYTICS
# ==========================================================
    
elif page == "📈 Sales Analytics":

    st.subheader("📈 Sales Analytics")

    st.caption("Revenue & Sales Performance Dashboard")

    revenue = pd.read_sql(TOTAL_REVENUE, conn)
    orders = pd.read_sql(TOTAL_ORDERS, conn)
    avg_order = pd.read_sql(AVERAGE_ORDER_VALUE, conn)
    monthly_revenue = pd.read_sql(MONTHLY_REVENUE, conn)
    payment = pd.read_sql(PAYMENT_METHOD, conn)
    state_revenue = pd.read_sql(REVENUE_BY_STATE, conn)
    category_sales = pd.read_sql(TOP_CATEGORY_SALES, conn)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1], gap="large")

    with col1:
        st.metric(
            "💰 Total Revenue",
            f"R$ {revenue.iloc[0,0]:,.2f}"
        )

    with col2:
        st.metric(
            "📦 Total Orders",
            f"{orders.iloc[0,0]:,}"
        )

    with col3:
        st.metric(
            "💵 Avg Order Value",
            f"R$ {avg_order.iloc[0,0]:,.2f}"
        )

# ==========================================================
# SALES ANALYTICS CHARTS
# ==========================================================

    st.markdown("---")

# ---------- FIRST ROW ----------
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("📊 Revenue by State")

        state_chart = state_revenue.set_index("customer_state")

        st.bar_chart(
            state_chart["revenue"],
            use_container_width=True,
            height=350
        )

    with col2:
        st.subheader("💳 Payment Method Distribution")

        payment = payment.sort_values("total", ascending=True)

        fig, ax = plt.subplots(figsize=(6,4))

        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#151A28")

        ax.barh(
            payment["payment_type"],
            payment["total"],
            color="#00E5FF"
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.tick_params(colors="white")

        ax.set_xlabel("Orders", color="white")
        ax.set_ylabel("")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)


# ---------- SECOND ROW ----------
    col3, col4 = st.columns(2, gap="large")

    with col3:

        st.subheader("🏆 Top 10 Product Categories")

        fig, ax = plt.subplots(figsize=(6,4))

        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#151A28")

        top_category = category_sales.loc[
            category_sales["revenue"].idxmax()]

        ax.barh(
        category_sales["product_category_name"],
        category_sales["revenue"],
        color="#00C49F"
)

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.tick_params(colors="white")

        ax.set_xlabel("Revenue (R$)", color="white")
        ax.set_ylabel("")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)


    with col4:

        st.subheader("📌 Sales Insights")

        top_category = category_sales.loc[
            category_sales["revenue"].idxmax()
        ]

        top_payment = payment.loc[
            payment["total"].idxmax()
        ]

        top_state = state_revenue.loc[
            state_revenue["revenue"].idxmax()
        ]

        with st.container(border=True):

            st.success(
            f"🏆 Top Category: {top_category['product_category_name']}"
            )

            st.info(
                f"💰 Revenue: R$ {top_category['revenue']:,.2f}"
            )

            st.success(
                f"💳 Most Used Payment: {top_payment['payment_type']}"
            )

            st.info(
                f"📍 Highest Revenue State: {top_state['customer_state']}"
            )

# ==========================================================
# CUSTOMER ANALYTICS
# ==========================================================
elif page == "👥 Customer Analytics":

    st.subheader("👥 Customer Analytics")
    st.caption("Customer Behavior & Geographic Insights")

    total_customers = pd.read_sql(TOTAL_CUSTOMERS, conn)
    customer_growth = pd.read_sql(CUSTOMER_GROWTH, conn)
    customers_state = pd.read_sql(CUSTOMERS_BY_STATE, conn)
    top_cities = pd.read_sql(TOP_CITIES, conn)
    customer_type = pd.read_sql(NEW_RETURNING_CUSTOMERS, conn)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
        "👥 Total Customers",
        f"{total_customers.iloc[0,0]:,}"
        )

    with col2:
        st.metric(
        "🌍 States Covered",
        f"{customers_state.shape[0]}"
        )

    with col3:
        st.metric(
        "🏙️ Cities Covered",
        f"{top_cities.shape[0]}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Customer Growth Trend
# ==========================================================

    st.subheader("📈 Customer Growth Over Time")

    customer_growth = customer_growth.set_index("month")

    st.line_chart(
    customer_growth["customers"],
    use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    chart1, chart2 = st.columns(2)

    with chart1:

        st.subheader("🌍 Customers by State")

        state_chart = customers_state.set_index("customer_state")

        st.bar_chart(
        state_chart["total_customers"],
        use_container_width=True
        )

    with chart2:

        st.subheader("🏙️ Top 10 Cities")

        fig, ax = plt.subplots(figsize=(5,5))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        city_chart = top_cities.sort_values(
        "total_customers",
        ascending=True
        )

        ax.barh(
        city_chart["customer_city"],
        city_chart["total_customers"],
        color="#6BB6FF"
        )

        ax.set_xlabel("Customers", color="white")
        ax.set_ylabel("")

        ax.tick_params(colors="white")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")

        st.pyplot(fig)

    chart3, chart4 = st.columns(2)

    with chart3:

        st.subheader("🔄 New vs Returning Customers")

        fig, ax = plt.subplots(figsize=(5,5))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        colors = ["#4F8BF9", "#00C49F"]

        wedges, _, autotexts = ax.pie(
            customer_type["total"],
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            radius=0.72,
            wedgeprops=dict(width=0.22),
            textprops={"color": "white", "fontsize": 12}
        )
        

        ax.legend(
            wedges,
            customer_type["customer_type"],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.15),
            ncol=2,
            frameon=False,
            labelcolor="white",
            fontsize=10
        )

        ax.set_aspect("equal")  # <-- Remove use_container_width=True
        plt.tight_layout()

        st.pyplot(fig)

    with chart4:

        st.subheader("📌 Customer Insights")

        top_state = customers_state.iloc[0]
        top_city = top_cities.iloc[0]

        new_customer = customer_type[
            customer_type["customer_type"] == "New Customer"
        ]["total"].values[0]

        returning_customer = customer_type[
            customer_type["customer_type"] == "Returning Customer"
        ]["total"].values[0]

        st.success(f"🌍 Top State: {top_state['customer_state']}")
        st.info(f"👥 Customers: {top_state['total_customers']:,}")

        st.success(f"🏙️ Top City: {top_city['customer_city']}")
        st.info(f"👥 Customers: {top_city['total_customers']:,}")

        st.success(f"🆕 New Customers: {new_customer:,}")
        st.info(f"🔁 Returning Customers: {returning_customer:,}")

# ==========================================================
# PRODUCT ANALYTICS
# ==========================================================

elif page == "📦 Product Analytics":

    st.subheader("📦 Product Analytics")
    st.caption("Product Performance & Category Analysis")

    # ==========================
    # Load Data
    # ==========================

    products = pd.read_sql(TOTAL_PRODUCTS, conn)
    top_categories = pd.read_sql(TOP_PRODUCT_CATEGORIES, conn)
    avg_price = pd.read_sql(AVERAGE_PRODUCT_PRICE, conn)
    price_range = pd.read_sql(PRICE_RANGE, conn)
    avg_price_category = pd.read_sql(AVERAGE_PRICE_BY_CATEGORY, conn)

# ==========================================================
# Top Categories by Revenue
# ==========================================================

   
    # ==========================================================
# PRODUCT ANALYTICS CHARTS
# ==========================================================

    st.markdown("---")

# ---------------- FIRST ROW ----------------

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.subheader("🏆 Top Product Categories by Revenue")

        chart = top_categories.sort_values("revenue", ascending=False)

        fig, ax = plt.subplots(figsize=(8,6.5))

        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#151A28")

        ax.bar(
            chart["product_category_name"],
            chart["revenue"],
            color="#6BB6FF"
        )

        ax.set_xlabel("Category", color="white")
        ax.set_ylabel("Revenue (R$)", color="white")

        ax.tick_params(axis="x", colors="white", rotation=45)
        ax.tick_params(axis="y", colors="white")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)

    with col2:

        st.subheader("💰 Product Price Range")

        fig, ax = plt.subplots(figsize=(6,4))

        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#151A28")

        ax.bar(
            price_range["price_range"],
            price_range["total_products"],
            color="#4F8BF9"
        )

        ax.set_xlabel("Price Range", color="white")
        ax.set_ylabel("Products", color="white")

        ax.tick_params(colors="white")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)


# ---------------- SECOND ROW ----------------

    col3, col4 = st.columns(2, gap="large")

    with col3:

        st.subheader("💰 Average Price by Category")

        avg_chart = avg_price_category.sort_values(
            "avg_price",
            ascending=True
        )

        fig, ax = plt.subplots(figsize=(6,4))

        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#151A28")

        ax.barh(
            avg_chart["product_category_name"],
            avg_chart["avg_price"],
            color="#00C49F"
        )

        ax.set_xlabel("Average Price (R$)", color="white")
        ax.set_ylabel("")

        ax.tick_params(colors="white")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")

        plt.tight_layout()

        st.pyplot(fig, use_container_width=True)


    with col4:

        st.subheader("📌 Product Insights")

        top_category = top_categories.sort_values(
            "revenue",
            ascending=False
        ).iloc[0]

        premium_category = avg_price_category.sort_values(
            "avg_price",
            ascending=False
        ).iloc[0]

        st.success(
            f"🏆 Highest Revenue Category: {top_category['product_category_name']}"
        )

        st.info(
            f"💰 Revenue: R$ {top_category['revenue']:,.2f}"
        )

        st.success(
            f"💎 Highest Avg Price Category: {premium_category['product_category_name']}"
        )

        st.info(
            f"💰 Avg Price: R$ {premium_category['avg_price']:,.2f}"
        )

        st.metric(
            "📦 Total Products",
            f"{products.iloc[0,0]:,}"
        )

        st.metric(
            "💵 Overall Avg Price",
            f"R$ {avg_price.iloc[0,0]:,.2f}"
        )
# ==========================================================
# DELIVERY & REVIEWS
# ==========================================================

elif page == "🚚 Delivery & Reviews":

    st.subheader("🚚 Delivery & Reviews")
    st.caption("Delivery Performance & Customer Satisfaction")

    # ==========================
    # Load Data
    # ==========================

    avg_delivery = pd.read_sql(AVERAGE_DELIVERY_DAYS, conn)
    avg_rating = pd.read_sql(AVERAGE_RATING, conn)
    order_status = pd.read_sql(ORDER_STATUS, conn)
    review_score = pd.read_sql(REVIEW_SCORE, conn)
    monthly_reviews = pd.read_sql(MONTHLY_REVIEWS, conn)
    delivery = pd.read_sql(DELIVERY_PERFORMANCE, conn)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🚚 Avg Delivery Days",
            f"{avg_delivery.iloc[0,0]} Days"
        )

    with col2:
        st.metric(
            "⭐ Avg Rating",
            f"{avg_rating.iloc[0,0]}"
        )

    with col3:
        delivered = order_status[
            order_status["order_status"] == "delivered"
        ]["total"].values[0]

        st.metric(
            "📦 Delivered Orders",
            f"{delivered:,}"
        )

    st.markdown("---")

 # ==========================================================
# Monthly Review Trend
# ==========================================================

    st.subheader("📈 Monthly Average Rating Trend")

    fig, ax = plt.subplots(figsize=(12,4))

    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#151A28")

    ax.plot(
        monthly_reviews["month"],
        monthly_reviews["avg_rating"],
        color="#6BB6FF",
        linewidth=2.5,
        marker="o",
        markersize=5
    )

    ax.set_xlabel("")
    ax.set_ylabel("Average Rating", color="white")

    ax.tick_params(axis="x", colors="white", rotation=45)
    ax.tick_params(axis="y", colors="white")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")

    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)
    st.markdown("---")

    # ==========================================================
# FIRST ROW
# ==========================================================

    chart1, chart2 = st.columns(2, gap="large")

# -----------------------------
# Order Status
# -----------------------------
    with chart1:

        st.subheader("📦 Order Status Distribution")

        fig, ax = plt.subplots(figsize=(4,4))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        colors = [
            "#4F8BF9",
            "#00C49F",
            "#F4B400",
            "#DB4437",
            "#AA23C2",
            "#13C8DF"
        ]

        wedges, _, autotexts = ax.pie(
            order_status["total"],
            startangle=90,
            colors=colors,
            radius=0.72,
            wedgeprops=dict(width=0.28),
            autopct=lambda p: f"{p:.1f}%" if p > 3 else "",
            textprops={"color":"white","fontsize":12}
        )

        ax.legend(
            wedges,
            order_status["order_status"],
            loc="lower center",
            bbox_to_anchor=(0.5,-0.05),
            ncol=3,
            frameon=False,
            labelcolor="white"
        )

        ax.set_aspect("equal")

        st.pyplot(fig)


# -----------------------------
# Review Score
# -----------------------------
    with chart2:

        st.subheader("⭐ Review Score Distribution")

        review_chart = review_score.set_index("review_score")

        st.bar_chart(
            review_chart["total"],
            use_container_width=True,
            height=350
        )


# ==========================================================
# SECOND ROW
# ==========================================================

    chart3, chart4 = st.columns(2, gap="large")


# -----------------------------
# Delivery Performance
# -----------------------------
    with chart3:

        st.subheader("🚚 Delivery Performance")

        fig, ax = plt.subplots(figsize=(4,4))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        colors = ["#00C49F","#DB4437"]

        wedges, _, autotexts = ax.pie(
            delivery["total"],
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            radius=0.72,
            wedgeprops=dict(width=0.28),
            textprops={"color":"white","fontsize":12}
        )

        ax.legend(
            wedges,
            delivery["delivery_status"],
            loc="lower center",
            bbox_to_anchor=(0.5,-0.05),
            ncol=2,
            frameon=False,
            labelcolor="white"
        )

        ax.set_aspect("equal")

        st.pyplot(fig)


# -----------------------------
# Insights
# -----------------------------
    with chart4:

        st.subheader("📌 Delivery Insights")

        on_time = delivery[
            delivery["delivery_status"] == "On Time"
        ]["total"].values[0]

        late = delivery[
            delivery["delivery_status"] == "Late"
        ]["total"].values[0]

        best_review = review_score.sort_values(
            "total",
            ascending=False
        ).iloc[0]

        with st.container(border=True):

            st.success(
            f"🚚 On-Time Deliveries: {on_time:,}"
            )

            st.warning(
            f"⏰ Late Deliveries: {late:,}"
            )

            st.success(
            f"⭐ Most Common Rating: {best_review['review_score']} Stars"
            )

            st.info(
            f"📝 Reviews: {best_review['total']:,}"
            )

elif page == "🤖 AI Business Assistant":

    st.title("🤖 AI Business Assistant")

    st.caption("Ask questions about the Olist dataset using natural language.")

    st.info("""
Examples:

• Which product generated the highest revenue?

• Show monthly sales trend.

• Which state has the highest revenue?

• Which payment method is most popular?

• Show customer growth.

• Which city has the most customers?
""")

    question = st.text_input(
        "Ask your question"
    )

    if st.button("Ask AI"):

        with st.spinner("Analyzing data..."):

            answer, df = ask_ai(question, conn)

        st.success(answer)

        if df is not None:

            st.subheader("Dataset Result")

            st.dataframe(df)
conn.close()
