import pandas as pd
import matplotlib.pyplot as plt

# Optional display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Replace with your CSV file name/path
df = pd.read_csv("superstore.csv", encoding='latin1')

print("DATASET LOADED:")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:\n")
print(df.dtypes)

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nStatistical Summary:\n")
print(df.describe())

print("DATA CLEANING:")

# Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Check duplicates
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Check null values again
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Create additional useful columns
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.month_name()

print("\nCleaned Dataset Shape:", df.shape)

print("EXPLORATORY DATA ANALYSIS:")

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# Average Discount
avg_discount = df['Discount'].mean()
print("Average Discount:", avg_discount)

# Top Categories
print("\nSales by Category:\n")
print(df.groupby('Category')['Sales'].sum())

# Top Sub Categories
print("\nTop 10 Sub-Categories by Sales:\n")
print(df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10))

# Region Wise Sales
print("\nRegion Wise Sales:\n")
print(df.groupby('Region')['Sales'].sum())

# State Wise Profit
print("\nTop 10 States by Profit:\n")
print(df.groupby('State')['Profit'].sum().sort_values(ascending=False).head(10))


# Visualizations

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# Bottom 10 Sub-Categories by Sales
sub_category_sales = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=True)
    .head(10)
)
plt.figure(figsize=(12, 6))
plt.bar(sub_category_sales.index, sub_category_sales.values)

plt.title("Bottom 10 Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Profit by Category
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_profit.index, category_profit.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()



# Monthly Sales Trend
monthly_sales = df.groupby('Order Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(range(1, 13))

plt.grid(True)
plt.tight_layout()
plt.show()



# Region Wise Sales Distribution
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct='%1.1f%%'
)

plt.title("Region Wise Sales Distribution")

plt.tight_layout()
plt.show()



# Top 10 States by Sales
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_states.index, top_states.values)

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



# Discount vs Profit
plt.figure(figsize=(8, 5))
plt.scatter(df['Discount'], df['Profit'])

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()




# Ship Mode Distribution
ship_mode_counts = df['Ship Mode'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(ship_mode_counts.index, ship_mode_counts.values)

plt.title("Ship Mode Distribution")
plt.xlabel("Ship Mode")
plt.ylabel("Count")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()



# Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.barh(top_products.index, top_products.values)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.show()



# Yearly Sales Trend
yearly_sales = df.groupby('Order Year')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o')

plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()
plt.show()



# Segment Wise Sales
segment_sales = df.groupby('Segment')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.bar(segment_sales.index, segment_sales.values)

plt.title("Segment Wise Sales")
plt.xlabel("Segment")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()



# Important Insights
print("IMPORTANT INSIGHTS:")

print("1. Highest sales category:")
print(df.groupby('Category')['Sales'].sum().idxmax())

print("\n2. Highest profit category:")
print(df.groupby('Category')['Profit'].sum().idxmax())

print("\n3. Most profitable state:")
print(df.groupby('State')['Profit'].sum().idxmax())

print("\n4. Region with maximum sales:")
print(df.groupby('Region')['Sales'].sum().idxmax())

print("\n5. Product with highest sales:")
print(df.groupby('Product Name')['Sales'].sum().idxmax())

print("\n6. Total Orders:")
print(df['Order ID'].nunique())


top_customers = (
    df.groupby(
        ['Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Region']
    )
    .size()
    .reset_index(name='Total Orders')
    .sort_values(by='Total Orders', ascending=False)
    .head(20)
)
print("\n7. Top 20 Most Frequent Customers:")
print(top_customers.to_string(index=False))

print("ANALYSIS COMPLETED")