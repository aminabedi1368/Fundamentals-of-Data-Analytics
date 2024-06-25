from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd


# Assuming 'data.csv' contains your dataset
df = pd.read_csv('./sales_data.csv')

# Selecting columns 'Number of Products Sold' and 'Marketing Expenditure'
X = df[['Number of Products Sold', 'Marketing Expenditure']]

# Print the first few rows to verify
print(X.head())
# Prepare data for regression
# X = df[['Number of Products Sold', 'Marketing Expenditure']]
y = df['Sales Amount']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Plot predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Sales Amount')
plt.grid(True)
plt.show()
