from matrix import Matrix
from font import Font

class ScrollScreen():
    def __init__(self, config, matrix):
        self.showDuration = config["screens"]["scrollScreen"].get("showDuration")

        self.matrix = matrix
        self.font_big = Font(file = "mini_pixel-7.ttf", size = 40)
        self.setText("Hello Matrix :)")
        
    def getShowDuration(self):
        return self.showDuration

    def setText(self, text):
        self.text = text
        self.width = self.matrix.get_textSize(font=self.font_big.font, text=text)
        self.pos = self.matrix.width

    def draw(self):
        self.pos -= 1
        if (self.pos + self.width < 0):
                self.pos = self.matrix.width

        self.matrix.draw_text([self.pos,"50%"],text=self.text,fill=(0, 50, 0),font=self.font_big.font, align="left-center" )
