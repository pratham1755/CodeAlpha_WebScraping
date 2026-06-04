import pandas as pd

df = pd.read_csv("books_data.csv")

print("Total Books:", len(df))

print("\nFirst Five Books:")
print(df.head())