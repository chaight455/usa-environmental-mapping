#imports
import streamlit as st
import folium
import geopandas as gpd
import earthpy as et
import pgeocode
import streamlit_folium
import pandas as pd
import random

#Functions
def pinpoint_location(zipcode = "0"):
      nomi = pgeocode.Nominatim('us')
      #Check if zipcode is valid
      if (zipcode != "0" and len(zipcode) != 5):
            st.write("Not a Valid US Zipcode!")
            return folium.Map(location=[37.0902, -95.7129], zoom_start = 4)
      #display map based on latiitude and longitude
      if (zipcode != "0"):
            user_zip = nomi.query_postal_code(zipcode)
            user_lat = user_zip['latitude']
            user_long = user_zip['longitude']
            if (pd.isnull(user_lat)):
                  st.write("Not a Valid US Zipcode!")
                  return folium.Map(location=[37.0902, -95.7129], zoom_start = 4)
            mymap = folium.Map(location=[user_lat, user_long], zoom_start=12)
      else:
            mymap = folium.Map(location=[37.0902, -95.7129], zoom_start = 4)
      return mymap

#Print out blank usa map
streamlit_folium.folium_static(pinpoint_location(str(zipcode)))

#get zip from user
zipcode = st.number_input('Enter Valid 5-digit US Zipcode to See Specific Location', min_value=0, max_value=99999, value=0)

#get map type from user
dropdown = st.selectbox("Choose Map", ["Droughts"])

#add markers to map based on type that user choose
if dropdown == "Droughts":
      mymap = pinpoint_location(str(zipcode)) # Store the map returned by the function
      for index, row in county_data.iterrows():
          # Access the 'INTPTLAT' and 'INTPTLONG' columns directly
          folium.Marker([row["INTPTLAT"]+random.uniform(0, 1), row[9]]+random.uniform(0, 1), popup=row["NAME"]).add_to(mymap)
    
streamlit_folium.folium_static(mymap)
