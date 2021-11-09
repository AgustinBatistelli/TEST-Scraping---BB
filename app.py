import requests
import json 


if __name__ == '__main__':
    url = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentType=Movie'
    response = requests.get(url)
    

    if response.status_code == 200:
       data = response.json()



playContentArray = data['playContentArray']

## JSON de Peliculas
with open('movies.json', 'w') as f:
    moviesJSON = json.dump(playContentArray, f, indent=4)
