import pandas as pd
import numpy as np

# Generating sample production data
np.random.seed(0)  # for reproducibility

# Sample size
num_records = 200

# Generate data
production_date = pd.date_range(start='2023-01-01', periods=num_records)
product_id = np.random.randint(1, 11, size=num_records)
production_time = np.random.uniform(1.5, 3.0, size=num_records)
temperature = np.random.randint(20, 30, size=num_records)
humidity = np.random.randint(50, 70, size=num_records)
quality_score = np.random.randint(75, 95, size=num_records)

# Create DataFrame
df_production = pd.DataFrame({
    'Production Date': production_date,
    'Product ID': product_id,
    'Production Time': production_time,
    'Temperature': temperature,
    'Humidity': humidity,
    'Quality Score': quality_score
})

# Save to CSV
df_production.to_csv('production_data.csv', index=False)
