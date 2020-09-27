import requests
import settings

def weather_by_city(city_name):
    weather_url = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        "key": settings.API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()

        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Network error")
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("Wroclaw"))