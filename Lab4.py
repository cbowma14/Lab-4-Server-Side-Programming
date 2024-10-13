# Name: Cooper Bowman
# Course and Section: CSCI-2910-001
# Assignment: Lab 4
# Due Date: 10/13/24
# Description: This python program is designed to make an API call and print the received data


import requests

# Prompts the user to enter a zip code
zip = int(input("Enter the zip code for the area you would like weather information for: "))

# The URL path for making the request utilizing the zip code the user entered
url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid=06f40281f6945abf7ff11005fdb33f85"

# Makes the GET request
response = requests.get(url)


# Checks to see if the data was received successfully
if response.status_code == 200:


    # Parses the response
    data = response.json()
    
    # Extracts the relevant data 
    main = data['main']
    weather_desc = data['weather'][0]['description']
    temp = main['temp']
    pressure = main['pressure']
    humidity = main['humidity']
    wind = data['wind']['speed']

    # Converts the extracted temperature from Kelvin to Celsius and Fahrenheit
    temp_celsius = temp - 273.15
    temp_fahrenheit = (temp - 273.15) * 9/5 + 32

    # Prints the data
    print(f"Current weather in {data['name']}:")
    print(f"Temperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")
    print(f"Description: {weather_desc.capitalize()}")
    print(f"Air Pressure: {pressure} hPa")
    print(f"Air Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")



# Prints the error code if an error occurs
else:
    print(f"Request failed with status code: {response.status_code}")



    