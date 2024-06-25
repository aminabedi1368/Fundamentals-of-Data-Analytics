from scipy.stats import ttest_ind, f_oneway
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load production data from CSV
df_production = pd.read_csv('production_data.csv')

# Perform t-tests for each variable
t_stat_time, p_val_time = ttest_ind(df_production['Quality Score'], df_production['Production Time'])
t_stat_temp, p_val_temp = ttest_ind(df_production['Quality Score'], df_production['Temperature'])
t_stat_humid, p_val_humid = ttest_ind(df_production['Quality Score'], df_production['Humidity'])

print(f'Test for Production Time - t-statistic: {t_stat_time:.2f}, p-value: {p_val_time:.4f}')
print(f'Test for Temperature - t-statistic: {t_stat_temp:.2f}, p-value: {p_val_temp:.4f}')
print(f'Test for Humidity - t-statistic: {t_stat_humid:.2f}, p-value: {p_val_humid:.4f}')

# Perform ANOVA for each variable
anova_time, p_val_anova_time = f_oneway(df_production['Quality Score'], df_production['Production Time'])
anova_temp, p_val_anova_temp = f_oneway(df_production['Quality Score'], df_production['Temperature'])
anova_humid, p_val_anova_humid = f_oneway(df_production['Quality Score'], df_production['Humidity'])

print(f'ANOVA for Production Time - F-statistic: {anova_time:.2f}, p-value: {p_val_anova_time:.4f}')
print(f'ANOVA for Temperature - F-statistic: {anova_temp:.2f}, p-value: {p_val_anova_temp:.4f}')
print(f'ANOVA for Humidity - F-statistic: {anova_humid:.2f}, p-value: {p_val_anova_humid:.4f}')

# Visualize relationships using plots
plt.figure(figsize=(16, 6))

# Scatter plot Production Time vs Quality Score
plt.subplot(1, 3, 1)
sns.scatterplot(x='Production Time', y='Quality Score', data=df_production)
plt.title('Production Time vs Quality Score')

# Scatter plot Temperature vs Quality Score
plt.subplot(1, 3, 2)
sns.scatterplot(x='Temperature', y='Quality Score', data=df_production)
plt.title('Temperature vs Quality Score')

# Scatter plot Humidity vs Quality Score
plt.subplot(1, 3, 3)
sns.scatterplot(x='Humidity', y='Quality Score', data=df_production)
plt.title('Humidity vs Quality Score')

plt.tight_layout()
plt.show()

