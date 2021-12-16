# FILE I/O:
from graphics import *
import random

def main():
    print('<<< MY FILE IO PGM >>>')

    #Initialize
    fname = 'scgssm800x531.ppm'
    infile = open(fname, 'r')

    fname2 = 'minion.ppm'
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
    # print(line1, end='')
    # print(line2, end='')
    # print(line3, end='')
    # print(line4, end='')

    dimlst = line3.split()
    w = eval(dimlst[0])
    h = eval(dimlst[1])
    print(dimlst, w , h , "number of RGB values is: ", w * h * 3)

    win0 = GraphWin(fname, w, h)
    win1 = GraphWin(fname2, w, h)
    win1 = GraphWin("myImage.ppm OUTPUT FILE--CLICK TO EXIT", w, h)

    img0 = Image(Point(w // 2, h // 2, ''))
    img1 = Image(Point(w // 2, h // 2, ''))
    img = Image(Point(w // 2, h // 2, ''))

    imgX = 0
    imgY = 0

    # Process

    imgData0 = infile0.read()
    imgDataLst0 = imgData0.split()
    print(len(imgDataLst0), '\n', imgDataLst0[:26])

    imgData1 = infile1.read()
    imgDataLst1 = imgData1.split()
    print(len(imgDataLst1), '\n', imgDataLst1[:26])

    imgData2 = infile2.read()
    imgDataLst2 = imgData2.split()
    print(len(imgDataLst2), '\n', imgDataLst2[:26])

    pixpos = 0

    for r in range(0, h):
        for c in range(0, w):
            rd = eval(imgDataLst[pixpos])
            grn = eval(imgDataLst[pixpos + 1])
            bl = eval(imgDataLst[pixpos + 2])

            rd2 = eval(imgDataLst2[pixpos])
            grn2 = eval(imgDataLst2[pixpos + 1])
            bl2 = eval(imgDataLst2[pixpos + 2])

            pixpos += 3

            if(grn2 > 200 and rd2 < 20 and bl2 < 20):
                r = rd
                g = grn
                b = bl
            else:
                r = rd2
                g = grn2
                b = bl2

            # r = rd
            # g = grn
            # b = bl
            #
            # rd = random.randint(0, 255)
            # grn = 255 - grn
            # bl = 255 - bl

            img0.setPixel(imgX, imgY, color_rgb(rd, grn, bl))
            img1.setPixel(imgX, imgY, color_rgb(rd2, grn2, bl2))
            img.setPixel(imgX, imgY, color_rgb(r, g, b))
            print(r, g, b, file=outfile)
            imgX += 1
        imgY += 1
        imgX = 0
        print('Working...', imgY)
    img0.draw(win)
    img1.draw(win)
    img.draw(win)

    # Terminate
    win.getMouse()
    win.close()
    infile.close()
    outfile.close()


main()