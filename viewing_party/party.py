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



# user_data = {
#         "watchlist": [{
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 5
#         }],
#         'watched': [{'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0},
#                     {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, 
#                     {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, 
#                     {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, 
#                     {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, 
#                     {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}]}


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
    # print(friends_movie)
    # print(unique_movie)
    return unique_movie
    
def get_friends_unique_watched(user_data):
    user_movie = set()
    unique_movie = []
    for movie in user_data["watched"]:
        for title in movie["title"]:
            user_movie.add(movie["title"]) 

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie["title"] not in user_movie:
                unique_movie.append(movie)
    
    friend_movie = []
    for movie in unique_movie:
        if movie not in friend_movie:
            friend_movie.append(movie)

    return friend_movie

    

# user_data = {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}], 'friends': [{'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]}, {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]}]}
# print(get_friends_unique_watched(user_data))

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs_movie = []
    friend_movie = get_friends_unique_watched(user_data)
    for movie in friend_movie:
        if movie["host"] in user_data["subscriptions"]:
            recs_movie.append(movie)
    return recs_movie

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recs_movie = []
    friends_movie = get_friends_unique_watched(user_data)
    prefer_genre = get_most_watched_genre(user_data)
    if not prefer_genre:
        return []
    for movie in friends_movie:
        if movie["genre"] in prefer_genre:
            recs_movie.append(movie)
    return recs_movie

def get_rec_from_favorites(user_data):
    recs_movie = []
    user_movies = get_unique_watched(user_data)
    fav_movie = user_data["favorites"]
    fav_list = []
    for movie in fav_movie:
        fav_list.append(movie["title"])
    for movie in user_movies:
        if movie["title"] in fav_list:
            recs_movie.append(movie)
    return recs_movie



# user_data = {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'amazon'}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2, 'host': 'amazon'}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5, 'host': 'disney+'}], 'friends': [{'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'amazon'}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'hulu'}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5, 'host': 'netflix'}]}, {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'hulu'}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2, 'host': 'amazon'}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0, 'host': 'disney+'}]}], 'subscriptions': ['netflix', 'hulu'], 'favorites': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'netflix'}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5, 'host': 'disney+'}]}

# user_data = {'watched': [{'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}], 'friends': [{'watched': []}, {'watched': []}]}
# print(get_new_rec_by_genre(user_data))