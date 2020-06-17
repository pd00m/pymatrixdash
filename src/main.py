import time
from threading import Timer
from itertools import cycle
import json

# Base classes
from base import Base
from matrix import Matrix

# Screens
from clock import ClockScreen
from hello import HelloScreen
from scroll import ScrollScreen

from weather import WeatherScreen

class Main(Base):

    def run(self):
        with open("config.json") as json_file:
            config = json.load(json_file)

        frame = Matrix(self.matrix)

        self.screenCycle = cycle([ScrollScreen(config, frame)])
        self.currentScreen = next(self.screenCycle)
        self.next_screen()


        while True:
            #time.sleep(0.1)  
            frame.clear()
            self.currentScreen.draw()
            frame.render()

    def next_screen(self):
        print("switching to next screen...")
        self.currentScreen = next(self.screenCycle)
        Timer(self.currentScreen.getShowDuration(), self.next_screen).start() 

# Main function
if __name__ == "__main__":
    main = Main()
    if (not main.process()):
        main.print_help()


# sudo ../env/bin/python3 main.py --led-gpio-mapping=adafruit-hat-pwm --led-rows=32 --led-cols=64 --led-slowdown-gpio=2

# sudo ../env/bin/python3 -m cProfile -s tottime main.py --led-gpio-mapping=adafruit-hat-pwm --led-rows=32 --led-cols=64 --led-slowdown-gpio=2