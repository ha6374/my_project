def analyze_monthly_sales(data):
 return data.groupby(data['sale_date'].dt.to_period('M'))['Total Sales'].sum()
          
