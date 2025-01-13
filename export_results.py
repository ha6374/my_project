def export_to_files(top_products,monthly_sales):
    top_products.to_csv('top_products.csv',index=True)
    monthly_sales.to_csv('monthly_sales.csv',index=True)
    
    print("Results exported to top_products.csv'and' monthly_sales.xlsx'")