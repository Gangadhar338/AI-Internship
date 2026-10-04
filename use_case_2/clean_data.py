import pandas as pd

# Read CSV
df = pd.read_csv("sample_data.csv")

print("Original Data:")
print(df)

# Clean Age: convert invalid values to missing
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Email
df["Email"] = df["Email"].fillna("unknown@example.com")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data to Excel
df.to_excel("cleaned_data.xlsx", index=False)

print("\nCleaned Data:")
print(df)

print("\nCleaned data successfully saved to cleaned_data.xlsx")
