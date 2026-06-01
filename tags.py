from element import Element, lookup

tags_file = ''''''


for element, stuff in lookup.items():
    code_block = f'''class {element[0].upper() + element[1:]} (Element):
    def __init__(self):
        super().__init__("{element}")
        self.init_attributes()'''
    tags_file += code_block + "\n\n"


exec(tags_file)
