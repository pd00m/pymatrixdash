from PIL import ImageFont

class Font():
    def __init__(self, file, size):
        self.file = file
        self.size = size
        self.font = ImageFont.truetype("../assets/fonts/" + file, size)



