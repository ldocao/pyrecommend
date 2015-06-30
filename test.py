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



##given some features
romance1 = at.Feature("romance", value=4)
action1 = at.Feature("action", value=0.5)
horror1 = at.Feature("horror", value=0)

romance2 = at.Feature("romance", value=4.9)
action2 = at.Feature("action", value=0.5)
horror2 = at.Feature("horror", value=3)

romance3 = at.Feature("romance", value=0)
action3 = at.Feature("action", value=5)
horror3 = at.Feature("horror", value=1)

romance4 = at.Feature("romance", value=0.5)
action4 = at.Feature("action", value=4.5)
horror4 = at.Feature("horror", value=0.2)

romance5 = at.Feature("romance", value=2)
action5 = at.Feature("action", value=1.5)
horror5 = at.Feature("horror", value=3)


silverster_stallone = at.Actor("Silvester","Stallone")

movie1.add(romance1,action1,horror1,silverster_stallone)
movie2.add(romance2,action2,horror2,silverster_stallone)
movie3.add(romance3,action3,horror3,silverster_stallone)
movie4.add(romance4,action4,horror4,silverster_stallone)
movie5.add(romance5,action5,horror5,silverster_stallone)








# rating1 = [at.Rating(5),at.Rating(5),at.Rating(0),at.Rating(0),at.Rating(3)]
# rating2 = [at.Rating(4.5),at.Rating(4),at.Rating(),at.Rating(1),at.Rating(2)]
# rating3 = [at.Rating(0.5),at.Rating(1),at.Rating(5),at.Rating(4.5),at.Rating()]
# rating4 = [at.Rating(),at.Rating(1),at.Rating(4),at.Rating(3.5),at.Rating(5)]

# list_ratings = [rating1, rating2, rating3, rating4]

# data = {}
# i=0
# for user in list_users:
#     j=0
#     for movie in list_movies:
#         data[tuple([user,movie])]=list_ratings[i][j]
#         print i,j,data[tuple([user,movie])] 
#         j+=1
#     i+=1

