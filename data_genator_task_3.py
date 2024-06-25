import pandas as pd
import numpy as np

# Generating sample transaction data
np.random.seed(0)  # for reproducibility

# Sample size
num_records = 1000

# Generate data
transaction_id = np.arange(1, num_records + 1)
dates = pd.date_range(start='2023-01-01', periods=num_records)
times = pd.to_datetime(np.random.randint(0, 24*60*60, num_records), unit='s').strftime('%H:%M:%S')
amounts = np.random.uniform(1, 1000, num_records)
merchants = np.random.choice(['Amazon', 'Walmart', 'Target', 'Best Buy'], num_records)
card_numbers = np.random.randint(1000, 9999, num_records)
transaction_types = np.random.choice(['purchase', 'refund'], num_records)

# Create DataFrame
df_transactions = pd.DataFrame({
    'Transaction ID': transaction_id,
    'Date': dates,
    'Time': times,
    'Amount': amounts,
    'Merchant': merchants,
    'Card Number': card_numbers,
    'Transaction Type': transaction_types
})

# Save to CSV
df_transactions.to_csv('transaction_data.csv', index=False)
