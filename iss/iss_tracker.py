#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude and human-readable address"""
import requests
from datetime import datetime
import reverse_geocoder as rg
import pycountry

URL = "http://api.open-notify.org/iss-now.json"

def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name
    except:
        return country_code

def main():
    resp = requests.get(URL).json()
    timestamp = resp['timestamp']
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']
    
    # Convert timestamp to human-readable format
    readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get human-readable location
    coordinates = (lat, lon)
    location = rg.search(coordinates, mode=1)
    city = location[0]['name']
    country_code = location[0]['cc']
    country_name = get_country_name(country_code)
    
    # Output the results
    print(f"CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {readable_time}")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City/Country: {city}, {country_name}")

if __name__ == "__main__":
    main()

