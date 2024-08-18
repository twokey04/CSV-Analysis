import pandas as pd
from classes.product import Product
from classes.sale import Sale


class DataLoader:
    def __init__(self, sales_file, products_file):
        self.sales_file = sales_file
        self.products_file = products_file
        self.sales = []
        self.products = []

    def load_data(self):
        """Load CSV files into pandas DataFrames."""
        self.sales_df = pd.read_csv(self.sales_file)
        self.products_df = pd.read_csv(self.products_file)
        print("Loaded sales data columns:", self.sales_df.columns)
        print("Loaded products data columns:", self.products_df.columns)

    def preprocess_data(self):
        """Preprocess the data if necessary."""
        self.sales_df['DateSold'] = pd.to_datetime(self.sales_df['DateSold'])
        print("Preprocessed sales data:")
        print(self.sales_df.head())

    def create_objects(self):
        """Create Product and Sale objects from the data."""
        self.products = [
            Product(row['ProductID'], row['Supplier'], row['CostPrice'])
            for _, row in self.products_df.iterrows()
        ]

        self.sales = [
            Sale(row['ProductID'], row['ProductName'], row['Category'], row['Sales'], row['DateSold'])
            for _, row in self.sales_df.iterrows()
        ]

    def get_sales(self):
        return self.sales

    def get_products(self):
        return self.products
