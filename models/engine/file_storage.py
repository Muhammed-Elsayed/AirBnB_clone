#!/usr/bin/python3
"""Airbnb clone file storage"""
import json


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

    def reload(self):
        """Loads storage dictionary from file"""
        pass
