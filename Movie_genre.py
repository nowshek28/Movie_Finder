import requests

api_key = ''


url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
response = requests.get(url)

if response.status_code == 200:
    genres_data = response.json()
    genres = genres_data.get('genres', [])
    for genre in genres:
        print(f"ID: {genre['id']}, Name: {genre['name']}")
else:
    print(f"Error: {response.status_code}")
