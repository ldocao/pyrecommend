##PURPOSE: create a fake database to test algorithm
import sys
import os
sys.path.append("/Users/ldocao/Documents/Professionnel/Data Science/S2DS/Utelly/pyrecommend/domain/")
import atoms as at



user1 = at.User("Alfred", "Dupont")
user2 = at.User("Bob", "Dupont")
user3 = at.User("Charles", "Dupont")
user4 = at.User("David", "Dupont")
list_users = [user1, user2, user3, user4]
n_users = len(list_users)


movie1 = at.Movie("Dinosaurs")
movie2 = at.Movie("Interstellar")
movie3 = at.Movie("Vice Versa")
movie4 = at.Movie("Barcelona")
movie5 = at.Movie("Sex on the city")
list_movies = [movie1, movie2, movie3, movie4, movie5]
n_movies = len(list_movies)


data = {}
for user in list_users:
    for movie in list_movies:
        data[[user,movie]]=1
