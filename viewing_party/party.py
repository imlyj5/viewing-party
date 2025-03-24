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
#Jeslyn's:
# def get_watched_avg_rating(user_data):
#     total_score = 0
#     movie_count = 0
#     if not user_data["watched"]:
#         return 0.0
#     for movie in user_data["watched"]:
#         total_score += movie["rating"]
#         movie_count += 1
    
#     return float(total_score/movie_count)

#Jeslyn's
# def get_most_watched_genre(user_data):
#     if not user_data["watched"]:
#         return None
#     #Set the most watched genre as the genre of first movie in the watched list
#     genre_frequency = {}
#     for movie in user_data["watched"]:
#         if movie["genre"] not in genre_frequency:
#             genre_frequency[movie["genre"]] = 1
#         else:
#             genre_frequency[movie["genre"]] += 1
    
#     highest_frequency = 0
#     most_watch_genre = ""
#     for genre, count in genre_frequency.items():
#         if count > highest_frequency:
#             highest_frequency = count
#             most_watch_genre = genre
    
#     return most_watch_genre 

#Jenny's:
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

#Jenny's    
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

#print(get_most_watched_genre(user_data))
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# data_with_friends = {
#         "watched": [{
#             "title": "MOVIE_TITLE_2",
#             "genre": "GENRE_1",
#             "rating": 3
#         },{
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 5
#         }],
#         "friends": [{"watched":[{
#             "title": "MOVIE_TITLE_2",
#             "genre": "GENRE_1",
#             "rating": 3
#         }]},{"watched":[{
#             "title": "MOVIE_TITLE_3",
#             "genre": "GENRE_1",
#             "rating": 3
#         }]}]
#     }

def get_unique_watched(user_data):
    #create cross check dictionary based on the movies watched by user
    #key is movie title, value is list of frequescy (set to 0) at index 0 and movie details at index 1
    cross_check = {}
    for user_movie in user_data["watched"]:
        cross_check[user_movie["title"]] = [0]
        cross_check[user_movie["title"]].append(user_movie)
    #print(f"cross check: {cross_check}")

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["title"] in cross_check:
                cross_check[friend_movie["title"]][0] += 1

    #print(f"cross check: {cross_check}")
    
    unique = []
    for movie, count in cross_check.items():
        if count[0] == 0:
            unique.append(count[1])
    #print(f"unique: {unique}")

    return unique

#get_unique_watched(data_with_friends)   

def get_friends_unique_watched(user_data):
    cross_check = {}
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["title"] in cross_check:
                continue
            else:
                cross_check[friend_movie["title"]] = [0]
                cross_check[friend_movie["title"]].append(friend_movie)
        #print(f"cross check: {cross_check}") 

    for user_movie in user_data["watched"]:
        if user_movie["title"] in cross_check:
            cross_check[user_movie["title"]][0] += 1

    unique = []
    for movie, count in cross_check.items():
        if count[0] == 0:
            unique.append(count[1])
    #print(f"unique: {unique}")
    
    return unique
#get_friends_unique_watched(data_with_friends)   
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
