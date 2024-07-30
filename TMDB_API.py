import requests

api_key = ''
movie_id = 550  # Example movie ID for "Fight Club"

url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
response = requests.get(url)

if response.status_code == 200:
    movie_data = response.json()
    genres = movie_data.get('genres', [])
    genre_names = [genre['name'] for genre in genres]
    print(f"Title: {movie_data['title']}")
    print(f"Genres: {', '.join(genre_names)}")
else:
    print(f"Error: {response.status_code}")
