import requests
from apikey import api_key
import requests.exceptions


#city = "asuncion"

def check_weather(city):

    url_base = "http://api.weatherapi.com/v1/current.json?"
    params = {"key" : api_key, "q" : city} 

    try:

        response = requests.get(url_base, params=params, timeout=5)
        print(f"{response.url}")

        if response.status_code == 200:
            data = response.json()
            location = data["location"]
            current = data["current"]
            return {
                
                "ciudad": location["name"],
                "region": location["region"],
                "pais": location["country"],
                "temperatura_actual": current["temp_c"],
                "condicion_actual": current["condition"]["text"],
                "precipitacion": current["precip_mm"],
                "humedad": current["humidity"],
                "fecha_actualizacion": current["last_updated"],
            }
        
        elif response.status_code == 400:
            raise Exception (f"Ubicacaion no encontrada: {city}")
        
        else:
            raise Exception (f"Err: {response.status_code}")
    except requests.exceptions.ConnectionError:
            raise Exception ("Error de connexion")
            