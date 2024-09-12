from collections import Counter
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},

]

# list comprehension filter for movies based on genre 'Crime'
crime = [movie for movie in movies if movie['genre'] == 'Crime']
drama = [movie for movie in movies if movie['genre'] == 'Drama']
print('Crime Movies')
for movie in crime:
    print(f"{movie['title']}: {movie['genre']}")

# list comprehension filter for movies based on rating threshold lower than 9.0
rating = [movie for movie in movies if movie['rating'] < 9.0]
for movie in rating:
    print(f"{movie['title']}: {movie['rating']}")

sorted_movies = sorted(movies, key=lambda movie: movie['rating'])
print("Movies sored by their rating in desc order")
for movie in sorted_movies:
    print(f"{movie['title']}: {movie['rating']}")

genre_count = [movie['genre'] for movie in movies]
genres = {genre:genre_count.count(genre) for genre in genre_count}

# anther way to get the count of genre
movie_genre = {genre: sum(1 for movie in movies if movie['genre'] == genre) for genre in set(movie['genre'] for movie in movies)}


genresCounts = Counter(movie["genre"] for movie in movies)

# saving to a text file named output
with open('nextfix.txt', 'w') as file:
    file.write('Drama Movies\n')
    for movie in drama:
        file.write(f"{movie['title']}: {movie['genre']}\n")
    
    file.write('\nHighly Rated\n')
    for movie in rating:
        file.write(f"{movie['title']}: {movie['genre']}\n")
    
    file.write("Movies sored by their rating in desc order")
    for movie in sorted_movies:
        file.write(f"{movie['title']}: {movie['rating']}")

    

    