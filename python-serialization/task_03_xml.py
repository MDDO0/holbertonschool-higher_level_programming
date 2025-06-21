#!/usr/bin/python3
"""Serialization and deserialization using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The data to serialize.
        filename (str): The name of the XML file to write to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
