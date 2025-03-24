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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

