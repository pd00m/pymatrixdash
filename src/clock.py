from datetime import date, time, datetime
from matrix import Matrix
from font import Font

class ClockScreen():
    def __init__(self, config, matrix):
        self.showDuration = config["screens"]["clockScreen"].get("showDuration")

        self.matrix = matrix
        self.font_small = Font(file = "CGpixel3x5.ttf", size = 5)
        self.font_big = Font(file = "mini_pixel-7.ttf", size = 30)
    
    def getShowDuration(self):
        return self.showDuration

    def draw(self):      
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%a %d. %b")    
        self.matrix.draw_text(["50%","17%"],text=current_date,fill=(50, 50, 50),font=self.font_small.font, align="center-center" )
        self.matrix.draw_text(["50%","60%"],text=current_time,fill=(50, 50, 50),font=self.font_big.font, align="center-center" )
