import pandas as pd

dataf1 = pd.read_csv("./geodata/relations_grodno.csv")
dataf2 = pd.read_csv("./geodata/traffic_signals_grodno.csv")
dataf3 = pd.read_csv("./geodata/crossroads_grodno.csv")

dataf1 = dataf1.append(dataf2).append(dataf3)

data_all = dataf1.drop(dataf1.columns[[0]], axis=1)  # df.columns is zero-based

data_all.reset_index(inplace=True)
data_dict = data_all.to_dict()

data_dict.pop("index")

final_data_dict = {}
for coordinate_lat, coordinate_lon in zip(data_dict["longitude"].values(), data_dict["latitude"].values()):
    print(coordinate_lat)
    print(coordinate_lon)
    final_data_dict.setdefault(coordinate_lat, coordinate_lon)

import json
with open("./json_geodata/grodno.json",
          "w") as f:
    json.dump(final_data_dict, f)