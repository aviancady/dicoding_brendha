import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
%matplotlib inline
from matplotlib.gridspec import GridSpec
import matplotlib.lines as mlines
import matplotlib.image as mpimg
pd.set_option('display.max_columns', 100)
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import json
import requests
import folium
from folium.plugins import FastMarkerCluster, Fullscreen, MiniMap, HeatMap, HeatMapWithTime, LocateControl
import datetime as dt

# Calculate time of mapping process
import time
start = time.perf_counter()

# Plot where the costomers are
import folium
from folium import Marker
from folium.plugins import MarkerCluster

# Make color palette
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex

def make_palette(n_samples, cmap):
    n_samples = n_samples
    color_map = plt.get_cmap(cmap)
    palette = []
    for c in np.linspace(0.0, 1.0, n_samples*2):
        color_code = rgb2hex(color_map(c))
        palette.append(color_code)
    return palette[n_samples:]

# Make color producer function
def color_producer(val):
    if val <= 45.9:
        return make_palette(2, "Blues")[0]
    if val <= 86.9:
        return make_palette(2, "Blues")[1]
    if val <= 137.8:
        return make_palette(1, "Wistia")[0]
    if val <= 149.9:
        return make_palette(2, "Reds")[0]
    else:
        return make_palette(2, "Reds")[1]

# Add points which is randomly selected(n_samples=1,000) on the map
# Make a sample data
import random
sample_idx = random.sample(purchase_price_df.index.to_list(), k=1000)
sample_df = purchase_price_df.loc[sample_idx]

# Add bubble map to base map
from folium import Circle

for i in range(0, len(sample_df)):
    Circle(
        location=[sample_df.iloc[i]["rep_lat"], sample_df.iloc[i]["rep_long"]],
        radius=sample_df.iloc[i]["purchase_price"],
        color=color_producer(sample_df.iloc[i]["purchase_price"]),
        popup=sample_df.iloc[i]["purchase_price"]
    ).add_to(m_2)

# Make function for add categorical legend
def add_categorical_legend(folium_map, title, colors, labels):
    if len(colors) != len(labels):
        raise ValueError("colors and labels must have the same length.")
    color_by_label = dict(zip(labels, colors))
    legend_categories = ""
    for label, color in color_by_label.items():
        legend_categories += f"<li><span style='background:{color}'></span>{label}</li>"
    legend_html = f"""
    <div id='maplegend' class='maplegend'>
      <div class='legend-title'>{title}</div>
      <div class='legend-scale'>
        <ul class='legend-labels'>
        {legend_categories}
        </ul>
      </div>
    </div>
    """
    script = f"""
        <script type="text/javascript">
        var oneTimeExecution = (function() {{
                    var executed = false;
                    return function() {{
                        if (!executed) {{
                             var checkExist = setInterval(function() {{
                                       if ((document.getElementsByClassName('leaflet-top leaflet-right').length) || (!executed)) {{
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].style.display = "flex"
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].style.flexDirection = "column"
                                          document.getElementsByClassName('leaflet-top leaflet-right')[0].innerHTML += `{legend_html}`;
                                          clearInterval(checkExist);
                                          executed = true;
                                       }}
                                    }}, 100);
                        }}
                    }};
                }})();
        oneTimeExecution()
        </script>
      """
    css = """
    <style type='text/css'>
      .maplegend {
        z-index:9999;
        float:right;
        background-color: rgba(255, 255, 255, 1);
        border-radius: 5px;
        border: 2px solid #bbb;
        padding: 10px;
        font-size:12px;
        positon: relative;
      }
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 0px solid #ccc;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    """
    folium_map.get_root().header.add_child(folium.Element(script + css))
    return folium_map