import re

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected_street_types = ["Street", "Avenue", "Boulevard", "Drive", "Court",
                         "Place", "Square", "Lane", "Road","Trail", "Parkway",
                         "Commons", "Way", 'Circle', 'Expressway', 'Plaza',
                         'Row', 'Terrace', 'Highway', 'Hill', 'Loop', 'Walk']

street_mapping = { "St": "Street",
            "St.": "Street",
            'Ave': 'Avenue',
            'ave': 'Avenue',
            'Rd.': 'Road',
            'Rd': 'Road',
            'Blvd': "Boulevard",
            'Dr': 'Drive',
            'Ct': 'Court',
            'Ln': 'Lane',
            'street': 'Street',
            'Sq': 'Square',
            'Boulvevard': 'Boulevard',
            'Cir': 'Circle',
            'Pkwy': 'Parkway'}


def audit_street(name):
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type in expected_street_types:                                #if street type is ok
            return name
        elif street_type in street_mapping.keys():                              #if street type in mapping
            res = re.sub(street_type_re, street_mapping[street_type], name)
            return res
        else:
            splitted = name.split(' ')                                          #trying to fix problem streets
            out = ''
            found = False
            for i in range(0, len(splitted)):
                word = splitted[i].replace(',', '')
                if word in expected_street_types:                               #find if type in the middle of the name
                    position = i
                    found = True
                elif word in street_mapping.keys():                             #find if type from mapping
                    position = i
                    splitted[i] = street_mapping[word]
                    found = True

            if found:                                                           #if street type found in the middle
                if splitted[position+1] in ['West', 'East']:
                    position +=1

                for k in range(0, position+1):                                  #creating output name
                    if k == 0:
                        out = splitted[k].replace(',', '')
                    else:
                        out = out + ' ' + splitted[k].replace(',', '')
                return out
            else:                                                               #if not just return name
                return name


cities = ['Sunnyvale', 'Santa Clara', 'Milpitas', 'San Jose', 'Saratoga', 'Sunnyvale', 'Cupertino', 'Morgan Hill',
          'Campbell', 'Los Gatos', 'Mountain View', 'Alviso', 'Redwood Estates', 'Felton', 'Moffett Field']


city_mapping = {'Mt Hamilton': 'Mount Hamilton',
                'Campbelll': 'Campbell',
                'Los Gato': 'Los Gatos'}


def audit_city(city):
    if city in cities:                                                          #if city is correct
        return city
    else:                                                                       #trying to find similar cities
        for i in range(0, len(cities)):
                if city[1:len(city)-1].lower() == cities[i][1:len(cities[i])-1].lower():
                    return cities[i]

    sp = city.split(', ')                                                       #getting rid of 'CA'
    if (len(sp) == 2) and (sp[0] in cities):
        return sp[0]
    elif city in city_mapping.keys():
        return city_mapping[city]
    else:
        return city