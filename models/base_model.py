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
	created_at (datetime): Date & time when the instance was created.
	updated_at (datetime): Date & time when the instance was last updated.
	 """
	def __init__(self):
        	self.id = str(uuid.uuid4())
        	self.created_at = self.updated_at = datetime.now()

	def __str__(self):
         	"""
        	Returns a string representation of the BaseModel instance.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) ({self.dict})"
	
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
        	result["__class__"] = self.__class__.__name_
        	result["created_at"] = self.created_at.isoformat()
        	result["updated_at"] = self.updated_at.isoformat()
		return result

