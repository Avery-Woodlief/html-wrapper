import json

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

    def init_attributes(self):
        attribute_names = lookup[self.name]["attributes"]
        for attr in attribute_names:
            self.attributes[attr] = None
        self.required_attributes = lookup[self.name]["required"]

    def __str__(self):
        first_attr = list(self.attributes.keys())[0]
        attr_string = f"{first_attr}='{self.attributes[first_attr]}'"
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

    def add(self, elem):
        self.children.append(elem)
