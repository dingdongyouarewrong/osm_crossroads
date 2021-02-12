intersection_coordinates = []
osm = "map_big.osm"

import pandas as pd
try:
    from xml.etree import cElementTree as ET
except ImportError as e:
    from xml.etree import ElementTree as ET


tree = ET.parse(osm)
root = tree.getroot()
dataframe_coordinates = pd.DataFrame(columns=["longitude", "latitude"])
relations = []
for child in root:
    if child.tag == 'relation':
        for item in child:
            try:
                if (item.attrib["type"] == "node" or
                    item.attrib["type"] == "way") and\
                        item.attrib["role"] in ["via", "to", "from"]:
                    relations.append(item.attrib["ref"])
            except:
                continue

for child in root:
    if child.tag == 'node' and \
                    child.attrib['id'] in relations:
        coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
        if coordinate not in intersection_coordinates:
            print(coordinate + ",1,#ffc1dc")
            intersection_coordinates.append(coordinate)
# Extract intersection coordinates
# You can plot the result using this url.
# http://www.darrinward.com/lat-long/
intersection_coordinates = []