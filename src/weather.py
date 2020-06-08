
from threading import Timer

from matrix import Matrix
from font import Font

from pyowm import OWM



class Weather():
    def __init__(self, matrix):
        self.matrix = matrix
        self.owm = OWM('??')

        self.font_small = Font(file = "CGpixel3x5.ttf", size = 5)

        self.getData()

    def getData(self):
        mgr = self.owm.weather_manager()
        observation = mgr.weather_at_place('Regierungsbezirk Detmold, DE')
        self.currentWeather = observation.weather

        # Get new weather data every 15 mins
        Timer(900, self.getData).start()

    def draw(self):
        self.matrix.draw_image_rgba("../assets/weather/sun.png")
        #temperature = self.currentWeather.temperature('celsius')
        #self.matrix.draw_text(["50%","17%"],text=current_date,fill=(50, 50, 30),font=self.font_small.font, align="center-center" )
        
    def temperature(self):
        return currentWeather.temperature('celsius')

    def humidity(self):
        return currentWeather.wind()
