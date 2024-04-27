import xml.etree.ElementTree as ET

data = """
<person>
    <name>John</name>
    <phone type="intl">
        +1 458 568 7749
    </phone>
    <email hide="yes"/>
</person>
"""

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))
