import os
import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define the data directory
data_dir = '../data'

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Function to generate sample sales data
def generate_sales_data(num_records=100, num_products=20):
    sales_data = []
    for _ in range(num_records):
        product_id = random.randint(1, num_products)  # Ensure product_id is within the range of available products
        sales = round(random.uniform(100.0, 5000.0), 2)
        date_sold = fake.date_this_year()
        sales_data.append({
            'ProductID': product_id,
            'ProductName': f"Product_{product_id}",
            'Category': random.choice(['Electronics', 'Furniture', 'Toys', 'Clothing', 'Food']),
            'Sales': sales,
            'DateSold': date_sold
        })
    return pd.DataFrame(sales_data)

# Function to generate sample product information data
def generate_product_info(num_products=20):
    product_info = []
    for product_id in range(1, num_products + 1):
        cost_price = round(random.uniform(50.0, 3000.0), 2)
        product_info.append({
            'ProductID': product_id,
            'Supplier': fake.company(),
            'CostPrice': cost_price
        })
    return pd.DataFrame(product_info)

# Number of products and sales records
num_products = 2000
num_sales_records = 10000

# Generate and save product_info.csv
product_info = generate_product_info(num_products)
product_info.to_csv(os.path.join(data_dir, 'product_info.csv'), index=False)
print("product_info.csv has been created and populated.")

# Generate and save sales_data.csv
sales_data = generate_sales_data(num_sales_records, num_products)
sales_data.to_csv(os.path.join(data_dir, 'sales_data.csv'), index=False)
print("sales_data.csv has been created and populated.")
