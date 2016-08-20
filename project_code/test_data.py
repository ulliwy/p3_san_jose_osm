cities = {}
tags = {}
temp = {}
county = {}

#getting all tags
def get_tags(element):
    if element.tag == "node" or element.tag == "way":
        for child in element.getchildren():
            if 'k' in child.attrib.keys():
                if child.attrib['k'] == 'addr:street':
                    if child.attrib['v'] in temp.keys():
                        temp[child.attrib['v']] += 1
                    else:
                        temp[child.attrib['v']] = 1
    return tags

#getting all cities
def get_cities(element):
    if element.tag == "node" or element.tag == "way":
        for child in element.getchildren():
            if 'k' in child.attrib.keys():
                if child.attrib['k'] == 'addr:city':
                    if child.attrib['v'] in ['Sunnyvale', 'Santa Clara', 'Milpitas', 'San Jose', 'Saratoga', 'Sunnyvale',
                                             'Cupertino', 'Morgan Hill', 'Campbell', 'Los Gatos', 'Mountain View']:
                        pass
                    else:
                        if child.attrib['v'] in cities.keys():
                            cities[child.attrib['v']] += 1
                        else:
                            cities[child.attrib['v']] = 1
    return cities

#get specific value
def get_value(element, all):
    if element.tag == "node" or element.tag == "way":
        for child in element.getchildren():
            if 'k' in child.attrib.keys():
                if child.attrib['k'].startswith('tiger:'):
                    all.add(child.attrib['k'])
    return all