#!/usr/bin/python3
"""test cases for the base_module module"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel





class Test_constructor(unittest.TestCase):
    
    def test_consturctor_with_no_kwargs(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_kwargs_constructor(self):
            
        data = {
            'id': 'some_id',
            'created_at': '2023-08-13T12:34:56.789',
            'updated_at': '2023-08-13T12:34:56.789',
            'name': 'Test Model'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, 'some_id')
        self.assertEqual(obj.name, 'Test Model')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        



class TestBaseModel_str_method(unittest.TestCase):
    
    def first_test(self):
        obj = BaseModel()
        obj.id = 1

        string = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), string)



class TestBaseModel(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    base = BaseModel()
    base.name = "My First Model"
    base.my_number = 89

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.name, "My First Model")
        self.assertEqual(self.base.my_number, 89)

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_base_json = self.base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 89)
        self.assertNotEqual(new_base, self.base)
        self.assertDictEqual(new_base.__dict__, self.base.__dict__)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.base.to_dict()
        expected_dic = self.base.__dict__.copy()
        expected_dic["__class__"] = self.base.__class__.__name__
        expected_dic["updated_at"] = self.base.updated_at.isoformat()
        expected_dic["created_at"] = self.base.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.base.updated_at
        self.base.my_number = 90
        self.base.save()
        after_update_time = self.base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        # all_objects = storage.all()
        # new_number = all_objects[self.base.__class__.__name__ +
        #                          "." + self.base.id]["my_number"]
        # self.assertEqual(new_number, 90)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.base.__class__.__name__
        expected_str = f"[{n}] ({self.base.id}) <{self.base.__dict__}>"
        self.assertEqual(self.base.__str__(), expected_str)