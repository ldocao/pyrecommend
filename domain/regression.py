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

    movie_features: list of features
        List of features for a given movie
    

    Return:
    ------
    prediction: Rating list
        Predicted rating of movies by the users in user_affinity.units.
    """


    return [a*f.value for a,f in zip(user_affinity,movie_features)]







def cost_function(user_features, movie_features, training_rating_users):
    """Compute the cost function for a given set of user_features, movie_features and training_rating_users"""





def regularization_term(user_features):
    """Regularization term in the cost function"""

    lambda_reg = 1
    #sum(user_features.value**2)

    return regularization
    



def gradient_descent_update():
    """Perform a gradient descent to minimize the cost function

    Parameters:
    ----------
    

    """

    alpha = 0.1



    return newfeature
