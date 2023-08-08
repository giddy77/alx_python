"""here the class base is defined"""
class Base:
    """the private attribute is defined"""
    __nb_objects = 0
    
    
    def __init__(self, id=None):
        """the constructor is defined"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects