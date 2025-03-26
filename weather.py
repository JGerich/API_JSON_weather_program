
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
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={API_KEY}")  ## enter your API key in place of: {API_KEY} ##

        except:
            print("An error occurred.Check your internet connection.")
    
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
    
    def temp_print(self):
        unit_symbol = "C" if self.units == "metric" else "F"
  
        print(f"The weather in {self.name} is {self.temp}° {unit_symbol}")     
        print(f"Today's High: {self.temp_max}°{unit_symbol}")
        print(f"Today's Low: {self.temp_min}° {unit_symbol}") 
      
my_city = City("London", 51.5074, 0.1278)
my_city.temp_print()

vacation_city = City("Malaga", 36.7178, -4.4256)
vacation_city.temp_print()

