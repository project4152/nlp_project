import pandas as pd
import vincent  as vince
import json
import matplotlib.pyplot as plt
import pprint
import canada_abbr

def draw_map(happiness_index_map):
    with open('generate_graph/canada.topo.json', 'r') as f:
        canada_json = json.load(f)

    new_geoms = []
    for geom in canada_json['objects']['collection']['geometries']:
        geom['properties']['NAME'] = str(geom['properties']['NAME'])
        new_geoms.append(geom)

    canada_json['objects']['collection']['geometries'] = new_geoms

    with open('generate_graph/canada.topo.json', 'w') as f:
        json.dump(canada_json, f)

    #grab the province names and load them into a dataframe
    # geometries = canada_json['objects']['collection']['geometries']
    # province_names = [x['properties']['NAME'] for x in geometries]
    # province_df = pd.DataFrame({'NAME': province_names}, dtype=str)
    #
    #translate province name into province code
    province_code_happiness_index_map = dict()
    for (province, happiness) in happiness_index_map.items():
        province_code_happiness_index_map[canada_abbr.abbr_dict().get(province)] = happiness

    province_code_happiness_df = pd.DataFrame({'NAME': province_code_happiness_index_map.keys(), "Happiness": province_code_happiness_index_map.values()})
    pprint.pprint(province_code_happiness_df)


