# Olist E-Commerce Analytics Dashboard

## Overview

The Olist E-Commerce Analytics Dashboard is a data analytics project built using Python, MySQL, Streamlit, and Google Gemini.

The project analyzes Brazilian e-commerce data and provides interactive dashboards for understanding sales, customers, products, payments, delivery performance, and customer reviews.

The project also includes an AI-powered Business Assistant that allows users to ask business questions in natural language and receive answers based on the data stored in the MySQL database.

## Business Problem

E-commerce businesses generate large amounts of data from orders, customers, products, payments, sellers, and customer reviews.

However, raw data alone does not provide an easy way to understand business performance.

This project aims to transform raw Olist e-commerce data into meaningful business insights by answering questions such as:

- How much revenue is being generated?
- How many orders and customers are there?
- Which product categories generate the most sales?
- Which states and cities have the most customers?
- Which payment methods are most frequently used?
- How many customers are new or returning?
- How well are orders being delivered?
- What are customers saying through their review scores?

The project combines data engineering, SQL analytics, interactive visualization, and Generative AI to create a single platform for exploring these business questions.

## Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset contains approximately **99,441 orders** and multiple related datasets covering different parts of the e-commerce business.

### Main Tables

- `customers` — Customer information and location
- `orders` — Order details and order status
- `order_items` — Products purchased in each order
- `order_payments` — Payment information
- `order_reviews` — Customer reviews and ratings
- `products` — Product information
- `sellers` — Seller information
- `geolocation` — Brazilian ZIP-code and geographic information

These datasets are loaded into a **MySQL relational database** and connected through primary and foreign-key relationships.

The project uses SQL queries to analyze the data and Streamlit to present the results through interactive dashboards.

## Tech Stack

### Programming & Data Analysis

- **Python** — Data processing, ETL, and application logic
- **Pandas** — Data cleaning and data transformation
- **Matplotlib** — Data visualization

### Database

- **MySQL** — Relational database for storing and querying e-commerce data
- **SQL** — Business analysis and dashboard queries

### Dashboard

- **Streamlit** — Interactive web dashboard

### Generative AI

- **Google Gemini API** — Natural-language business question answering

### Environment & Configuration

- **python-dotenv** — Managing environment variables
- **Git & GitHub** — Version control and project management

## Project Architecture

The project follows a simple data analytics pipeline:

```text
Olist CSV Dataset
        │
        ▼
Python ETL Pipeline
(Pandas)
        │
        ▼
MySQL Database
        │
        ▼
SQL Queries
        │
        ▼
Streamlit Dashboard
        │
        ▼
Gemini AI Assistant
```

## Database Schema

The project uses MySQL as the relational database.

### Main Tables

| Table | Purpose |
|---|---|
| `customers` | Stores customer details and location |
| `orders` | Stores order information and status |
| `order_items` | Stores products included in each order |
| `order_payments` | Stores payment details |
| `order_reviews` | Stores customer reviews and ratings |
| `products` | Stores product information |
| `sellers` | Stores seller information |
| `geolocation` | Stores geographic information |

### Key Relationships

```text
customers
    │
    └── orders
          │
          ├── order_items ── products
          │       │
          │       └── sellers
          │
          ├── order_payments
          │
          └── order_reviews
```

## ETL Process

The project uses Python-based ETL scripts to load the Olist datasets into MySQL.

### ETL Workflow

```text
CSV Files
   ↓
Read Data using Pandas
   ↓
Clean & Transform Data
   ↓
Handle Missing Values
   ↓
Convert Data Types
   ↓
Load into MySQL
   ↓
Verify Loaded Data
```

The ETL scripts are located inside the `etl/` directory:

- `load_data.py` — Data loading operations
- `load_table.py` — Generic table loading functionality
- `load_all_tables.py` — Coordinates loading of database tables

The database connection is managed separately through `database/connection.py`.

## Dashboard Features

The Streamlit dashboard provides multiple analytical sections.

### Executive Dashboard

- Total orders
- Total customers
- Total products
- Total sellers
- Revenue
- Average rating
- Average order value
- Interactive filters

### Sales Analytics

- Monthly revenue
- Revenue by state
- Payment method analysis
- Top product categories

### Customer Analytics

- Customer growth
- Customers by state
- Top cities
- New vs returning customers

### Product Analytics

- Product category sales
- Average product price
- Average price by category
- Product price ranges

### Delivery & Reviews

- Average delivery time
- Order status distribution
- Delivery performance
- Review score distribution
- Monthly review trends

## AI Business Assistant

The project includes an AI-powered Business Assistant using the Google Gemini API.

Users can ask questions about the business data using natural language.

### How It Works

```text
User Question
      ↓
Gemini identifies the relevant analytical query
      ↓
SQL query executes against MySQL
      ↓
Query result returned
      ↓
Gemini explains the result
      ↓
Business-focused answer
```

The assistant uses predefined analytical SQL queries and Gemini to select the appropriate query and explain the resulting data in simple business language.

### Example Questions

- "What is the average order value?"
- "Which states generate the most revenue?"
- "What are the most popular payment methods?"
- "Which product categories generate the most sales?"

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Olist_Project
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=olist
GEMINI_API_KEY=your_gemini_api_key
```

**Do not commit the `.env` file to GitHub.**

### 6. Set Up MySQL

Create the `olist` database and load the required Olist tables using the ETL scripts.

### 7. Run the Dashboard

```bash
python -m streamlit run dashboard/app.py
```

On Windows, you can also run:

```bash
.venv_new\Scripts\python.exe -m streamlit run dashboard\app.py
```

## Key Business Insights

Based on the analysis performed in the project:

- Total orders analyzed: **99,441**
- Total payment revenue: **R$ 16,008,872.12**
- Average order value: **R$ 160.99**
- São Paulo generated **R$ 5,998,226.96** in payment revenue.
- Credit card payments were associated with **76,505 unique orders**.
- Health & Beauty generated approximately **R$ 1,258,681.34** in item sales.
- Among delivered orders, **88,649** were classified as on time and **7,827** as late.

> **Note:** Metric definitions can differ depending on the analysis. For example, overall revenue uses `payment_value`, while category sales use item `price`.

## Project Structure

```text
Olist_Project/
├── .gitignore
├── README.md
├── .env
├── requirements.txt
├── data/
├── database/
│   ├── connection.py
│   └── __init__.py
├── etl/
│   ├── load_data.py
│   ├── load_table.py
│   └── load_all_tables.py
└── dashboard/
    ├── app.py
    ├── queries.py
    ├── charts.py
    ├── ai_assistant.py
    └── logo.png
```

## Security

Sensitive configuration such as database passwords and API keys is stored in environment variables.

The `.env` file and virtual environments are excluded from Git using `.gitignore`.

API keys and passwords should never be committed to the public repository.

## Future Improvements

- Add more advanced business metrics
- Improve dashboard performance
- Add additional AI-powered analytical capabilities
- Deploy the dashboard to a cloud platform
- Add automated data refresh and ETL pipelines