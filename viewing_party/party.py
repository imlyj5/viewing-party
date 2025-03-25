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
    
    genre_frequency = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequency:
            genre_frequency[movie["genre"]] +=1
        else:
            genre_frequency[movie["genre"]] = 1

    most_watched_genre = max(genre_frequency, key = genre_frequency.get)
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movie = []
    friends_movie = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie.add(movie["title"])  #add friend's movie titles to set to remove duplicate
    
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie:
            unique_movie.append(movie)
    return unique_movie
    

def get_friends_unique_watched(user_data):
    user_movie_titles = []
    for movie in user_data["watched"]:
        user_movie_titles.append(movie["title"])  #add user's movie titles to list

    friends_movie_titles = set()  #use set to store friend's movie titles to remove duplicate movie titles
    unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            #if the title not in user_movie_titles and not exist in friends_movie_titles
            if movie["title"] not in user_movie_titles and movie["title"] not in friends_movie_titles: 
                friends_movie_titles.add(movie["title"])  #add this title to friends_movie_titles
                unique_movies.append(movie)  #confirm this movie is friends_unique_watched

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
def get_new_rec_by_genre(user_data):
    rec_list = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            rec_list.append(movie)
    return rec_list


def get_rec_from_favorites(user_data):
    rec_list = []
    for movie in get_unique_watched(user_data):
        if movie in user_data["favorites"]:
            rec_list.append(movie)
    return rec_list



