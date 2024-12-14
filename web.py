import requests
import streamlit as st

url = "your_api_key_link"
api = "your_api_key"

response = requests.get(url)
content = response.json()


ip,isp,org,country,city = (content["ip"], 
                           content["isp"],
                           content["organization"],
                           content["country_name"],
                           content["city"])

st.header("Find Your IP Address")

if st.button("Find My IP"):
    st.write(f"Your IP Address: {ip}")
    st.write(f"Your Country : {country}")
    st.write(f"Your City: {city}")
    st.write(f"Your ISP: {isp}")
    st.write(f"Your Internet Organization : {org}")
