import pandas as pd

## this repo doesnt contain consolidated_data.csv because of his size (604mb)
## if you want download this file check
## https://www.kaggle.com/danielpe/earthquakes

## extract algerian places only from  consolidated_data.csv with lat and long and depth
df = pd.read_csv("../dataResources/files/consolidated_data.csv", usecols=[2,3,4,14])
df  = df.fillna(value="undifined")
df = df[df['place'].str.contains("alger", case=False)]
df.to_csv("../dataResources/files/algeria_consolidated_data.csv")
