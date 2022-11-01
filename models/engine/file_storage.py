#!/usr/bin/python3
"""class Filestorage"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """class FileStorage that serializes instances to a JSON file and 
    deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}
 
    def all(self):
        """all - returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        new - sets in __objects the obj given
        Args:
            obj(unk) - object to copy into __objects dictionary
        Return:
            None
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        save - serializes __objects to JSON file
        Args:
            None
        Return:
            None
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json_objects = {}
            for key, v in FileStorage.__objects.items():
                json_objects[key] = v.to_dict()
            j = json.dumps(a)
            f.write(j)

    def reload(self):
        """
        reload - deserializes JSON file back to __objects
        Arg:
            None
        Return:
            None
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for v in data.values():
                    my_cl = v["__class__"]
                    my_cl = eval(my_cl)
                    obj = my_cl(**v)
                    self.new(obj)
        except:
            pass
