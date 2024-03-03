import requests #the request module will get the weather data for you 
from apikey import api

apikey="54ce6773f54b5e444847909c3212f4ba"

city ="New York" #write the city whose weather you want to get 
#use rdequsts module to get the url for weather data on openweather 
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q=los%20angeles&units=imperial&cnt=3&appid=7b26c92417fd3678d52eac12dc870222"
f"{city}&units=imperial&APPID="
f"'{apikey}")

weather_conde=weather_data.json()['weather'][0]['main']
temp=round(weather_conde.json['main']['temp'])
maxtemp=round(weather_conde.json['main']['temp_max'])
mintemp=round(weather_conde.json['main']['temp_min'])

print(f"{city}")
print(f"Current Temperature :{temp}")


