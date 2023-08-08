#!/usr/bin/python3
import json
import models
""" storing and reloading objects in json file """


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    """ dictionary for object"""
    def all(self):
        return FileStorage.__objects

    """ adding a new object inside the dictionary of objects """
    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    """ saves objects inside a json file """
    def save(self):
        objects = {}
        for k, v in FileStorage.__objects.items():
            objects[k] = v.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(objects))

    """ reloads dictionary from a json file """
    def reload(self):
        dct = {'BaseModel': models.BaseModel}
        try:
            with open(FileStorage.__file_path, "r") as f:
                dic = json.loads(f.read())
                for k, v in dic.items():
                    obj = dct[v["__class__"]](**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
