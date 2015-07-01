##PURPOSE: create a fake database to test algorithm
import sys
import os
sys.path.append("/Users/ldocao/Documents/Professionnel/Data Science/S2DS/Utelly/pyrecommend/domain/")
import atoms as at
import numpy as np
import regression as reg

user1 = at.User("Alfred", "Dupont")
user2 = at.User("Bob", "Dupont")
list_users = [user1, user2]
n_users = len(list_users)


movieA = at.Movie("Love1")
movieB = at.Movie("Love2")
movieC = at.Movie("Action1")
movieD = at.Movie("Action2")
list_movies = [movieA, movieB, movieC, movieD]
n_movies = len(list_movies)



##given some features
romanceA = at.Feature("romance", value=1)
romanceB = at.Feature("romance", value=0.9)
romanceC = at.Feature("romance", value=0.4)
romanceD = at.Feature("romance", value=0)
romance = [romanceA, romanceB, romanceC, romanceD]

actionA = at.Feature("action", value=0)
actionB = at.Feature("action", value=0.1)
actionC = at.Feature("action", value=0.3)
actionD = at.Feature("action", value=0.99)
action = [actionA, actionB, actionC, actionD]

adventureA = at.Feature("adventure", value=0)
adventureB = at.Feature("adventure", value=0.)
adventureC = at.Feature("adventure", value=0.3)
adventureD = at.Feature("adventure", value=0.01)
adventure = [adventureA, adventureB, adventureC, adventureD]

features = [romance, action, adventure]
features = np.array(features).T.tolist() #transpose features


rating1 = [at.Rating(5),at.Rating(0),at.Rating(2),at.Rating(1)]
rating2 = [at.Rating(0),at.Rating(0.5),at.Rating(5),at.Rating(4)]

ratings = [rating1, rating2]






##initialization guess
affinity1 = [at.Rating(3),at.Rating(2),at.Rating(1)]
affinity2 = [at.Rating(0.2),at.Rating(4),at.Rating(4.5)]
affinity = [affinity1, affinity2]
result = reg.cost_function(affinity, features, ratings)



