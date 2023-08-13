#!/usr/bin/python3
"""Airbnb clone file storage"""
import json
from models.base_model import BaseModel
<<<<<<< HEAD
from models import storage

=======
from models.user import User
>>>>>>> ee9570739bff23c61dca0767b591b440c8209e8e
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}  # contains normal objects

    def all(self):
        """returns all the dictionary objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_objects = {}

        for key, obj in self.__objects.items():
            dict_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dict_objects, f)  # convert dict into json

    """I will edit this later, Its just for now"""
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
