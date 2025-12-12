import pandas as pd

print("===== Pandas CSV Reader & Basic Analysis =====")

print("\nData from CSV\n")
data = pd.read_csv("data.csv")

print("Head:\n", data.head())
print("\nTail:\n", data.tail())
print("\nData Types:\n", data.dtypes)
print("\nShape(rows, columns):", data.shape)

print("\n\nSummary Statistics\n")
print("Column-wise Mean:\n", data.mean(numeric_only=True))
print("\nColumn-wise Median:\n", data.median(numeric_only=True))
print("\nColumn-wise Min:\n", data.min(numeric_only=True))
print("\nColumn-wise Max:\n", data.max(numeric_only=True))
print("\nColumn-wise Count:\n", data.count())

print("\n\nFiltering & Selecting\n")
if len(data.columns) >= 2:
    print("\nSelected Columns (first 2):\n", data.iloc[:, :2])

numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
if len(numeric_cols) > 0:
    col = numeric_cols[0]
    print(f"\nRows where {col} > {data[col].mean():.2f}:\n")
    print(data[data[col] > data[col].mean()])

print("\nFirst 10 rows:\n", data.iloc[:10])
print("\nRows 5 to 15:\n", data.iloc[5:16])

print("\n\nSaving Filtered Results\n")
if len(numeric_cols) > 0:
    filtered = data[data[numeric_cols[0]] > data[numeric_cols[0]].mean()]
else:
    filtered = data.head(10)

filtered.to_csv("filtered_output.csv", index=False)

print("Filtered results saved as 'filtered_output.csv'")