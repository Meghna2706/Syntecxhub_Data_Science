import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

data = pd.DataFrame({
    'Region': np.random.choice(['A', 'B'], 300),
    'Sales': np.concatenate([
        np.random.normal(300, 50, 150),   # Region A
        np.random.normal(400, 80, 150)    # Region B
    ])
})

# 1. Histogram
plt.figure()
plt.hist(data['Sales'], bins=15)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Sales Distribution (Histogram)')
plt.savefig('histogram_sales.png')
plt.close()

# 2. KDE (Density plot)
plt.figure()
data[data['Region'] == 'A']['Sales'].plot(kind='kde', label='Region A')
data[data['Region'] == 'B']['Sales'].plot(kind='kde', label='Region B')
plt.xlabel('Sales')
plt.title('Sales Density by Region')
plt.legend()
plt.savefig('kde_sales.png')
plt.close()

# 3. Boxplot (Outlier detection)
plt.figure()
data.boxplot(column='Sales', by='Region')
plt.title('Sales Boxplot by Region')
plt.suptitle('')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.savefig('boxplot_sales.png')
plt.close()

print("Statistical plots saved as PNG files.")
data.to_csv('sales_data_stats.csv', index=False)
print("Sales data saved as 'sales_data_stats.csv'.")