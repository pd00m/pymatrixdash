
from threading import Timer
import json

from matrix import Matrix
from font import Font

from pyowm import OWM

class WeatherScreen():
    def __init__(self, config, matrix):

        self.showDuration = config["screens"]["weatherScreen"].get("showDuration")
        self.apiKey = config["screens"]["weatherScreen"].get("apiKey")
        self.cityId = config["screens"]["weatherScreen"].get("cityId")
        self.format = config.get("format")
        
        print("Configrued weather plugin:")
        print("API Key: " + str(self.apiKey))
        print("City ID: " + str(self.cityId))
        print("Format: " + str(self.format))

        # assignment of weather icons according to openweathermap API documentation - https://openweathermap.org/weather-conditions
        self.weatherIcons = {   "thunderstorm with light rain": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm with rain": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm with heavy rain": "../assets/img/weather/thunderstorm.png", 
                                "light thunderstorm": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm": "../assets/img/weather/thunderstorm.png", 
                                "heavy thunderstorm": "../assets/img/weather/thunderstorm.png", 
                                "ragged thunderstorm": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm with light drizzle": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm with drizzle": "../assets/img/weather/thunderstorm.png", 
                                "thunderstorm with heavy drizzle": "../assets/img/weather/thunderstorm.png",
                                "light intensity drizzle": "../assets/img/weather/rainy.png", 
                                "drizzle": "../assets/img/weather/rainy.png", 
                                "heavy intensity drizzle": "../assets/img/weather/rainy.png", 
                                "light intensity drizzle rain": "../assets/img/weather/rainy.png", 
                                "drizzle rain": "../assets/img/weather/rainy.png", 
                                "heavy intensity drizzle rain": "../assets/img/weather/rainy.png", 
                                "shower rain and drizzle": "../assets/img/weather/rainy.png", 
                                "heavy shower rain and drizzle": "../assets/img/weather/rainy.png", 
                                "shower drizzle": "../assets/img/weather/rainy.png",
                                "light rain": "../assets/img/weather/rainy.png", 
                                "moderate rain": "../assets/img/weather/rainy.png", 
                                "heavy intensity rain": "../assets/img/weather/rainy.png", 
                                "very heavy rain": "../assets/img/weather/rainy.png", 
                                "extreme rain": "../assets/img/weather/rainy.png", 
                                "freezing rain": "../assets/img/weather/rainy.png", 
                                "light intensity shower rain": "../assets/img/weather/rainy.png", 
                                "shower rain": "../assets/img/weather/rainy.png", 
                                "heavy intensity shower rain": "../assets/img/weather/rainy.png", 
                                "ragged shower rain": "../assets/img/weather/rainy.png",                                 
                                "light snow": "../assets/img/weather/snowy.png",
                                "snow": "../assets/img/weather/snowy.png",
                                "Heavy snow": "../assets/img/weather/snowy.png",
                                "Sleet": "../assets/img/weather/snowy.png",
                                "Light shower sleet": "../assets/img/weather/snowy.png",
                                "Shower sleet": "../assets/img/weather/snowy.png",
                                "Light rain and snow": "../assets/img/weather/snowy.png",
                                "Rain and snow": "../assets/img/weather/snowy.png",
                                "Light shower snow": "../assets/img/weather/snowy.png",
                                "Shower snow": "../assets/img/weather/snowy.png",
                                "Heavy shower snow": "../assets/img/weather/snowy.png",
                                "mist": "../assets/img/weather/mist.png",
                                "Smoke": "../assets/img/weather/mist.png",
                                "Haze": "../assets/img/weather/mist.png",
                                "sand/ dust whirls": "../assets/img/weather/mist.png",
                                "fog": "../assets/img/weather/mist.png",
                                "sand": "../assets/img/weather/mist.png",
                                "dust": "../assets/img/weather/mist.png",
                                "volcanic ash": "../assets/img/weather/mist.png",
                                "squalls": "../assets/img/weather/mist.png",
                                "tornado": "../assets/img/weather/mist.png",
                                "clear sky": "../assets/img/weather/sunny.png",
                                "few clouds": "../assets/img/weather/halfsunny.png",
                                "scattered clouds": "../assets/img/weather/cloudy.png",
                                "broken clouds": "../assets/img/weather/cloudy.png",
                                "overcast clouds": "../assets/img/weather/cloudy.png",
                                "error": "../assets/img/weather/error.png" }

        self.matrix = matrix
        

        self.font_small = Font(file = "mini_pixel-7.ttf", size = 20)
        
        self.owm = OWM(self.apiKey)
        self.getData()

    def getShowDuration(self):
        return int(self.showDuration)

    def getData(self):
        mgr = self.owm.weather_manager()

        try:
            observation = mgr.weather_at_id(self.cityId)
            dailyForecast = mgr.forecast_at_id(self.cityId, "daily").forecast
        except:
            self.currentWeatherStatus = self.weatherIcons.get("error")
            self.currentTemperature = "API KEY"
        else:
            self.currentWeatherStatus = self.weatherIcons.get(str(observation.weather.detailed_status), "../assets/img/weather/error.png")
            if(self.format == "imperial"):
                self.currentTemperature = str(round(observation.weather.temperature("farenheit").get("temp"), 1)) + " F"
            else:
                self.currentTemperature = str(round(observation.weather.temperature("celsius").get("temp"), 1)) + " C"
        
        #print(dailyForecast)
        #self.forecastMaxTemperature = dailyForecast
        #self.forecastMinTemperature = 
        # Get new weather data every 15 mins
        Timer(900, self.getData).start()

    def draw(self):

        self.matrix.draw_image_rgba(self.currentWeatherStatus, (2,2))
        self.matrix.draw_text(["60%","32%"],text=self.currentTemperature,fill=(50, 50, 50),font=self.font_small.font, align="center-center" )
