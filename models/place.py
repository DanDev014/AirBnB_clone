#!/usr/bin/python3
"""Place Model module"""

from models import base_model


class Place(base_model.BaseModel):
    """This class defines the Place structure for the projects
    and inherits from BaseModel.

    Atributes:
        city_id (string): the corresponding city id of the place.
        user_id (string): the corresponding user id of the place.
        name (string): the name of the place.
        description: (string): the description of the place.
        number_rooms (int): the number of rooms in the place.
        max_guest (int): the maximal number of guest supported.
        price_by_night (int): the price of one night at the place.
        latitude (float): the latitude of the place.
        longitude (float): the longitude of the place.
        amenity_ids (list): lists of amenity of the place.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class.

        Parameters:
            args (list): not used.
            kwargs (dict): used to assign attribute to the object
        """

        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

        if kwargs is not None and len(kwargs.keys()) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()