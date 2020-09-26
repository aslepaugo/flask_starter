from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    page_title = "Python news"
    weather = weather_by_city("Wroclaw")

    return render_template('index.html', page_title=page_title, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
