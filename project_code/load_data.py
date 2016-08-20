import xml.etree.cElementTree as ET
from timeit import default_timer
import codecs
import json

import shape_data

FILENAME = 'river_oaks.osm'                 #small 971 kb
FILENAME2 = 'neighborhood.osm'              #medium 6.1 mb
FILENAME3 = 'san-jose_california.osm'       #large 282.7 mb


def process_map(filename, pretty = False):
    file_out = "{0}.json".format(filename)                              #output file
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(filename):
            el = shape_data.shape_element(element)
            #test = test_data.get_value(element, all)                   #for testing
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


if __name__ == "__main__":
    start = default_timer()
    data = process_map(FILENAME, True)
    t = default_timer() - start
    m = int(t/60)
    s = int(t - m*60)
    print t
    print 'Time: %i min %i sec' % (m, s)

    #with open('filename_stat.csv', 'wb') as csv_file:              #create test csv
    #    writer = csv.writer(csv_file)
    #    for key, value in tags.items():
    #        writer.writerow([key, value])
