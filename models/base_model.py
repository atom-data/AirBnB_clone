#!/usr/bin/python3
"""
File: base_model.py
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel definition for AirBnB clone project
    This is the core object from which all objects are derived
    """
    def __init__(self, *args, **kwargs):
        """
        __init__ - initialze BaseModel object
        Args:
            args(tuple) - should have zero arguments (not used)
            kwargs(dict) - if variable exists, then init instance with data
                Note, datetime format is 2020-10-31 21:05:54.119572
        Return:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, v in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    self.__class__.__name__ = v
                else:
                    setattr(self, key, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        __str__ - print method for BaseModel instance
        Args:
            None
        Return:
            None
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save - updates public instance attribute, updated_at, with
            current timestamp
        Args:
            None
        Return:
            None
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        to_dict - return dictionary with copy all key/value pairs of __dict__
        Args:
            None
        Return:
            entire copy of dictionary instance and must stringify some
            JSON modifications
        """
        a = {}
        for key, v in self.__dict__.items():
            if key != 'created_at' and key != 'updated_at':
                a[key] = v
        a['__class__'] = self.__class__.__name__
        a['created_at'] = self.created_at.isoformat()
        a['updated_at'] = self.updated_at.isoformat()
        return a
