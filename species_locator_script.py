#imports
import streamlit as st
import folium
import geopandas as gpd
import earthpy as et
import pgeocode
import streamlit_folium
import pandas as pd

#Functions
def pinpoint_location(zipcode = "0"):
      nomi = pgeocode.Nominatim('us')
      if (zipcode != "0" and len(zipcode) != 5):
            st.write("Not a Valid US Zipcode!")
            return folium.Map(location=[37.0902, -95.7129], zoom_start = 4)
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

#Streamlit output 
zipcode = st.number_input('Enter Valid 5-digit US Zipcode to See Specific Location', min_value=0, max_value=99999, value=0)

dropdown = st.selectbox("Choose Map", ["Droughts"])

if dropdown == "Droughts":
      for index, row in county_data.iterrows():
          #no fucking clue why it dosen't let me use the actual collumn name INTPTLONG
          folium.Marker([row["INTPTLAT"], row[9]], popup=row["NAME"]).add_to(mymap)
    
mymap


streamlit_folium.folium_static(pinpoint_location(str(zipcode)))
