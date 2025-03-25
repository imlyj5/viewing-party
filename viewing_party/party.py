# --------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(title, genre, rating):
    movie = {}
    if title == None or genre == None or rating == None:
        return None
    
    movie["title"] = title
    movie ["genre"] = genre
    movie["rating"] = rating
    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data   

# --------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    if not user_data["watched"]:
        return 0.0
    
    for movie in user_data["watched"]:
        total_rating += movie["rating"]   
    avg_rating = total_rating / len(user_data["watched"])

    return avg_rating


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_frequence = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequence:
            genre_frequence[movie["genre"]] +=1
        else:
            genre_frequence[movie["genre"]] = 1

    max_frequence = max(genre_frequence, key = genre_frequence.get)
    return max_frequence

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movie = []
    friends_movie = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie.add(movie["title"])  
    
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie:
            unique_movie.append(movie)
    return unique_movie
    

def get_friends_unique_watched(user_data):
    user_movie_titles = []
    for movie in user_data["watched"]:
        user_movie_titles.append(movie["title"])

    friends_movie_titles = set()
    unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if title not in user_movie_titles and title not in friends_movie_titles:
                friends_movie_titles.add(title)
                unique_movies.append(movie)

    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    rec_list = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)
    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#Jeslyn's
def get_new_rec_by_genre(user_data):
    rec_list = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            rec_list.append(movie)
    return rec_list

# def get_new_rec_by_genre(user_data):
#     recs_movie = []
#     friends_movie = get_friends_unique_watched(user_data)
#     prefer_genre = get_most_watched_genre(user_data)
#     if not prefer_genre:
#         return []
#     for movie in friends_movie:
#         if movie["genre"] in prefer_genre:
#             recs_movie.append(movie)
#     return recs_movie


#Jeslyn's
def get_rec_from_favorites(user_data):
    rec_list = []
    for movie in get_unique_watched(user_data):
        if movie in user_data["favorites"]:
            rec_list.append(movie)
    return rec_list

# def get_rec_from_favorites(user_data):
#     recs_movie = []
#     user_movies = get_unique_watched(user_data)
#     fav_movie = user_data["favorites"]
#     fav_list = []
#     for movie in fav_movie:
#         fav_list.append(movie["title"])
#     for movie in user_movies:
#         if movie["title"] in fav_list:
#             recs_movie.append(movie)
#     return recs_movie


