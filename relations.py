intersection_coordinates = []
osm = "maps/map_vitebsk"

import pandas as pd
try:
    from xml.etree import cElementTree as ET
except ImportError as e:
    from xml.etree import ElementTree as ET


tree = ET.parse(osm)
root = tree.getroot()
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
dataframe_coordinates = pd.DataFrame(columns=["longitude", "latitude"])

for child in root:
    if child.tag == 'node' and \
                    child.attrib['id'] in relations:
        coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
        if coordinate not in intersection_coordinates:
            print(coordinate + ",1,#ffc1dc")
            print(child.attrib['lon'])
            print(child.attrib['lat'])
            dataframe_coordinates = dataframe_coordinates.append({
                "latitude":child.attrib['lat'],
                                          "longitude":child.attrib['lon']},
                                         ignore_index=True)
            intersection_coordinates.append(coordinate)
dataframe_coordinates.to_csv("geodata/relations_vitebsk.csv")

intersection_coordinates = []