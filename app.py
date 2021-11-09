import requests
import json
import csv 
from requests.api import request 


if __name__ == '__main__':
    urlMovies = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentType=Movie'
    urlSeries = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentType=Series%20with%20Season'
    responseMovies = requests.get(urlMovies)
    responseSeries = requests.get(urlSeries)
    

    if responseMovies.status_code == 200:
       dataMovie = responseMovies.json()

       
    if responseSeries.status_code == 200:
       dataSeries = responseSeries.json()




moviesWithPlayContents = dataMovie['playContentArray']
movies = moviesWithPlayContents['playContents']
series = dataSeries


## JSON de Peliculas
with open('movies.json', 'w') as f:
    json.dump(movies, f, indent=4)

## JSON de Series

with open('series.json','w') as f:
    json.dump(series, f, indent = 4)

# Cargar la base de datos:

with open('movies.json') as contenidoJSON:
    movies = json.load(contenidoJSON)
    for movie in movies:
        print('title: ', movie.get('title'), ' Year: ', movie.get('releaseYear'))

        


