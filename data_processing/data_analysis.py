class DataAnalyzer:
    def __init__(self, merged_df):
        self.merged_df = merged_df

    def calculate_total_sales(self):
        """Calculate total sales for each product."""
        total_sales = self.merged_df.groupby(['ProductID', 'ProductName'])['Sales'].sum().reset_index()
        total_sales.rename(columns={'Sales': 'TotalSales'}, inplace=True)
        return total_sales

    def identify_top_selling_products(self, total_sales_df):
        """Identify the top 5 best-selling products."""
        top_selling = total_sales_df.sort_values(by='TotalSales', ascending=False).head(5)
        return top_selling

    def compute_profit(self):
        """Compute profit for each product."""
        self.merged_df['Profit'] = self.merged_df['Sales'] - self.merged_df['CostPrice']
        return self.merged_df[['ProductID', 'ProductName', 'Sales', 'CostPrice', 'Profit']]
