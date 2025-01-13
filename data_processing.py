import pandas as pd

def process_data(conn):
    # Updated SQL query that includes price
    query = """
    SELECT s.sale_id, s.product_id, s.quantity, s.sale_date, p.price
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    """
    sales_df = pd.read_sql(query, conn)

    # Print the columns and the first few rows to verify
    print("Columns in the DataFrame:", sales_df.columns)
    print("First few rows of the DataFrame:\n", sales_df.head())

    # Ensure 'sale_date' exists in the columns (correct column name)
    if 'sale_date' in sales_df.columns:
        sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
    else:
        raise ValueError("The column 'sale_date' does not exist in the data.")

    # Calculate 'Total Sales' if necessary
    if 'Total Sales' not in sales_df.columns:
        if 'quantity' in sales_df.columns and 'price' in sales_df.columns:
            sales_df['Total Sales'] = sales_df['quantity'] * sales_df['price']
        else:
            raise ValueError("Missing columns needed to calculate 'Total Sales'.")

    return sales_df


    