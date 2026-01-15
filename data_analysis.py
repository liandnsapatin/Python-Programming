# Liand Sapatin

import pandas as pd

# Read the csv file into variable
df = pd.read_csv("avatar.csv")

# Display first few rows in the dataframe
print(df.head())

# Put the book_num column into 
avatar_count = df["book_num"]

# Display 