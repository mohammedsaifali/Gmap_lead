from gomaps import maps_search
import streamlit as st
import json
import csv


st.title('CP GMaps Extraction')
st.image('./header.png')
st.write('Powered by Constructions Platform LLC')
query = st.text_input('Enter your Keyword for lead extraction')
if st.button('submit'):
    result = maps_search(query) # Returns a list of GoogleMaps objects
# GoogleMapsResults([<gomaps.GoogleMaps object; Place-Name: Tops Diner>])
df = pd.read_json(result)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
