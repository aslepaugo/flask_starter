from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Wroclaw")

    if weather:
        return f"Weather {weather['temp_C']}, feels like {weather['FeelsLikeC']}"
    else:
        return "Service is unavailable now"

if __name__ == "__main__":
    app.run()
