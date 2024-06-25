import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('./sales_data.csv')

# Plot Sales Amount over Time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales Amount'], marker='o', linestyle='-')
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Correlation Matrix
correlation_matrix = df[['Sales Amount', 'Number of Products Sold', 'Marketing Expenditure']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()
