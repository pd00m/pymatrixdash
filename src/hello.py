from matrix import Matrix
from font import Font

class HelloScreen():
    def __init__(self, config, matrix):
        self.showDuration = config["screens"]["helloScreen"].get("showDuration")

        self.matrix = matrix
        self.font_big = Font(file = "mini_pixel-7.ttf", size = 20)

    def getShowDuration(self):
        return self.showDuration

    def draw(self):      
        self.matrix.draw_text(["50%","50%"],text="Hello :}",fill=(0, 50, 0),font=self.font_big.font, align="center-center" )
