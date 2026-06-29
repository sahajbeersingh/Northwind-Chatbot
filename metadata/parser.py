import xml.etree.ElementTree as ET
import json

def parse_metadata():
    tree = ET.parse("metadata/metadata.xml")
    root = tree.getroot()
    schema_dict = {}
    for child in root:
        for schema in child:
            for element in schema:
                if "EntityType" in element.tag:
                    entity_name = element.attrib["Name"]
                    schema_dict[entity_name] = {
                        "primary_keys": [],
                        "properties": {},
                        "navigation": []}
                    for x in element:
                        tag = x.tag.split("}")[-1]
                        if tag == "Key":
                            for y in x:
                                child_tag = y.tag.split("}")[-1]
                                if child_tag == "PropertyRef":
                                    schema_dict[entity_name]["primary_keys"].append(y.attrib["Name"])
                        elif "NavigationProperty" == tag:
                            schema_dict[entity_name]["navigation"].append(x.attrib["Name"])
                        elif "Property" == tag:
                            schema_dict[entity_name]["properties"][x.attrib["Name"]] = (x.attrib["Type"])
    with open("metadata/schema.json", "w", encoding="utf-8") as f:
        json.dump(schema_dict, f, indent=4)

if __name__=="__main__":
    parse_metadata()

