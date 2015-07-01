##PURPOSE: minimize cost function to find best estimate for user profile features

import numpy as np
import pdb

# n_movies : number of movies
# n_features : number of features for a movie (eg: genre)

# user_rating : array for a given user of ratings for all movies [n_movies]
# user_has_rated : array for a given user of yes or no for all movies if he has rated [n_movies]
# user_affinity : array for a given user of affinity with a feature of a movie [n_features]
# movie_features : array of components for a given movie [n_feature]

# A feature is dimensionless and normalized [0,1]
# An affinity is in star units





def predicted_rating(user_affinity, movie_features):
    """Predicted rating for users on movies

    Parameters:
    ----------
    user_affinity: list of Rating
        List of affinity for all features in a movie, for a given user.

    movie_features: list of Feature
        List of features for a given movie. Sum of all features must be <= 1
    

    Return:
    ------
    prediction: list of Rating
        Predicted rating of movies by the users in user_affinity.units.
    """

    rating_per_feature = [a*f.value for a,f in zip(user_affinity,movie_features)]
    start = Rating(0,units=rating_per_feature[0].units) #i need to initialize the sum
    return sum(rating_per_feature,start)







def regularization_term(user_affinity, lambda_reg=1.):
    """Regularization term in the cost function


    Parameters:
    ----------
    user_affinity: list of Rating
        List of affinity for all features in a movie, for a given user.

    lambda_reg: float
        Control parameter for regularization.
    """

    regularization = sum([a.value**2 for a in user_affinity])

    return lambda_reg/2.*regularization






def cost_function(user_affinity, movie_features, training_user_rating,
                  lambda_reg=0.):
    """Compute the cost function for a given set of user_affinity, movie_features and training_user_rating

    Parameters:
    ----------
    user_affinity: list of Rating [n_features]
        List of affinity for all features in a movie, for a given user. 

    movie_features: list of Feature [n_features]
        List of features for a given movie

    training_user_rating: Rating 
        Rating from user for the given movie. 

    Return:
    ------
    cost: Float
        Cost for the current parameters. Units are user_affinity.units**2
    """


    cost = (predicted_rating(user_affinity,movie_features) - training_user_rating)
    cost += regularization_term(user_affinity,lambda_reg=lambda_reg) #add regularization term
    
    return cost



    



def gradient_descent_update():
    """Perform a gradient descent to minimize the cost function

    Parameters:
    ----------
    

    """

    alpha = 0.1



    return newfeature
