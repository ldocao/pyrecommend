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


movie1 = at.Movie("Love1")
movie2 = at.Movie("Love2")
movie3 = at.Movie("Action1")
movie4 = at.Movie("Action2")
movie5 = at.Movie("Bizarre")
list_movies = [movie1, movie2, movie3, movie4, movie5]
n_movies = len(list_movies)


rating1 = [at.Rating(5),at.Rating(5),at.Rating(0),at.Rating(0),at.Rating(3)]
rating2 = [at.Rating(4.5),at.Rating(4),at.Rating(0.5),at.Rating(1),at.Rating(2)]
rating3 = [at.Rating(0.5),at.Rating(1),at.Rating(5),at.Rating(4.5),at.Rating(1)]
rating4 = [at.Rating(0.5),at.Rating(1),at.Rating(4),at.Rating(3.5),at.Rating(5)]

list_ratings = [rating1, rating2, rating3, rating4]

data = {}
i=0
for user in list_users:
    j=0
    for movie in list_movies:
        data[tuple([user,movie])]=list_ratings[i][j]
        print i,j,data[tuple([user,movie])] 
        j+=1
    i+=1
