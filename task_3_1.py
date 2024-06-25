import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.covariance import EllipticEnvelope
import matplotlib.pyplot as plt

# Load transaction data from CSV
df_transactions = pd.read_csv('transaction_data.csv')

# Represent transaction data as a matrix
X = df_transactions[['Amount']].values  # Consider 'Amount' as the feature for simplicity

# Apply Principal Component Analysis (PCA) for dimensionality reduction
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)

# Apply Elliptic Envelope for outlier detection
outlier_detection = EllipticEnvelope(contamination=0.05)
outlier_detection.fit(X_pca)
df_transactions['Anomaly'] = outlier_detection.predict(X_pca)

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
