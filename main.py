from matplotlib.pyplot import axis
import pandas as pd


#Gathering data
df = pd.read_csv("data.csv")
group_by_date = df.groupby(["Year", "County"])
print(group_by_date.head())