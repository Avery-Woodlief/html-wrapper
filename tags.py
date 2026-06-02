# This file only generates the code blocks for each of the tags classes

from element import Element, lookup
import re

tags_file = '''from element import Element, lookup\n'''
tags_file += "# classes for the supported html elements\n\n"


for element, _____ in lookup.items():
    elem_attributes = lookup[element]["attributes"]
    formatted_strings = {}
    for i in range(len(elem_attributes)):
        formatted_string = re.sub("[-*]", "", elem_attributes[i])
        formatted_strings[elem_attributes[i]] = formatted_string
    #print(formatted_strings)
    
    attr_params = f"{formatted_strings[elem_attributes[0]]}_=None"
    for i in range(1, len(elem_attributes)):
        attr_params += f", {formatted_strings[elem_attributes[i]]}_=None"

    init_vars = f"self.{formatted_strings[elem_attributes[0]]}_={formatted_strings[elem_attributes[0]]}_\n        "
    for i in range(1, len(elem_attributes)):
        init_vars += f"self.{formatted_strings[elem_attributes[i]]}_={formatted_strings[elem_attributes[i]]}_\n        "

    code_block = f'''class {element[0].upper() + element[1:]} (Element):
    def __init__(self, {attr_params}):
        super().__init__("{element}")
        self.required_attributes = lookup[self.name]["required"]
        {init_vars}
        self.init_attributes_dict()'''
    tags_file += code_block + "\n\n"


#exec(tags_file)

with open("tags_generated_classes.py", "w") as file:
    file.write(tags_file)

file.close()
