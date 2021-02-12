import pandas as pd
import matplotlib.pyplot as plt
try:
    from xml.etree import cElementTree as ET
except ImportError as e:
    from xml.etree import ElementTree as ET

dataframe_coordinates = pd.DataFrame(columns=["longitude", "latitude"])

def extract_intersections(osm, verbose=True):
    # This function takes an osm file as an input. It then goes through each xml 
    # element and searches for nodes that are shared by two or more ways.
    # Parameter:
    # - osm: An xml file that contains OpenStreetMap's map information
    # - verbose: If true, print some outputs to terminal.
    # 
    # Ex) extract_intersections('WashingtonDC.osm')
    #
    breakcycle = True
    tree = ET.parse(osm)
    root = tree.getroot()
    counter = {}
    i=1
    for child in root:
        if child.tag == 'way':
            for item in child:
                try:

                    if item.attrib["k"] =="highway" and\
                        item.attrib["v"] in \
                            ["motorway", "trunk", "primary",
                                                 "secondary","residential",
                             "unclassified", "tertiary"
                                                 "motorway_link", "trunk_link", "primary_link",
                                                 "secondary_link", "traffic_signals"]:
                        breakcycle = False
                        i+=1
                        print(i)
                        break
                    else:
                        breakcycle = True
                        break
                except:
                    breakcycle = True
            if breakcycle:
                breakcycle=False
                continue
            for item in child:
                print(item.attrib)
            for item in child:
                if item.tag == 'nd':
                    nd_ref = item.attrib['ref']
                    if not nd_ref in counter:
                        counter[nd_ref] = 0

                    counter[nd_ref] += 1

    # Find nodes that are shared with more than one way, which
    # might correspond to intersections
    intersections = list(filter(lambda x: counter[x] > 1, counter))

    # viafrom = []
    # for child in root:
    #     if child.tag == 'relation':
    #         for item in child:
    #             try:
    #                 if (item.attrib["type"] == "node" or
    #                     item.attrib["type"] == "way") and\
    #                         item.attrib["role"] in ["via", "to", "from"]:
    #                         if item.attrib["ref"] not in intersections:
    #                             viafrom.append(item.attrib["ref"])
    #             except:
    #                 continue
    # Extract intersection coordinates
    # You can plot the result using this url.
    # http://www.darrinward.com/lat-long/
    intersection_coordinates = []
    print(list(intersections))
    for child in root:

        if child.tag == 'node' and \
                        child.attrib['id'] in intersections:

            # if child.tag == 'node' and \
            #         child.attrib['id'] in intersections:
            # childlist = list(child)
            # for tag in childlist:
            #     if tag.attrib["k"]=="building":
            #         breakcycle = True
            #         break
            # if breakcycle:
            #     breakcycle=False
            #     continue
            # for item in child:
            #     if item.attrib["k"] == "highway" or id in viafrom:
            dataframe_coordinates.append({"latitude":child.attrib['lat'],
                                          "longitude":child.attrib['lon']},
                                         ignore_index=True)
            coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
            if verbose:
                print(coordinate+",1,#F18111")
            intersection_coordinates.append(coordinate)
    # for child in root:

        # if child.tag == 'node' and \
        #         child.attrib['id'] in viafrom:
        #     coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
        #     if coordinate not in intersection_coordinates:
        #         print(coordinate + ",1,#F18111")
        #         intersection_coordinates.append(coordinate)
    return intersection_coordinates


extract_intersections("map.osm", verbose=True)
minlat = "52.4309000"
minlon = "30.9852000"
maxlat = "52.4434000"
maxlon = "31.0162000"

BBox = ((minlon,   maxlon,
         minlat, maxlat))
ruh_m = plt.imread('map.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(dataframe_coordinates.longitude, dataframe_coordinates.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')

