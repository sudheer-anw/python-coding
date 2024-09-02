from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own OpenWeatherMap API key
API_KEY = 'your_api_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = get_weather(city)
    return render_template('index.html', weather_data=weather_data)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
