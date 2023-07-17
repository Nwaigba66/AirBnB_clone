#!/usr/bin/python3
"""
This module defines the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for other models.
    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date & time the instance was created.
        updated_at (datetime): Date & time instance was last updated.
    """
	def __init__(self, *args, **kwargs):
        	"""
		Initializes a new instance of BaseModel.

		The id is set to a unique identifier generated using UUID.
		The created_at & updated_at attributes are set to current date & time.
        	"""
        	if kwargs:
            		for key, value in kwargs.items():
                		if key == "__class__":
                  			# skip this attribute
                    			continue
                		if key == "created_at" or key == "updated_at":
                    			# convert value from string to datetime object
                    			value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                			# set attribute of object using key & value
                			setattr(self, key, value)
        	else:
            		self.id = str(uuid.uuid4())
            		self.created_at = datetime.now()
            		self.updated_at = self.created_at

            		# save the new instance to storage
            		models.storage.new(self)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

def save(self):
        """
        Updates the updated_at attribute with the current date and time
        & saves it to storage

        This method is called to mark when an instance is updated.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        The dictionary contains all the attributes of the instance,
        including the class name, id, created_at, and updated_at converted
        to ISO 8601 format.

        Returns:
            dict: Dictionary representation of the instance.
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
