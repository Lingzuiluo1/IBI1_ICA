# Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Check current working directory
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())
# Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#1. Show Year and DALYs (columns 3 and 4) for first 10 rows
print("\n=== First 10 rows: Year and DALYs ===")
first_10 = dalys_data.iloc[0:10, [2, 3]]
print(first_10)
#Find the year with maximum DALYs in first 10 years
afg_10 = dalys_data.iloc[0:10]
max_daly = 0
max_year = 0
for i in range(len(afg_10)):
     current_daly = afg_10.iloc[i]["DALYs"]
     current_year = afg_10.iloc[i]["Year"]
     if current_daly > max_daly:
         max_daly = current_daly
         max_year = current_year
print("\nAfghanistan first 10 years:")
print("Year with max DALYs:", max_year)
# Answer: Year with maximum DALYs in Afghanistan's first 10 years: 1998