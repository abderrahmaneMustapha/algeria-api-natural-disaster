import pandas as pd

## this repo doesnt contain consolidated_data.csv because of his size (604mb)
## if you want download this file check
## https://www.kaggle.com/danielpe/earthquakes

## extract algerian places only from  consolidated_data.csv with lat and long and depth
df = pd.read_csv("../../dataResources/files/earthquakes/consolidated_data.csv", usecols=[1,2,3,4,14])
df_api = pd.read_csv("../../dataResources/files/earthquakes/algeria_from_api.csv", usecols=[1,2,3,4,14])
df_con = pd.concat([df, df_api])
df_con = df_con.fillna(value="undifined")
df_con = df_con[df_con['place'].str.contains("alge", case=False)]
df_con.to_csv("../../dataResources/files/earthquakes/algeria_consolidated_data.csv")
