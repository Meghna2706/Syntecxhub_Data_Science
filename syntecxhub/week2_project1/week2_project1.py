import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create simple sales data
dates = pd.date_range('2023-01-01', periods=180)
categories = ['A', 'B', 'C']

df = pd.DataFrame({
    'Date': np.random.choice(dates, 300),
    'Category': np.random.choice(categories, 300),
    'Sales': np.random.randint(100, 500, 300)
})

# 1. Line chart – Sales over time
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure()
plt.plot(daily_sales.index, daily_sales.values)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Daily Sales Trend')
plt.savefig('line_sales.png')
plt.close()

# 2. Bar chart – Total sales per category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure()
plt.bar(category_sales.index, category_sales.values)
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Sales by Category')
plt.savefig('bar_category_sales.png')
plt.close()

# 3. Pie chart – Sales share
plt.figure()
plt.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%')
plt.title('Sales Share by Category')
plt.savefig('pie_sales_share.png')
plt.close()

# 4. Histogram – Sales distribution
plt.figure()
plt.hist(df['Sales'], bins=10)
plt.xlabel('Sales Value')
plt.ylabel('Frequency')
plt.title('Sales Distribution')
plt.savefig('hist_sales.png')
plt.close()

print("Charts generated and saved as PNG files.")

df.to_csv('sales_data.csv', index=False)
print("Sales data saved as 'sales_data.csv'.")
