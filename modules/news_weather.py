"""
Jarvis News and Weather Module
Gets current news and weather information
"""

import requests
import json
from datetime import datetime

class NewsProvider:
    """Get latest news"""
    
    def __init__(self):
        self.api_url = "https://newsapi.org/v2/top-headlines"
        self.api_key = None  # Users can add their own from newsapi.org
    
    def get_top_news(self, country="us", limit=3):
        """Get top news headlines"""
        try:
            # Using free news API (no key required for basic use)
            url = "https://api.currentsapi.services/v1/latest-news?apikey=demo"
            
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                news = []
                for article in data.get('news', [])[:limit]:
                    news.append(f"• {article.get('title', 'No title')}")
                return "\n".join(news) if news else "No news available"
            else:
                return "Could not fetch news at this time"
        except Exception as e:
            return f"News service unavailable: {str(e)}"

class WeatherProvider:
    """Get weather information"""
    
    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast"  # Free API, no key needed!
    
    def get_weather(self, city="Berlin"):
        """Get weather for a city"""
        try:
            # Using Open-Meteo API (free, no key required)
            # First, we need to geocode the city
            geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
            geo_params = {"name": city, "count": 1, "language": "en"}
            
            geo_response = requests.get(geocode_url, params=geo_params, timeout=5)
            if geo_response.status_code != 200:
                return f"Could not find city: {city}"
            
            geo_data = geo_response.json()
            if not geo_data.get('results'):
                return f"City not found: {city}"
            
            location = geo_data['results'][0]
            latitude = location['latitude']
            longitude = location['longitude']
            city_name = location['name']
            country = location.get('country', '')
            
            # Get weather
            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m",
                "temperature_unit": "celsius"
            }
            
            weather_response = requests.get(self.api_url, params=weather_params, timeout=5)
            if weather_response.status_code != 200:
                return "Could not fetch weather data"
            
            weather_data = weather_response.json()
            current = weather_data.get('current', {})
            
            temp = current.get('temperature_2m', 'N/A')
            humidity = current.get('relative_humidity_2m', 'N/A')
            wind = current.get('wind_speed_10m', 'N/A')
            
            # Weather code interpretation
            weather_codes = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Foggy",
                48: "Foggy",
                51: "Light drizzle",
                61: "Slight rain",
                80: "Moderate rain",
                95: "Thunderstorm"
            }
            
            weather_code = current.get('weather_code', 0)
            weather_desc = weather_codes.get(weather_code, "Unknown")
            
            weather_text = f"""
🌍 Weather in {city_name}, {country}
🌡️  Temperature: {temp}°C
☁️  Condition: {weather_desc}
💧 Humidity: {humidity}%
💨 Wind Speed: {wind} km/h
"""
            return weather_text.strip()
            
        except Exception as e:
            return f"Weather service error: {str(e)}"

class InfoProvider:
    """Combined info provider"""
    
    def __init__(self):
        self.news = NewsProvider()
        self.weather = WeatherProvider()
    
    def get_daily_briefing(self, city="Berlin"):
        """Get complete daily briefing"""
        briefing = "📰 Daily Briefing\n"
        briefing += "=" * 50 + "\n\n"
        
        # Weather
        briefing += "Weather:\n"
        briefing += self.weather.get_weather(city) + "\n\n"
        
        # News
        briefing += "Top News:\n"
        briefing += self.news.get_top_news(limit=3) + "\n"
        
        return briefing
