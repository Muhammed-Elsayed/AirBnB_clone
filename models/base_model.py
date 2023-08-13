#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from uuid import uuid4


"""python base_model module used as a parent class for the comming classed"""


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)



    """represinting the object in the form of str"""
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    """should be called when any change occured to the obj """
    def save(self):
        self.updated_at = datetime.now()

    """updating __dict__"""
    def to_dict(self):
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = self.__class__.__name__

        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()

        return copy_dict
