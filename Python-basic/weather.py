# temp = 95
# if temp >75 and temp>50:
#     print("Its too hot")
#     print("stay in side")
# elif temp<20:
#     print("Its too cold")
#     print("stay inside")
# else:
#     print("enjoy outdoor")
# rain = True
# if not rain:
#     print("stay inside")

import requests
city= 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=12e4eef15923401983670110211712&q='+city+'&aqi=no'
response = requests.get(url)
weather_json= response.json()
temp= weather_json.get('current').get('temp_c')
description= weather_json.get('current').get('condition').get('text')
print(temp,description)