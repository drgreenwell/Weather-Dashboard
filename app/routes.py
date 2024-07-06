# app/routes.py
from flask import render_template, request, redirect, url_for
from pymongo import MongoClient
from config import Config
from app import app
import requests

app.config.from_object(Config)

client = MongoClient(app.config['MONGODB_URI'])
db = client.weather_dashboard

def get_weather(city):
    api_key = app.config['OPENWEATHERMAP_API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        city = request.form['city']
        db.preferences.update_one({'name': 'default'}, {'$addToSet': {'cities': city}}, upsert=True)
        weather = get_weather(city)
        if weather:
            db.weather_data.insert_one({'city': city, 'data': weather})
        else:
            error = f'Weather data not found for {city}'
    preferences = db.preferences.find_one({'name': 'default'})
    cities = preferences.get('cities', []) if preferences else []
    weather_data = []
    for city in cities:
        weather_entry = db.weather_data.find_one({'city': city})
        if weather_entry:
            weather_data.append(weather_entry['data'])
        else:
            error = f'Weather data not found for {city}'
    return render_template('index.html', weather_data=weather_data, cities=cities, error=error)

@app.route('/update_preference', methods=['POST'])
def update_preference():
    new_city = request.form['city']
    db.preferences.update_one({'name': 'default'}, {'$addToSet': {'cities': new_city}}, upsert=True)
    return redirect(url_for('index'))

@app.route('/delete_preference', methods=['POST'])
def delete_preference():
    city_to_delete = request.form['city']
    db.preferences.update_one({'name': 'default'}, {'$pull': {'cities': city_to_delete}})
    db.weather_data.delete_one({'city': city_to_delete})
    return redirect(url_for('index'))