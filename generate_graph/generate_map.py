from IPython.core.display import HTML
from IPython.display import display
import pandas as pd
import vincent  as vince
import json
import matplotlib.pyplot as plt
import pprint
import canada_abbr

def draw_map(happiness_index_map):
    vince.core.initialize_notebook()
    with open('generate_graph/canada.topo.json', 'r') as f:
        canada_json = json.load(f)

    new_geoms = []
    for geom in canada_json['objects']['collection']['geometries']:
        geom['properties']['NAME'] = str(geom['properties']['NAME'])
        new_geoms.append(geom)

    canada_json['objects']['collection']['geometries'] = new_geoms

    with open('generate_graph/canada.topo.json', 'w') as f:
        json.dump(canada_json, f)


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
                    scale=400,
                    data_bind='Happiness',
                    data_key='NAME',
                    map_key={
                        'provinces': 'properties.NAME'
                    },
                    width=600,
                    height=200,
                    brew="Oranges")
    vis.marks[0].properties.enter.stroke_opacity = vince.ValueRef(value=0.5)
    vis.scales['color'].type = 'threshold'
    happiness_index_list = happiness_index_map.values()
    max_happiness_index = max(happiness_index_list)
    min_happiness_index = min(happiness_index_list)
    diff = round((max_happiness_index - min_happiness_index) / 8, 2)
    vis.scales['color'].domain = [round((x * diff + min_happiness_index),2) for x in range(len(happiness_index_list) - 1) ]
    vis.legend(title='Hapiness by Provinces')
    vis.display()


