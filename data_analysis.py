# Liand Sapatin

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into variable
df = pd.read_csv("avatar.csv")

# Display first few rows in the dataframe
print(df.head())

# Put the book_num column into a variable
avatar_count = df["book_num"]

# Display largest year count
# Print (year_count.max())

largest_year_count = df [df['book_num'] == df ['book_num'].max()]
print("Largest year o")