import json

lookup = {}

lookup["html"] = {
    "attributes": ["lang"],
    "required": []
}

lookup["meta"] = {
    "attributes": ["charset", "name", "content"],
    "required": []
}

lookup["link"] = {
    "attributes": ["rel", "href", "type"],
    "required": ["rel", "href"]
}

lookup["script"] = {
    "attributes": ["src", "type", "defer", "async"],
    "required": []
}

lookup["a"] = {
    "attributes": ["href", "target", "rel", "download", "title", "class", "id"],
    "required": ["href"]
}

lookup["img"] = {
    "attributes": ["src", "alt", "width", "height", "loading", "class", "id"],
    "required": ["src", "alt"]
}

lookup["form"] = {
    "attributes": ["action", "method", "autocomplete", "class", "id"],
    "required": []
}

lookup["input"] = {
    "attributes": [
        "type",
        "name",
        "id",
        "value",
        "placeholder",
        "required",
        "checked",
        "min",
        "max"
    ],
    "required": []
}

lookup["button"] = {
    "attributes": ["type", "disabled", "name", "value", "class", "id"],
    "required": []
}

lookup["label"] = {
    "attributes": ["for", "class", "id"],
    "required": []
}

lookup["textarea"] = {
    "attributes": ["rows", "cols", "placeholder", "maxlength", "class", "id"],
    "required": []
}

lookup["select"] = {
    "attributes": ["name", "multiple", "required", "class", "id"],
    "required": []
}

lookup["option"] = {
    "attributes": ["value", "selected", "disabled"],
    "required": []
}

lookup["iframe"] = {
    "attributes": ["src", "width", "height", "allowfullscreen", "loading"],
    "required": ["src"]
}

lookup["audio"] = {
    "attributes": ["src", "controls", "autoplay", "loop", "muted"],
    "required": []
}

lookup["video"] = {
    "attributes": [
        "src",
        "controls",
        "autoplay",
        "loop",
        "muted",
        "width",
        "height"
    ],
    "required": []
}

lookup["div"] = {
    "attributes": ["id", "class", "style", "title", "hidden", "data-*"],
    "required": []
}

lookup["header"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["nav"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["main"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["section"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["article"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["footer"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["p"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["span"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h1"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h2"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h3"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h4"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h5"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}

lookup["h6"] = {
    "attributes": ["id", "class", "style", "title"],
    "required": []
}


with open("lookup.json", "w+") as file:
    json.dump(lookup, file, indent=4)
