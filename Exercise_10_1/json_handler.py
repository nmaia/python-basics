import json

data = """
{
    "name": "John",
    "phone": {
        "type": "intl",
        "number": "+1 258 157 5687"
    },
    "email": {
        "hide": "yes"
    }
}
"""

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])
