"""XML utilities. Assumes usage of the xml.etree.ElementTree module"""

from datetime import datetime
from typing import Any, Callable, Dict, Optional, Union
from xml.etree.ElementTree import Element

from . import Map, Handler

def toint(node: Element) -> Union[int, str]:
    if node.text == "na":
        return "na"
    else:
        return int(node.text) if node.text else 0

def tofloat(node: Element) -> float:
    return float(node.text) if node.text else 0.0

def tobool(node: Element) -> bool:
    return node.text.lower() == "on" if node.text else False

def totext(node: Element) -> str:
    return node.text if node.text else ""

def todatetime(node: Element) -> datetime:
    """Converts from a datetime in ISO 8601 format to a datetime object
    Note that datetime.fromisoformat() doesn't fully support ISO 8601 in Python 3.9
    (it seems Python 3.11 corrected this), so we have to drop the last "Z" from
    the string as a workaround
    """
    if node.text and node.text.endswith("Z"):
        return datetime.fromisoformat(node.text[:-1])
    else:
        return datetime.fromisoformat(node.text if node.text else "")

def findnode(root: Element, xpath: str) -> Optional[Element]:
    """Finds an XML node, allowing for leading '/' or '.' to be used"""
    xpath = xpath[1:] if xpath.startswith("/") else xpath
    path_components = xpath.split("/")
    if path_components[0] == ".":
        return root.find(xpath)
    if path_components[0] == root.tag:
        return root.find("/".join(path_components[1:]))
    return None

def map_xml_payload(node: Element, map: Map) -> Dict[str, Handler]:
    """Converts an XML node into a dictionary based on the supplied map"""
    result = { }
    for k, v in map.items():
        subNode = findnode(node, k)
        result.update({ v["name"]: v["handler"](subNode) })
    return result
