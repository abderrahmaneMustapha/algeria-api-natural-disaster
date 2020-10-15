import requests
import pandas as pd
import io

query = "starttime=2019-03-29T21:47:56.920Z"

response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&{}&latitude=36.72&longitude=3.08&maxradius=60".format(query))
data =  response.content
print(response.status_code)

df = pd.read_csv(io.BytesIO(data), encoding='utf8')
df  = df.fillna(value="undifined")
df = df[df['place'].str.contains("alge", case=False)]
df.to_csv("../../dataResources/files/earthquakes/algeria_from_api.csv")

