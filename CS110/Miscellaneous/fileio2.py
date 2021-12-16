## FILE I/O:
from graphics import *
import random

def main():
    print('<<< MY FILE IO PGM >>>')

    #Initialize
    fname = 'minion.ppm'
    infile = open(fname, 'r')
    outfile = open('myImage.ppm', 'w')

    #Handle metadata
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    print(line1, file = outfile)
    print('#THIS IS MY IMAGE I MADE IN PYTHON! - BCC', file = outfile)
    print(line3, file = outfile)
    print(line4, file = outfile)

    #Sanity Check
    print(line1, end='')
    print(line2, end='')
    print(line3, end='')
    print(line4, end='')

    dimlst = line3.split()
    w = eval(dimlst[0])
    h = eval(dimlst[1])
    print(dimlst, w , h , "number of RGB values is: ", w * h * 3)

    win = GraphWin(fname, w, h)
    img = Image(Point(w//2, h//2), '')

    imgX = 0
    imgY = 0

    #Process
    imgData = infile.read()
    imgDataLst = imgData.split()
    print(len(imgDataLst), '\n', imgDataLst[:26])

    pixpos = 0

    for r in range(0, h):
        for c in range(0, w):

            rd = eval(imgDataLst[pixpos])
            grn = eval(imgDataLst[pixpos + 1])
            bl = eval(imgDataLst[pixpos + 2])
            pixpos += 3
            #
            # tmp = rd
            # rd = grn
            # grn = bl
            # bl = tmp

            rd = random.randint(0,255)
            grn = 255 - grn
            bl = 255 - bl

            img.setPixel(imgX, imgY, color_rgb(rd,grn,bl))
            print(rd, grn, bl, file = outfile)
            imgX += 1
        imgY += 1
        imgX = 0
        print('Working...', imgY)

    img.draw(win)

    #Terminate
    win.getMouse()
    win.close()
    infile.close()
    outfile.close()

main()