from tags import *
import json

def expand_(root):
    return {f"{child['id']}" : [child.attributes, child.text, expand_(child)] for child in root.children}

class Document:

    def __init__(self, name):
        self.children = []
        self.name = name
        self.tree = {}
    def add(self, elem):
        self.children.append(elem)

    def expand(self):
        return expand_(self)

    def upload(self):
        self.tree = self.expand()
        with open(f"{self.name}_document_tree.json", "w") as file:
            json.dump(self.tree, file, indent=4)



def example1():
    doc = Document("example1")

    a1 = A()
    a1["href"] = "#1"
    a1['id']='a1'
    a2 = A()
    a2["href"] = "#2"
    a2["id"] = "a2"

    p = P()
    p["title"] = "short sentence"
    p.text = "This is a demo for p tag"
    p["id"] = "p1"
    a1.add(p)


    doc.add(a1)
    doc.add(a2)

    #print(doc.expand())
    doc.upload()
