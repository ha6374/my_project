import warnings
from db_connection import create_connection
from data_processing import process_data
from analysis import analyze_monthly_sales
from visualization import plot_sales_trends
from export_results import export_to_files

if __name__ == "__main__":
    
  conn= create_connection()
  sales_data=process_data(conn)
  top_products = sales_data.groupby('product_id')['Total Sales'].sum().sort_values(ascending=False)

  monthly_sales=analyze_monthly_sales(sales_data)
  export_to_files(top_products,monthly_sales)
  plot_sales_trends(monthly_sales)
  
  print(sales_data['sale_date'].min(), sales_data['sale_date'].max())
  print(top_products)
  warnings.filterwarnings("ignore", message=".*identical low and high xlims.*")
  print("Min sale_date:", sales_data['sale_date'].min())
  print("Max sale_date:", sales_data['sale_date'].max())





  conn.close() 
