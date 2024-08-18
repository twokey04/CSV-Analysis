import pandas as pd

class DataIntegrator:
    def __init__(self, sales, products):
        self.sales = sales
        self.products = products
        self.merged_df = None

    def integrate_data(self):
        """Integrate sales and product data into a DataFrame."""
        # Extract sales data
        sales_data = [{
            'ProductID': sale.product_id,
            'ProductName': sale.product_name,
            'Category': sale.category,
            'Sales': sale.sales,
            'DateSold': sale.date_sold
        } for sale in self.sales]

        # Extract products data
        products_data = [{
            'ProductID': product.product_id,
            'Supplier': product.supplier,
            'CostPrice': product.cost_price
        } for product in self.products]

        # Create DataFrames
        sales_df = pd.DataFrame(sales_data)
        products_df = pd.DataFrame(products_data)

        # Merge the two DataFrames on ProductID
        self.merged_df = pd.merge(sales_df, products_df, on='ProductID', how='left')

        # Fill missing values
        self.merged_df['ProductName'] = self.merged_df['ProductName'].fillna('NA')
        self.merged_df['Category'] = self.merged_df['Category'].fillna('NA')
        self.merged_df['Supplier'] = self.merged_df['Supplier'].fillna('NA')
        self.merged_df['CostPrice'] = self.merged_df['CostPrice'].fillna(0)

        # Ensure that 'Sales' and 'CostPrice' are treated as numeric
        self.merged_df['Sales'] = pd.to_numeric(self.merged_df['Sales'], errors='coerce').fillna(0)
        self.merged_df['CostPrice'] = pd.to_numeric(self.merged_df['CostPrice'], errors='coerce').fillna(0)

        pd.set_option('display.max_columns', None)

        # Verify integration results
        print("Integration complete. Merged data preview:")
        print(self.merged_df.head(10))  # Print first 10 rows to verify

        print(f"Total number of records in merged data: {len(self.merged_df)}")

    def get_merged_data(self):
        """Return the merged dataset."""
        return self.merged_df
