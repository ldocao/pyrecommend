import uuid
from warnings import warn






def flatten(x):
    """Flatten a list of arbitrary depth"""
        
    try:
        y = iter(x)
    except TypeError:
        warn("x is not an iterable. Returning x.")
        return x
    
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result






class User(object):
    """User identification

    """
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.ID = uuid.uuid4() #generate unique identifier UUID
        #self.dateofbirth = dateofbirth
        self.points = 0 #experience points
        ##add here other caracteristics (country, premium status)

    
    def __repr__(self):
        return "User("+str(self.ID)+")"

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

    def __init__(self, title, producer="unknown", year="unknown"):
        self.title = title
        self.producer = producer
        self.ID = uuid.uuid4() #generate unique identifier UUID
        # self.country
        # self.year

        # self.tags = Tags() #list of strings
        
        try:
            self.year = int(year)
        except ValueError:
            self.year = "unknown"
            
        self.actors = []    
        self.features = [] #list of features
            
    def __repr__(self):
        return "Movie("+str(self.ID)+")"
    
    def __str__(self):
        return self.title+" by "+self.producer+" in "+self.year



    def add(self,*args):
        """Add something to a list

        Parameters:
        ----------

        Notes:
        -----
        You can add several objects, but they must be unpacked
        """

        for count, elem in enumerate(args):
            if isinstance(elem, Feature):
                self.features.append(elem)
            elif isinstance(elem, Actor):
                self.actors.append(elem)
            else:
                raise TypeError("Can't add ")



class Star(object):
    """Casual unit of rating"""

    def __init__(self, maxvalue=5, minvalue=0):
        self.unit_name = "star"
        self.maxvalue = maxvalue
        self.minvalue = minvalue




class UserNormalized(object):
    """Normalize to mean and standard deviation user rating"""

    def __init__(self, mean, sdv):
        self.unit_name = "User_Normalized"
        self.mean = mean
        self.sdv = sdv


class UnityNormalized(object):
    """Normalize to [0,1]"""

    def __init__(self, minvalue, maxvalue):
        self.unit_name = "Unity_Normalized"
        self.maxvalue = maxvalue
        self.minvalue = minvalue

        # try:
       #      self.normalized_value = (value - self.units.minvalue) / (
       #          self.units.maxvalue - self.units.minvalue) #rescale rating to [0,1]
       #  except TypeError:
       #      self.normalized_value = None




        
        
class Rating(object):
    """Rating of a movie by a given user"""

    def __init__(self, value=None, units=Star()):
        self.value = value
        self.units = units


    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Try to sum two objects of different types.")
        return Rating(self.value+other.value, units=self.units)

    __radd__ = __add__


    def __sub__(self,other):
        if type(self) != type(other):
            raise TypeError("Try to sum two objects of different types.")
        return Rating(self.value-other.value, units=self.units)
        
        
    def __mul__(self,scalar):
        return Rating(self.value*scalar, units=self.units)

    __rmul__ = __mul__ #define back multiplication as multiplication

            
    def __repr__(self):
        try:    
            return str(round(self.value,1))+"/"+str(self.units.maxvalue)+" "+self.units.unit_name
        except TypeError:
            return str(None)





        

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


class Feature(object):
    """A feature for a movie"""

    def __init__(self, name, value=0, weight=1):
        self.name = name
        self.value = value
        self.weight = weight
        self.unit = UnityNormalized


    def __repr__(self):
        return "Feature("+self.name+","+str(self.value)+","+str(self.weight)+")"





class Actor(object):
    """An Actor in Movie"""

    def __init__(self,firstname,lastname, sex=None):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex

    def __repr__(self):
        return "Actor("+self.firstname+","+str(self.lastname)+")"





user0=User("0000","0000")
