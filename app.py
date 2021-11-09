import requests
import json
from requests.api import request 
import pymysql




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

#conexion db
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'starz123',
    db ='starz'
)

cursor = connection.cursor()

def armarLink(s,id):
    sacarEspacios = s.replace(' ', '-')
    link = 'www.starz.com/ar/es/movies/' + sacarEspacios +'-' +str(id)
    return link


with open('movies.json') as contenidoJSON:
    movies = json.load(contenidoJSON)
    for movie in movies:
        link = armarLink(movie.get('title'), movie.get('contentId'))
        cursor.execute(
                         "INSERT INTO pelicula(id, titulo, anio, sinopsis, duracion,link) VALUES(%s, %s, %s, %s,%s,%s)",  (movie.get('contentId'),
                                    movie.get('title'),
                                    movie.get('releaseYear'), 
                                    movie.get('logLine'),
                                    movie.get('runtime'),
                                    link))
        connection.commit()
        

    
 

 


