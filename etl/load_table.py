import pandas as pd
import math

def load_table(
    conn,
    cursor,
    csv_path,
    table_name,
    create_query,
    insert_query,
    date_columns=None
):
    print(f"\n{'='*50}")
    print(f"Loading Table : {table_name}")
    print(f"{'='*50}")

    # Read CSV
    df = pd.read_csv(csv_path)

    # Convert date columns (if any)
    if date_columns:
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Convert DataFrame to object datatype
    # This allows None values to exist
    df = df.astype(object)

    # Replace NaN / NaT with None
    df = df.where(pd.notnull(df), None)

    print(f"Records Found : {len(df)}")

    # Drop table if it already exists
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()

    print("Old table dropped.")

    # Create table
    cursor.execute(create_query)
    conn.commit()

    print(f"{table_name} table created successfully.")

    # Convert DataFrame to list of tuples
    data = list(df.itertuples(index=False, name=None))

    print(f"Prepared {len(data)} rows for insertion.")

    # Final safety check for NaN values
    cleaned_data = []

    for row in data:
        cleaned_row = []

        for value in row:

            # Replace float NaN with None
            if isinstance(value, float) and math.isnan(value):
                cleaned_row.append(None)

            # Replace pandas NA / NaT with None
            elif pd.isna(value):
                cleaned_row.append(None)

            else:
                cleaned_row.append(value)

        cleaned_data.append(tuple(cleaned_row))

    # Insert records
    try:
        cursor.executemany(insert_query, cleaned_data)
        conn.commit()

        print(f"{len(cleaned_data)} rows inserted successfully into '{table_name}'.")

    except Exception as e:
        print("\nError while inserting data:")
        print(e)
        conn.rollback()
        return

    # Verify
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()

    print(f"Total rows in {table_name}: {count[0]}")

    print(f"{'='*50}\n")