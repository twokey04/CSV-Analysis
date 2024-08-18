# CSV Data Analysis and Sales Prediction

## Project Overview

This project involves analyzing sales data from two CSV files (`sales_data.csv` and `product_info.csv`). The analysis includes data integration, cleaning, computing sales and profit metrics, identifying top-selling products, and making sales predictions using machine learning. The project is divided into several steps, each handled by a separate Python script.

## Setup and Installation

### Prerequisites

- Python 3.10 or later
- Recommended IDE: PyCharm

### Installing Dependencies

Clone the repository and navigate to the project directory. Then, install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Generating Sample Data

To generate the sample `sales_data.csv` and `product_info.csv` files, run:

```bash
python3 utils/mock_file_generator.py
```