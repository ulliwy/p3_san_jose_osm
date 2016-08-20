 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the
tag name as the key and number of times this tag can be encountered in
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

TAGS_MAP = {}


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def check(node):
    print node.tag
    if node.tag in TAGS_MAP.keys():
        TAGS_MAP[node.tag] += 1
    else:
        TAGS_MAP[node.tag] = 1



def traverse_tree(node, tags):
    if node.tag in tags.keys():
        tags[node.tag] += 1
    else:
        tags[node.tag] = 1
    for child in node:
        traverse_tree(child, tags)
    return tags


def count_tags(filename):
    root = get_root(filename)
    tags = traverse_tree(root, {})
    return tags


count_tags('example.osm')



def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}



if __name__ == "__main__":
    test()