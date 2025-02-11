#!/usr/bin/env python3
"""
Serialize_to_xml :
serialize the dictionary into XML and save it to the given filename.
deserialize_from_xml :
read the XML data from that file, and return a deserialized Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    dictionary : python dict to serialize
    filename : file to save the serialized python dict
    """

    root = ET.Element("data")  # Create the principal element <data></data>

    # iterate through dictionary item and add each item in child
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Create subelement with dict key
        child.text = value  # Attribute the value of root[key]

    tree = ET.ElementTree(root)  # Create an XML tree
    ET.indent(tree, space="    ")  # indent with tabulation
    tree.write(filename)  # write the XML tree into filename


def deserialize_from_xml(filename):
    """
    filename : xml file to read
    """
    my_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        my_dict[child.tag] = child.text

    return my_dict
