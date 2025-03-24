# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title == None or genre == None or rating == None:
        return None
    
    movie["title"] = title
    movie ["genre"] = genre
    movie["rating"] = rating

    
    return movie

def add_to_watched(user_data, movie):
    print(f"user data: {user_data}")
    print(movie)
    user_data["watched"].append(movie)
    print(f"watched: {user_data["watched"]}")
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #print(user_data["watchlist"][0]["title"])
    for movie in user_data["watchlist"]:
        print(f"movie title: {movie["title"]}") 
        print(f"title: {title}") 
        if title == movie["title"]:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    print(f"updated watchlist: {user_data["watchlist"]}") 
    print(f"updated watched: {user_data["watched"]}") 
    return user_data

# janes_data = {
#         "watchlist": [{
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 5
#         }],
#         "watched": []
#     }
# movie = {
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 5
#         }
# watch_movie(janes_data, "MOVIE_TITLE_1")
# add_to_watched(janes_data, movie)
    
# --------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
        # print (movie["rating"])
        total_rating += movie["rating"]   
        # print(total_rating)
    avg_rating = total_rating / len(user_data["watched"])
    return avg_rating
    
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_frequence = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequence:
            genre_frequence[movie["genre"]] +=1
            # print(genre_frequence)
        else:
            genre_frequence[movie["genre"]] = 1
    max_frequence = max(genre_frequence, key = genre_frequence.get)
    # print(genre_frequence)

    return max_frequence



user_data = {
        "watchlist": [{
            "title": "MOVIE_TITLE_1",
            "genre": "GENRE_1",
            "rating": 5
        }],
        'watched': [{'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0},
                    {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, 
                    {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, 
                    {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, 
                    {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, 
                    {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}]}

print(get_most_watched_genre(user_data))
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

