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
    # province_code_happiness_index_map = dict()
    # for (province, happiness) in happiness_index_map.items():
    #     province_code_happiness_index_map[canada_abbr.abbr_dict().get(province)] = happiness

    province_happiness_df = pd.DataFrame({'Province Name': happiness_index_map.keys(), "Happiness": happiness_index_map.values()})
    province_province_code_df = pd.DataFrame({"Province Name": canada_abbr.abbr_dict().keys(), "NAME": canada_abbr.abbr_dict().values()}, dtype=str)
    province_province_code_happiness_df = pd.merge(province_happiness_df, province_province_code_df, on="Province Name", how='inner')

    province_province_code_happiness_df = province_province_code_happiness_df.fillna(method='pad')
    province_topo = r'generate_graph/canada.topo.json'

    geo_data = [
        {
            'name': 'provinces',
            'url': province_topo,
            'feature': 'collection'
        }
    ]

    #create map of canada, color coded based upon on the positive happiness index
    vis = vince.Map(data=province_province_code_happiness_df,
                    geo_data=geo_data,
                    scale=1100,
                    projection='albersUsa',
                    data_bind='Happiness',
                    data_key='NAME',
                    map_key={
                        'provinces': 'properties.NAME'
                    })
    vis.marks[0].properties.enter.stroke_opacity = vince.ValueRef(value=0.5)
    vis.scales['color'].type= 'threshold'

    vis.legend(title='Hapiness by Provinces')
    vis.to_json('Canada Happiness.json')


