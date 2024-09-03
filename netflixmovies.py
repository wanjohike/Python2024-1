movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},

]

crime = [movie for movie in movies if movie['genre'] == 'Crime']
highly_rated = [movie for movie in movies if movie['rating'] >= 9.0]
print('Crime Movies')
for movie in crime:
    print(f"{movie['title']}: {movie['genre']}")