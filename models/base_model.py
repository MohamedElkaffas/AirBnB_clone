#!/usr/bin/python3
"""BaseModel class"""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """BaseModel class that defines all common attributes/methods for others"""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict):  pair of attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """print with this format:[<class name>] (<self.id>) <self.__dict__>"""
        return f'[{self.__class__.name}], ({self.id}), {self.__dict__}'
    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.update_at = datetime.today()
        models.storge.save()

    def to_dict(self):
        """a dic containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
