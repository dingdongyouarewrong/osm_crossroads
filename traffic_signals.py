intersection_coordinates = []
osm = "map_gomel"
import pandas as pd

try:
    from xml.etree import cElementTree as ET
except ImportError as e:
    from xml.etree import ElementTree as ET

tree = ET.parse(osm)
root = tree.getroot()
dataframe_coordinates = pd.DataFrame(columns=["longitude", "latitude"])

for child in root:
    if child.tag == "node":
        for item in child:

            if item.attrib["k"] == "traffic_signals" or item.attrib["v"] == \
                    "traffic_signals":
                dataframe_coordinates \
                    = dataframe_coordinates.append({"latitude":  child.attrib['lat'],
                                                    "longitude": child.attrib['lon']},
                                                   ignore_index=True)

                coordinate = child.attrib['lat'] + ',' + child.attrib['lon']

                print(coordinate + ",1,#79FE2D")
                break

dataframe_coordinates.to_csv("maps/traffic_signals_gomel.csv")
