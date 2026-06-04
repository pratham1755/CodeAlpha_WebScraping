import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_data.csv")

top_books = df.head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top_books["Title"],
    range(len(top_books))
)

plt.xticks(rotation=90)

plt.title("Top 10 Books")

plt.tight_layout()

plt.show()