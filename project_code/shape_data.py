import audit


CREATED = ["version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    created_key = {}
    pos = [None, None]
    node_refs = []
    address = {}
    tiger = {}
    tiger_temp = {'zip_left': [], 'zip_right': [], 'name_base': [], 'name_direction_suffix': [],
                  'name_direction_prefix': []}
    members = []

    if element.tag == "node" or element.tag == "way":
        node['type'] = element.tag                                          #element type

        for att in element.attrib.keys():                                   #parsing attributes
            if att in CREATED:
                created_key[att] = element.attrib[att]
            elif (att == 'lon'):
                try:                                                        #lon and lat must be numbers
                    pos[1] = float(element.attrib[att])
                except ValueError:
                    print element.attribfloat[att], 'longitude not number!!!!!'
            elif (att == 'lat'):
                try:
                    pos[0] = float(element.attrib[att])
                except ValueError:
                    print element.attrib[att], 'latitude not number!!!!!'
            else:
                node[att] = element.attrib[att]

        for child in element.getchildren():                                 #parsing children
            if child.tag == 'nd':                                           #parsing nd
                node_refs.append(child.attrib['ref'])
            if child.tag == 'tag':
                if child.attrib['k'].startswith('addr:'):                   #grouping for 'address'
                    if child.attrib['k'] == 'addr:street':
                        address['street'] = audit.audit_street(child.attrib['v'])   #fixing street type
                    elif child.attrib['k'] == 'addr:city':
                        address['city'] = audit.audit_city(child.attrib['v'])       #fixing city
                    else:
                        address[child.attrib['k'][5:]] = child.attrib['v']
                elif child.attrib['k'].startswith('tiger:'):                    #grouping 'tiger' data
                    if child.attrib['k'].startswith('tiger:zip_right'):
                        tiger_temp['zip_right'].append(child.attrib['v'])
                    elif child.attrib['k'].startswith('tiger:zip_left'):
                        tiger_temp['zip_left'].append(child.attrib['v'])
                    elif child.attrib['k'].startswith('tiger:name_base'):
                        tiger_temp['name_base'].append(child.attrib['v'])
                    elif child.attrib['k'].startswith('tiger:name_direction_suffix'):
                        tiger_temp['name_direction_suffix'].append(child.attrib['v'])
                    elif child.attrib['k'].startswith('tiger:name_direction_prefix'):
                        tiger_temp['name_direction_prefix'].append(child.attrib['v'])
                    else:
                        tiger_temp[child.attrib['k'][6:]] = child.attrib['v']
                else:
                    node[child.attrib['k']] = child.attrib['v']

    if element.tag == "relation":
        node['type'] = element.tag                                          #element type

        for att in element.attrib.keys():                                   #parsing attributes
            if att in CREATED:
                created_key[att] = element.attrib[att]
            else:
                node[att] = element.attrib[att]

        for child in element.getchildren():                                 #parsing children
            if child.tag == 'member':
                member = {'type': [], 'ref': [], 'role': ''}
                for m in child.attrib.keys():
                    member[m] = child.attrib[m]
                members.append(member)
            else:
                node[child.attrib['k']] = child.attrib['v']


    for i in tiger_temp.keys():
        if tiger_temp[i] != []:
            tiger[i] = tiger_temp[i]
    if created_key != {}:                           #adding all created data
        node['created'] = created_key
    if pos != [None, None]:
        node['pos'] = pos
    if tiger != {}:
        node['tiger'] = tiger
    if address != {}:
        node['address'] = address
    if node_refs != []:
        node['node_refs'] = node_refs
    if members != []:
        node['members'] = members

    return node

