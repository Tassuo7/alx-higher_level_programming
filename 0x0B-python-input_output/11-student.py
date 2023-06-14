#!/usr/bin/python3
""" a class Student that defines a student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and all([type(nr) == str for nr in attrs])):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, val in json.items():
            setattr(self, k, val)
