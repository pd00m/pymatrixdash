import time
from threading import Timer
from itertools import cycle

# Base classes
from base import Base
from matrix import Matrix

# Screens
from clock import ClockScreen
from hello import HelloScreen

from weather import Weather

class Main(Base):

    def run(self): 
        frame = Matrix(self.matrix)

        self.screenCycle = cycle([ClockScreen(frame), HelloScreen(frame), Weather(frame)])
        self.currentScreen = next(self.screenCycle)
        self.next_screen()

        #weather = Weather(frame)
        #weather.parse()

        while True:
            time.sleep(0.1)  
            frame.clear()
            self.currentScreen.draw()
            frame.render()

    def next_screen(self):
        self.currentScreen = next(self.screenCycle)
        Timer(1, self.next_screen).start()
    

# Main function
if __name__ == "__main__":
    main = Main()
    if (not main.process()):
        main.print_help()


# sudo ../env/bin/python3 main.py --led-gpio-mapping=adafruit-hat-pwm --led-rows=32 --led-cols=64 --led-slowdown-gpio=2