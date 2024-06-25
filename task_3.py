import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Load transaction data from CSV
df_transactions = pd.read_csv('transaction_data.csv')

# Utilize linear algebra to represent transaction data as vectors and matrices (if applicable)

# Apply anomaly detection algorithm (Isolation Forest)
model = IsolationForest(contamination=0.05, random_state=0)
df_transactions['Anomaly'] = model.fit_predict(df_transactions[['Amount']])

# Separate normal and anomaly transactions
normal_transactions = df_transactions[df_transactions['Anomaly'] == 1]
anomaly_transactions = df_transactions[df_transactions['Anomaly'] == -1]

# Visualize anomalies
plt.figure(figsize=(10, 6))
plt.scatter(normal_transactions['Date'], normal_transactions['Amount'], color='blue', label='Normal')
plt.scatter(anomaly_transactions['Date'], anomaly_transactions['Amount'], color='red', label='Anomaly')
plt.title('Anomaly Detection in Credit Card Transactions')
plt.xlabel('Date')
plt.ylabel('Transaction Amount')
plt.legend()
plt.show()

# Output flagged suspicious transactions for further investigation
flagged_transactions = anomaly_transactions[['Transaction ID', 'Date', 'Time', 'Amount', 'Merchant', 'Card Number', 'Transaction Type']]
print("Flagged Suspicious Transactions:")
print(flagged_transactions)
