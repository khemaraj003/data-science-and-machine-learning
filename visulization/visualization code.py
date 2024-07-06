import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)  # For reproducibility

months = pd.date_range(start='2023-01-01', periods=12, freq='M').strftime('%B')
regions = ['North', 'South', 'East', 'West']
data = []

for month in months:
    for region in regions:
        total_sales = np.random.uniform(10000, 50000)
        units_sold = np.random.randint(100, 500)
        avg_unit_price = total_sales / units_sold
        data.append([month, region, total_sales, units_sold, avg_unit_price])

df = pd.DataFrame(data, columns=['Month', 'Region', 'Total Sales', 'Units Sold', 'Average Unit Price'])
df.head()
# Setting the style for the plots
plt.style.use('seaborn-whitegrid')

# Total Sales by Month
total_sales_month = df.groupby('Month')['Total Sales'].sum().reindex(months)

plt.figure(figsize=(14, 7))
plt.bar(total_sales_month.index, total_sales_month.values)
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Total Sales by Region
total_sales_region = df.groupby('Region')['Total Sales'].sum()

plt.figure(figsize=(14, 7))
plt.bar(total_sales_region.index, total_sales_region.values)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# Average Unit Price by Region
plt.figure(figsize=(14, 7))
df.boxplot(column='Average Unit Price', by='Region')
plt.title('Average Unit Price by Region')
plt.suptitle('')
plt.xlabel('Region')
plt.ylabel('Average Unit Price')
plt.show()

# Units Sold by Month and Region
units_sold_pivot = df.pivot(index='Month', columns='Region', values='Units Sold').reindex(months)

plt.figure(figsize=(14, 7))
for region in regions:
    plt.plot(units_sold_pivot.index, units_sold_pivot[region], marker='o', label=region)
plt.title('Units Sold by Month and Region')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.show()
