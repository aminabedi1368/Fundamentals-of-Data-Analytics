import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Generate dates
dates = pd.date_range(start='2023-01-01', periods=200, freq='D')

# Generate random sales data
sales_amount = np.random.normal(loc=1000, scale=200, size=200).round(2)
number_of_products_sold = np.random.poisson(lam=50, size=200)
marketing_expenditure = np.random.normal(loc=300, scale=50, size=200).round(2)
regions = np.random.choice(['North', 'South', 'East', 'West'], size=200)

# Create DataFrame
data = {
    'Date': dates,
    'Sales Amount': sales_amount,
    'Number of Products Sold': number_of_products_sold,
    'Marketing Expenditure': marketing_expenditure,
    'Region': regions
}

df = pd.DataFrame(data)
df.to_csv('./sales_data.csv', index=False)

df.head()
