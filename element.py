import json
import re

with open("lookup.json", "r") as file:
    lookup = json.load(file)

class Element:

    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.required_attributes = []
        self.children = []
        self.string = ""
        self.text = ""

    def init_attributes_dict(self):
        attribute_names = lookup[self.name]["attributes"]
        #print(self.attributes)
        for attr in attribute_names:
            exec(f'''self.attributes[attr] = self.{re.sub("[-*]", "", attr)}_''')


    def __str__(self):
        try:
            #print(self.attributes.keys())
            first_attr = list(self.attributes.keys())[0]
            attr_string = f"{first_attr}='{self.attributes[first_attr]}'"
        except (IndexError):
            attr_string = ""
        for name, value in self.attributes.items():
            if name == first_attr:
                continue
            if value == None:
                continue
            attr_string += f", {name}='{value}'"
        self.string = f"{self.name}"
        return self.string
    
    def __getitem__(self, item):
        if (item not in list(self.attributes.keys())):
            raise KeyError(f"{self.name} has no {item} attribute!")
        else:
            return self.attributes[item]

    def __setitem__(self, item, value):
        if (item not in list(self.attributes.keys())):
            raise KeyError(f"{self.name} has no {item} attribute!")
        else:
            self.attributes[item] = value
            exec(f'''self.{re.sub("[-*]", "", item)}_ = {value}''')

    def add(self, elem):
        self.children.append(elem)
