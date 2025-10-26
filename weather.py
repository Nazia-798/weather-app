import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"   # Free weather API (no key needed)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]

        # Extract details
        condition = current["weatherDesc"][0]["value"]
        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        cloud = current["cloudcover"]
        rain_chance = data["weather"][0]["hourly"][0]["chanceofrain"]
        snow_chance = data["weather"][0]["hourly"][0]["chanceofsnow"]

        # Show result
        print(f"\n🌤️ Weather in {city.capitalize()}, Pakistan:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} km/h")
        print(f"☁️ Cloud Cover: {cloud}%")
        print(f"🌧️ Chance of Rain: {rain_chance}%")
        print(f"❄️ Chance of Snow: {snow_chance}%")

    else:
        print("❌ Could not fetch weather data. Please check your internet or city name.")

# --- Main Program ---
city = input("Enter a Pakistan city name: ")
get_weather(city)

