import pandas as pd
from geopy.geocoders import Nominatim
import re
import time

class DataFromCsv():
    
    #concatenate the two csv files
    def concat(self):
        ## this repo doesnt contain consolidated_data.csv because of his size (604mb)
        ## if you want download this file check
        ## https://www.kaggle.com/danielpe/earthquakes

        ## extract algerian places only from  consolidated_data.csv with lat and long and depth

        #read consolidated_data.csv (contains data from 1970 to 2019)
        df = pd.read_csv("../../dataResources/files/earthquakes/consolidated_data.csv", usecols=[1,2,3,4,14])

        #read the data fetched from api contains earthquakes from 2019 to 2020
        df_api = pd.read_csv("../../dataResources/files/earthquakes/algeria_from_api.csv", usecols=[1,2,3,4,14])

        # concat the first and the secend dataset
        df_con = pd.concat([df, df_api])
        #replace Nan and na with undifined
        df_con = df_con.fillna(value="undifined")

        #get algeria data only
        df_con = df_con[df_con['place'].str.contains("alge", case=False)]

        # a list of  exact location(city or wilaya) that we are going to extract 
        # by passing the lang and lat to geopy 
        locations =[]



        #loop trough dataset 


        for i in df_con.iloc[:, 1:3].values:
            try :
                geolocator = Nominatim(user_agent="algeria-api")
                location = geolocator.reverse("{}, {}".format(i[0], i[1]))
                time.sleep(3.4)
            except:
                print("Nominatim conecction exception")
                locations.append("algeria")
                continue

            try : 
                print(location.raw["address"]['state'])
                locations.append(location.raw["address"]['state'])
                

            except :
                
                time.sleep(10)
                locations.append("algeria")
            


        df_con['place_exact'] =  pd.Series( locations).values


        print(df.head)
        df_con.to_csv("../../dataResources/files/earthquakes/algeria_consolidated_data.csv")

    #separating languages
    def separateLang(self):
        french_lang_list  =[]
        arbic_lang_list = []
        df = pd.read_csv("../../dataResources/files/earthquakes/algeria_consolidated_data.csv", usecols=[6])
        for d in df.iloc[:,].values:          
            french_lang_list.append(re.split(r"[^A-Za-zÀ-ÿ\u00C0-\u017F'\s]", d[0])[0])
            arbic_lang_list.append(re.split(r"[^\u0621-\u064A\s]",  d[0])[-1])
        
        df['exact_place_ar'] = pd.Series(arbic_lang_list).values
        df['exact_place_fr'] = pd.Series(french_lang_list).values

        print(df.head)
        df.to_csv("../../dataResources/files/earthquakes/algeria_consolidated_data.csv")
            

        

d =  DataFromCsv()
d.separateLang()