import uuid



class IDIsReadOnly(type):
    """Metaclass to prevent the alteration of ID class attribute"""
    
    def __setattr__(cls, name, value):
        raise ValueError(name)


    

class User(object):
    """User identification

    """
    
    __metaclass__ = IDIsReadOnly

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = uuid.uuid4() #generate unique identifier UUID
        self.points = 0 #experience points
        ##add here other caracteristics (country, premium status)



    def add_points(self, additional_points):
        """Add points to his counter
        """
        
        self.points += additional_points




# class Friend(User):
#     """Friend of a user"""

#     def __init__(self):
        


class Movie(object):
    """Movie identification
    """

    __metaclass__ = IDIsReadOnly

    
    def __init__(self, title, producer="unknown", year="unknown"):
        self.title = title
        self.producer = producer
        self.id = uuid.uuid4() #generate unique identifier UUID
        self.tags = [] #list of strings
        
        try:
            self.year = int(year)
        except ValueError:
            self.year = "unknown"
            

    def __repr__(self):
        return "Movie()"
    
    def __str__(self):
        return self.title+" by "+self.producer+" in "+self.year






class Star(object):
    """Casual unit of rating"""

    def __init__(self, maxvalue=5, minvalue=0):
        self.maxvalue = maxvalue
        self.minvalue = minvalue
        self.unit_name = "star"


class Unity(object):
    """Unit normalized to 1"""

    def __init__(self):
        self.unit_name = "unity"



class Rating(object):
    """Rating of a movie by a given user"""

    def __init__(self, movie_id, user_id, value=0):
        self.value = value
        self.units = Star()
        self.normalized_value = (value - self.units.minvalue) / (
            self.units.maxvalue - self.units.minvalue) #rescale rating to [0,1]
        

    def __str__(self):
        return str(self.value)+"/"+str(self.units.maxvalue)


        

class Cluster(object):
    """Group of movies"""

    def __init__(self):
        self.name = "unknown"
        self.id = 0 #group id
        self.members = [] #id of movie members


    ##define containing



class Score(object):
    """Score of an unseen movie for a given user"""


    def __init__(self):
        self.value = 0
        self.units = Dimensionless()
