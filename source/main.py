#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' the file pyramids.csv contains 62 Egyptian pyramids;
every pyramid has a Modern Name and some of them have an Ancient Name as it was translated from ancient egyptian hieroglyphs;
every pyramid has its coordinates - Latitude and Longitude in decimal form;
there are owners of a pyramid and sometimes supposed owners - symbol '(?)' follows the name of Pharaoh;
every pyramid is marked with it's Dynasty and location (Site);
there is missing data (Slope and Volume of some pyramids mostly);
base (Base1 (m) and Base2 (m)) and Height (m) of pyramid are in meters and represent the original size (that the pyramid was or was supposed to be);
some pyramids are marked with a Lepsius number which is a roman number from I to LXVII plus the pyramid number LG100 (pyramid of Khentkaus I);
most pyramids have a Type of construction (Step, True, Smooth-faced, Smooth-sided) and most used Material (Limestone, Mudbrick, Granite, Sandstone or a combination);
there is also a column Comment which contains some descriptive information.'''

import pandas as pd
import folium

def saveMap(prmds):
	'''ARRANGEs PYRAMIDS INTO PERIODS:
	has a function to color different kingdoms;
	provides a legend
	Сreates a map in html with all known pyramids
	glyphicon with open eye shows if Pharaoh is certain'''
	periods = {'EDP': (1,2), 'Old': (3,4,5,6,7), 'FIP': (8,9,10), 'Middle': (11,12,13,14), 'SIP': (15,16,17), 'New': (18,)}
	colors_dyn = {'EDP':'violet', 'Old': 'green', 'FIP': 'blue', 'Middle': 'orange', 'SIP': 'yellow', 'New': 'red'}

	def col_dyn(dyn):
		for k, v in periods.items():
			if dyn in v:
				c = colors_dyn[k]
				break
			else:
				c = 'black'
		return c

	legend_kingdom = '''
     <div style= "position: fixed; 
     bottom: 45px; left: 15px; width: 150px; height: 150px;white-space: pre-line; 
     border:1px solid grey; z-index:9999; font-size:10px; background-color:white;
     ">&nbsp; <b>Period</b>
    &nbsp; Early Dyn. Period &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:violet"></i>
     &nbsp; Old Kingdom &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:green"></i>
     &nbsp; FIP &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:lightblue"></i>
     &nbsp; Middle Kingdom &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:orange"></i>
    &nbsp; SIP &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:yellow"></i>
    &nbsp; New Kingdom &emsp;<i class="fa fa-caret-up fa-2x"
                  style="color:red"></i>
      </div>
     '''

	m = folium.Map(location = [lat_mean, lon_mean], #center of a map
               zoom_start=6, min_zoom = 5, width = 600, control_scale = True)
	try:
		for i in range(0,len(prmds)):
			lat = prmds.iloc[i]['Latitude']
			lon = prmds.iloc[i]['Longitude']
			folium.Marker([lat, lon], popup=prmds.iloc[i]['Modern name'], # show a modern name of pyramid in popup
					icon=folium.Icon(color=col_dyn(prmds.iloc[i]['Dynasty']),
									icon='eye-close' if str(prmds.iloc[i]['Pharaoh']).find("?")==-1 else 'eye-open') # glyphicon with open eye if Pharaoh is certain
					).add_to(m)
		m.get_root().html.add_child(folium.Element(legend_kingdom))		
		m.save(outfile= "../map-of-ancient-egypt/docs/map-pyramids.html")
	except Exception as e:
		print(f'Error creating map: {e}')
		return 
	return 'Map successfully created.'

def saveLepsiusMap(prmds_Le):
	'''Creats Lepsius list and map
	Drop rows where Lepsius column contains NaN values
	zoom in to get the pyramids and the Pharaoh's name'''
	prmds_Le = prmds.dropna(subset=['Lepsius'])
	m2 = folium.Map(location = [prmds_Le['Latitude'].mean(), prmds_Le['Longitude'].mean()],
               zoom_start=9, min_zoom = 6, width = 600)
	try:
		for i in range(0,len(prmds_Le)):
			lat = prmds_Le.iloc[i]['Latitude']
			lon = prmds_Le.iloc[i]['Longitude']
			temp = prmds_Le.iloc[i]['Lepsius']
			folium.CircleMarker([lat, lon],  radius=8,  color='red', fill=True, fill_color='red').add_to(m2)
			folium.Marker([lat, lon], 
					popup=prmds_Le.iloc[i]['Pharaoh'], 
							icon=folium.DivIcon(html=f'''<div style="font-family: arial; color: 'black'">{"{}".format(temp)}</div>''')
					
			).add_to(m2)		
		m2.save(outfile= "../map-of-ancient-egypt/docs/map-Lepsius.html")
	except Exception as e:
		print(f'Error creating Lepsius map: {e}')
		return 
	return 'Lepsius map successfully created.'

if __name__ == '__main__':	
	lat_mean = 29.22 # fix it
	lon_mean = 31.3
	prmds = pd.read_csv('../map-of-ancient-egypt/pyramids.csv') 
	# Get some statistics:
	print(prmds.describe())
	# find mean latitude and longitude of dataset;
	lat_mean = prmds['Latitude'].mean()
	lon_mean = prmds['Longitude'].mean()
	
	saveMap(prmds)
	saveLepsiusMap(prmds)