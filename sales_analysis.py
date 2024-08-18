from data_processing.data_loader import DataLoader
from data_processing.data_integrator import DataIntegrator
from data_processing.data_analysis import DataAnalyzer
from ml.sales_predict import SalesPredictor
from utils.pretty_print import print_header
import os


def main():
    # Install requirements
    print_header("Installing Required Packages")
    exit_code = os.system('pip install -r requirements.txt')
    if exit_code == 0:
        print("Installation completed successfully.")
    else:
        print(f"An error occurred during installation. Exit code: {exit_code}")

    # Initialize data loader
    data_loader = DataLoader('data/sales_data.csv', 'data/product_info.csv')

    print_header("Load & Preprocess Data")
    # Load and preprocess data
    data_loader.load_data()
    data_loader.preprocess_data()

    # Create Product and Sale objects
    data_loader.create_objects()
    print("Data Loaded Preprocessed Successfully")

    # Integrate data
    data_integrator = DataIntegrator(data_loader.get_sales(), data_loader.get_products())
    data_integrator.integrate_data()
    merged_df = data_integrator.get_merged_data()

    print_header("Data Integration")
    print(merged_df.head(10))  # Print merged DataFrame to verify

    # Data Analysis
    print_header("Calculate Total Sales")
    data_analyzer = DataAnalyzer(merged_df)
    total_sales_df = data_analyzer.calculate_total_sales()
    print(total_sales_df.head())  # Display total sales

    print_header("Identify Top 5 Best-Selling Products")
    top_selling_products_df = data_analyzer.identify_top_selling_products(total_sales_df)
    top_selling_products_df = top_selling_products_df.reset_index(drop=True)
    print(top_selling_products_df)  # Display top 5 products

    print_header("Compute Profit")
    profit_df = data_analyzer.compute_profit()
    print(profit_df[['ProductID', 'ProductName', 'Sales', 'CostPrice', 'Profit']].head())  # Display sample profit

    # Ensure unique ProductID in profit_df
    profit_df = profit_df.drop_duplicates(subset='ProductID')

    # Generate Summary Report
    print_header("Generate Summary Report")
    # Use total_sales_df for the summary to include all products with sales data
    summary_report = total_sales_df.copy()

    # Merge profit_df with summary_report on ProductID
    summary_report = summary_report.merge(profit_df[['ProductID', 'Profit']], on='ProductID', how='left')

    summary_report['Top5BestSeller'] = summary_report['ProductID'].isin(top_selling_products_df['ProductID'])

    # Fill missing 'TotalProfit' with 0 (products without profit data)
    summary_report['Profit'] = summary_report['Profit'].fillna(0)

    # Rename columns for clarity
    summary_report.rename(columns={'Profit': 'TotalProfit'}, inplace=True)

    # Save the summary report
    summary_report.to_csv('reports/sales_summary.csv', index=False)
    print("\nSummary report saved as 'data/sales_summary.csv'")

    # Train the model
    print_header("Train and Evaluate the Model")
    sales_predictor = SalesPredictor(merged_df)
    sales_predictor.train_model()

    # Make predictions about future sales
    print_header("Predict Future Sales")
    future_data = [{'CostPrice': cp} for cp in merged_df['CostPrice'].unique()]
    future_sales_df = sales_predictor.predict_future_sales(future_data)
    print(future_sales_df.head())  # Display future sales predictions


if __name__ == '__main__':
    main()
