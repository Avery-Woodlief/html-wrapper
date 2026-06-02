from element import Element, lookup
# classes for the supported html elements

class Html (Element):
    def __init__(self, lang_=None):
        super().__init__("html")
        self.required_attributes = lookup[self.name]["required"]
        self.lang_=lang_
        
        self.init_attributes_dict()

class Meta (Element):
    def __init__(self, charset_=None, name_=None, content_=None):
        super().__init__("meta")
        self.required_attributes = lookup[self.name]["required"]
        self.charset_=charset_
        self.name_=name_
        self.content_=content_
        
        self.init_attributes_dict()

class Link (Element):
    def __init__(self, rel_=None, href_=None, type_=None):
        super().__init__("link")
        self.required_attributes = lookup[self.name]["required"]
        self.rel_=rel_
        self.href_=href_
        self.type_=type_
        
        self.init_attributes_dict()

class Script (Element):
    def __init__(self, src_=None, type_=None, defer_=None, async_=None):
        super().__init__("script")
        self.required_attributes = lookup[self.name]["required"]
        self.src_=src_
        self.type_=type_
        self.defer_=defer_
        self.async_=async_
        
        self.init_attributes_dict()

class A (Element):
    def __init__(self, href_=None, target_=None, rel_=None, download_=None, title_=None, class_=None, id_=None):
        super().__init__("a")
        self.required_attributes = lookup[self.name]["required"]
        self.href_=href_
        self.target_=target_
        self.rel_=rel_
        self.download_=download_
        self.title_=title_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Img (Element):
    def __init__(self, src_=None, alt_=None, width_=None, height_=None, loading_=None, class_=None, id_=None):
        super().__init__("img")
        self.required_attributes = lookup[self.name]["required"]
        self.src_=src_
        self.alt_=alt_
        self.width_=width_
        self.height_=height_
        self.loading_=loading_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Form (Element):
    def __init__(self, action_=None, method_=None, autocomplete_=None, class_=None, id_=None):
        super().__init__("form")
        self.required_attributes = lookup[self.name]["required"]
        self.action_=action_
        self.method_=method_
        self.autocomplete_=autocomplete_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Input (Element):
    def __init__(self, type_=None, name_=None, id_=None, value_=None, placeholder_=None, required_=None, checked_=None, min_=None, max_=None):
        super().__init__("input")
        self.required_attributes = lookup[self.name]["required"]
        self.type_=type_
        self.name_=name_
        self.id_=id_
        self.value_=value_
        self.placeholder_=placeholder_
        self.required_=required_
        self.checked_=checked_
        self.min_=min_
        self.max_=max_
        
        self.init_attributes_dict()

class Button (Element):
    def __init__(self, type_=None, disabled_=None, name_=None, value_=None, class_=None, id_=None):
        super().__init__("button")
        self.required_attributes = lookup[self.name]["required"]
        self.type_=type_
        self.disabled_=disabled_
        self.name_=name_
        self.value_=value_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Label (Element):
    def __init__(self, for_=None, class_=None, id_=None):
        super().__init__("label")
        self.required_attributes = lookup[self.name]["required"]
        self.for_=for_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Textarea (Element):
    def __init__(self, rows_=None, cols_=None, placeholder_=None, maxlength_=None, class_=None, id_=None):
        super().__init__("textarea")
        self.required_attributes = lookup[self.name]["required"]
        self.rows_=rows_
        self.cols_=cols_
        self.placeholder_=placeholder_
        self.maxlength_=maxlength_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Select (Element):
    def __init__(self, name_=None, multiple_=None, required_=None, class_=None, id_=None):
        super().__init__("select")
        self.required_attributes = lookup[self.name]["required"]
        self.name_=name_
        self.multiple_=multiple_
        self.required_=required_
        self.class_=class_
        self.id_=id_
        
        self.init_attributes_dict()

class Option (Element):
    def __init__(self, value_=None, selected_=None, disabled_=None):
        super().__init__("option")
        self.required_attributes = lookup[self.name]["required"]
        self.value_=value_
        self.selected_=selected_
        self.disabled_=disabled_
        
        self.init_attributes_dict()

class Iframe (Element):
    def __init__(self, src_=None, width_=None, height_=None, allowfullscreen_=None, loading_=None):
        super().__init__("iframe")
        self.required_attributes = lookup[self.name]["required"]
        self.src_=src_
        self.width_=width_
        self.height_=height_
        self.allowfullscreen_=allowfullscreen_
        self.loading_=loading_
        
        self.init_attributes_dict()

class Audio (Element):
    def __init__(self, src_=None, controls_=None, autoplay_=None, loop_=None, muted_=None):
        super().__init__("audio")
        self.required_attributes = lookup[self.name]["required"]
        self.src_=src_
        self.controls_=controls_
        self.autoplay_=autoplay_
        self.loop_=loop_
        self.muted_=muted_
        
        self.init_attributes_dict()

class Video (Element):
    def __init__(self, src_=None, controls_=None, autoplay_=None, loop_=None, muted_=None, width_=None, height_=None):
        super().__init__("video")
        self.required_attributes = lookup[self.name]["required"]
        self.src_=src_
        self.controls_=controls_
        self.autoplay_=autoplay_
        self.loop_=loop_
        self.muted_=muted_
        self.width_=width_
        self.height_=height_
        
        self.init_attributes_dict()

class Div (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None, hidden_=None, data_=None):
        super().__init__("div")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        self.hidden_=hidden_
        self.data_=data_
        
        self.init_attributes_dict()

class Header (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("header")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Nav (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("nav")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Main (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("main")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Section (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("section")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Article (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("article")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Footer (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("footer")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class P (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("p")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class Span (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("span")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H1 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h1")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H2 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h2")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H3 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h3")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H4 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h4")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H5 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h5")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

class H6 (Element):
    def __init__(self, id_=None, class_=None, style_=None, title_=None):
        super().__init__("h6")
        self.required_attributes = lookup[self.name]["required"]
        self.id_=id_
        self.class_=class_
        self.style_=style_
        self.title_=title_
        
        self.init_attributes_dict()

