import pandas as pd

try:
    from xml.etree import cElementTree as ET
except ImportError as e:
    from xml.etree import ElementTree as ET


def extract_intersections(osm, verbose=True):
    dataframe_coordinates = pd.DataFrame(columns=["longitude", "latitude"])
    tree = ET.parse(osm)
    root = tree.getroot()
    counter = {}
    breakcycle = True
    dot_array = []
    for child in root:
        if child.tag == 'way':
            for item in child:
                try:
                    if item.attrib["k"] == "highway" and \
                            item.attrib["v"] in \
                            ["motorway", "trunk", "primary",
                             "secondary", "residential",
                             "unclassified", "tertiary"
                                             "motorway_link", "trunk_link",
                             "primary_link",
                             "secondary_link", "traffic_signals"]:
                        breakcycle = False

                        break
                    else:
                        breakcycle = True
                except:
                    breakcycle = True
            if breakcycle:
                breakcycle = False
                continue
            for item in child:
                if item.tag == 'nd':
                    nd_ref = item.attrib['ref']
                    dot_array.append(nd_ref)
                    if not nd_ref in counter:
                        counter[nd_ref] = 0

                    counter[nd_ref] += 1

    # Find nodes that are shared with more than one way, which
    # might correspond to intersections
    intersections = list(filter(lambda x: counter[x] > 1, counter))

    intersection_coordinates = []
    print(list(intersections))
    for child in root:

        if child.tag == 'node' and \
                child.attrib['id'] in intersections:

            dataframe_coordinates = dataframe_coordinates.append({
                "latitude":  child.attrib['lat'],
                "longitude": child.attrib['lon']
            },
                    ignore_index=True)
            coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
            if verbose:
                print(coordinate + ",1,#F18111")
            intersection_coordinates.append(coordinate)

    dataframe_coordinates.to_csv("geodata/crossroads_vitebsk.csv")

    return intersection_coordinates


extract_intersections("maps/map_vitebsk", verbose=True)
