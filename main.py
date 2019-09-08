from yeelight import Bulb
import pyscreenshot as ImageGrab
from PIL import Image
leftBulb = Bulb("192.168.0.234")
rightBulb = Bulb("192.168.0.38")
leftBulb.turn_on()
rightBulb.turn_on()


def averageRGB(image):
    pixels = screen.load()
    width = image.size[0]
    height = image.size[1]
    averageR = 0
    averageG = 0
    averageB = 0

    for i in range(width):
        for j in range(height):
            averageR += pixels[i,j][0]
            averageG += pixels[i,j][1]
            averageB += pixels[i,j][2]
    area = width * height
    averageR = averageR / area
    averageG = averageG / area
    averageB = averageB / area

    return averageR, averageG, averageB

if __name__ == "__main__":
    leftBulb.start_music()
    rightBulb.start_music()
    while(True):
        screen = ImageGrab.grab()
        rgb = averageRGB(screen)
        leftBulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))
        rightBulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    leftBulb.stop_music()
    rightBulb.stop_music()

    
