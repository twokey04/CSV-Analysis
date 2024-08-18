import pandas as pd


class Reporter:
    def __init__(self, total_sales_df, top_selling_df, profit_df):
        self.total_sales_df = total_sales_df
        self.top_selling_df = top_selling_df
        self.profit_df = profit_df

    def generate_summary(self):
        """Generate a summary report."""
        # Ensure all required columns are present in the dataframes
        required_columns = {'ProductID', 'ProductName'}
        if not required_columns.issubset(self.total_sales_df.columns):
            raise ValueError("Total Sales DataFrame must contain 'ProductID' and 'ProductName' columns.")
        if not required_columns.issubset(self.profit_df.columns):
            raise ValueError("Profit DataFrame must contain 'ProductID' and 'ProductName' columns.")

        # Merge total sales with profit data
        summary_df = pd.merge(self.total_sales_df, self.profit_df[['ProductID', 'ProductName', 'Profit']],
                              on=['ProductID', 'ProductName'], how='left')

        # Create the Top5BestSeller column
        summary_df['Top5BestSeller'] = summary_df['ProductID'].isin(self.top_selling_df['ProductID'])

        # Rename columns to match the required format
        summary_df = summary_df.rename(columns={'TotalSales': 'TotalSales', 'Profit': 'TotalProfit'})

        # Reorder columns
        summary_df = summary_df[['ProductID', 'ProductName', 'TotalSales', 'TotalProfit', 'Top5BestSeller']]

        # Save to CSV
        summary_df.to_csv('sales_summary.csv', index=False)
        print("Summary report generated: sales_summary.csv")
