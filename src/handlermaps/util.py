"""XML utilities. Assumes usage of the xml.etree.ElementTree module"""

from datetime import datetime

def toint(node):
    if node.text == "na":
        return "na"
    else:
        return int(node.text)

def tofloat(node):
    return float(node.text) if node.text else 0.0

def tobool(node):
    return node.text.lower() == "on"

def totext(node):
    return node.text

def todatetime(node):
    """Converts from a datetime in ISO 8601 format to a datetime object
    Note that datetime.fromisoformat() doesn't fully support ISO 8601 in Python 3.9
    (it seems Python 3.11 corrected this), so we have to drop the last "Z" from
    the string as a workaround
    """
    if node.text.endswith("Z"):
        return datetime.fromisoformat(node.text[:-1])
    else:
        return datetime.fromisoformat(node.text)

def findnode(root, xpath):
    """Finds an XML node, allowing for leading '/' or '.' to be used"""
    xpath = xpath[1:] if xpath.startswith("/") else xpath
    path_components = xpath.split("/")
    if path_components[0] == ".":
        return root.find(xpath)
    if path_components[0] == root.tag:
        return root.find("/".join(path_components[1:]))
    return None

def map_xml_payload(node, map):
    """Converts an XML node into a dictionary based on the supplied map"""
    result = { }
    for k, v in map.items():
        subNode = findnode(node, k)
        result.update({ v["name"]: v["handler"](subNode) })
    return result
