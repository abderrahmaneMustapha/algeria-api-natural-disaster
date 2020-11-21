# Algeria API (Natural disaster)

this repository is an external dependency of the [Algerian Api](https://github.com/Fcmam5/algeria-api) ,  provide a structured JSON and XML data that can be found in [WialyaNaturalDisasterList.json](/data/WialyaNaturalDisasterList.json) and [WialyaNaturalDisasterList.xml](/data/WialyaNaturalDisasterList.xml)

## Meta

### Resources

 A list of resources that we are using to get Data :

#### earthquakes

- [catnat]( https://www.catnat.net/donneesstats/bd-catnat)

- [volcanodiscovery.com](https://www.volcanodiscovery.com/earthquakes/algeria/archive/2011-may-.html)

- [recherche catalogue](/utils/dataResources/files/recherche_catalogue_0_1602169384.csv)

- [kaggle data set (608 mb)](https://www.kaggle.com/danielpe/earthquakes)

- [earthquake usgs api](https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=20100907&latitude=28&longitude=2.&maxradius=50)

#### floods

- nothing to see here yet

[click here](/utils/dataResources/files/more.md)  to see more data resources that i haven't check yet, feel free to add  more resources, or review existing resources

### Code
 - [datafromapi.py](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/code/earthquakes/datafromapi.py) : <br>
 to get data from  earthquake.usgs.gov
 - [datafromcsv.py](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/code/earthquakes/datafromcsv.py) : <br>
  to manipulate data in csv files in [here](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/tree/main/utils/dataResources/files/earthquakes)
 - [webscraper.py](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/code/earthquakes/webscraper.py) : <br> 
 scrape data from  websites in [here](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/dataResources/files/more.md)
### Data
 - [algeria_from_api](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/dataResources/files/earthquakes/algeria_from_api.csv) : <br>
 cotains data fetched from earthquake.usgs.gov  doesn't contain a exact_place row
- [algeria_consolidated_data.csv](https://github.com/abderrahmaneMustapha/algeria-api-natural-disaster/blob/main/utils/dataResources/files/earthquakes/algeria_consolidated_data.csv) : <br>
final  earthquakes results 

## License

Copyright (c) 2020  Licensed under the MIT license.
