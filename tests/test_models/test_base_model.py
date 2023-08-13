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
