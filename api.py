import requests
from apikey import api_key


city = "asuncion"

def check_weather(city):

    url_base = "http://api.weatherapi.com/v1/current.json?"
    params = {"key" : api_key, "q" : city} 

    response = requests.get(url_base, params=params, timeout=5)
    print(f"response.url")

    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        return f"Err: {response.status_code}, {response.text}"
    
weather = check_weather(city)
print(weather)