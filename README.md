# weather_program

# Simple Weather Data Fetcher using OpenWeatherMap API and JSON.
##  This code demonstrates object-oriented programming principles by encapsulating city-specific weather data and behavior within the City class. ##

The program retrieves weather data from the OpenWeatherMap API and presents it in a user-friendly format. 

Users can input different location parameters to access weather details, including:
- City name
- Latitude and Longitude (geographical coordinates to retrieve location-specific weather details)

The program will display the current temperature, the high temperature for the day, and the low temperature for the day.

# To use this program, sign up for a free API key at OpenWeatherMap at https://home.openweathermap.org/users/sign_up.
Once you have the API key, it can be used to request weather data via the OpenWeatherMap API endpoints.
Example API Request Format: https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_KEY}

The program will use the requests library to make the API call and the json library to parse the JSON response.

# The provided code is a program that models weather data for different cities using a City class. 
- The code includes functionality to print temperature information for two cities: London and Malaga. 
- It uses formatted strings (f-strings) to display the data in a user-friendly format.
- The City class has an __init__ method that initializes the city object with a name, latitude, longitude, and units (defaulting to "metric").
- It also highlights the use of f-strings for clean and readable output formatting.



## Code explained:


import requests
class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon  
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={API_KEY}")   ## enter your API key in place of: {API_KEY} ##

        except:
            print("An error occurred.Check your internet connection.")
    
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
    
    def temp_print(self):
        unit_symbol = "C" if self.units == "metric" else "F"
  
#The first set of print statements outputs temperature details for a city.These include the current temperature (self.temp), the day's high temperature (self.temp_max), and the day's low temperature (self.temp_min).
#The second set of print statements outputs the same temperature details for a vacation city.

        print(f"The weather in {self.name} is {self.temp}° {unit_symbol}")     
        print(f"Today's High: {self.temp_max}°{unit_symbol}")
        print(f"Today's Low: {self.temp_min}° {unit_symbol}") 
      
#The first instance, my_city, represents London, with its name, latitude, and longitude provided as arguments.

my_city = City("London", 51.5074, 0.1278)
my_city.temp_print()

#The second instance, vacation_city, represents Malaga, with its name, latitude, and longitude provided as arguments.

vacation_city = City("Malaga", 36.719444, -4.420000)
vacation_city.temp_print()


## Example of the output:

The weather in London is 10.5° C
Today's High: 11.56°C
Today's Low: 8.34° C
The weather in Malaga is 15.99° C
Today's High: 15.99°C
Today's Low: 15.7° C
