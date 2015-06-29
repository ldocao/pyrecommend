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

    def __repr__(self):
        return "User("+str(self.id)+")"

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
        #self.tags = Tags() #list of strings
        
        try:
            self.year = int(year)
        except ValueError:
            self.year = "unknown"
            
    

            
    def __repr__(self):
        return "Movie("+str(self.id)+")"
    
    def __str__(self):
        return self.title+" by "+self.producer+" in "+self.year






class Star(object):
    """Casual unit of rating"""

    def __init__(self, maxvalue=5, minvalue=0):
        self.maxvalue = maxvalue
        self.minvalue = minvalue
        self.unit_name = "star"


class Dimensionless(object):
    """Dimensionless unit"""

    def __init__(self):
        self.unit_name = "1"



class Rating(object):
    """Rating of a movie by a given user"""

    def __init__(self, value=None, units=Star()):
        self.value = value
        self.units = units

        if value > self.units.maxvalue:
            raise ValueError("Value is greater than max value in units of "+self.units.unit_name)

        self.normalized_value = (value - self.units.minvalue) / (
            self.units.maxvalue - self.units.minvalue) #rescale rating to [0,1]
                
            
    def __repr__(self):
        return str(round(self.value,1))+"/"+str(self.units.maxvalue)+" "+self.units.unit_name





        

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




class Tag(object):
    """Tag for movie"""


    def __init__(self, name):
        self.name = name



class Tags(object):
    """List of Tags for movie"""

    def __init__(self, list_tags):
        self.names = [tag.name for tag in list_tags]




user0=User("0000","0000")
