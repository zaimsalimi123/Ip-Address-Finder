import requests
import streamlit as st

url = "https://api.ipgeolocation.io/ipgeo?apiKey=54ca81e4a7b34d51a063370066694c38&output=json"
api = "54ca81e4a7b34d51a063370066694c38"

response = requests.get(url)
content = response.json()

#1  2   3     4     5
ip,isp,org,country,city = (content["ip"], #1
                           content["isp"],#2
                           content["organization"],#3
                           content["country_name"],#4
                           content["city"])#5

st.header("Find Your IP Address")

if st.button("Find My IP"):
    st.write(f"Your IP Address: {ip}")
    st.write(f"Your Country : {country}")
    st.write(f"Your City: {city}")
    st.write(f"Your ISP: {isp}")
    st.write(f"Your Internet Organization : {org}")
