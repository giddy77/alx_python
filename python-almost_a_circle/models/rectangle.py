class Base:
    """Base class for project"""
    nb_objects = 0

    def init(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.__nb_objects