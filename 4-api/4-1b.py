import requests


def geocode(location):
    uri = "https://portal.app.cent-su.org/api/weather/geocode"
    params = {"language": "en", "count": 5, "place": location}
    headers = {"accept": "application/json"}
    response = requests.get(uri, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def weather(lat, lon):
    uri = "https://portal.app.cent-su.org/api/weather/current"
    params = {"lat": lat, "lon": lon}
    headers = {"accept": "application/json"}
    response = requests.get(uri, params=params, headers=headers)
    response.raise_for_status()
    weather_data = response.json()
    return weather_data["current"]["temperature_2m"]

import streamlit as st
st.title("Weather App")
location = st.text_input("Enter a location(city, state, or country:)")
if location:
    lat, lon = geocode(location)
    if lat is None or lon is None:
        st.error("Location not found.")
    else:
        temp = weather(lat, lon)
        st.write(f"The current temperature in {location} is {temp}°C.")