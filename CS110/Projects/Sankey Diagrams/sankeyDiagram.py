# Ben Charest
# CSC110, semester, Python for Scientists
# 4 / 18 / 2021
# Reads data from a file and creates a sankey diagram to represent the data

# imports
# zelle's graphics used for window, draw, shape functions etc
# math used for .pi
from graphics import *
from math import *

# help function - returns nothing
''' This function gives the user input on what the program is and how they can use it.
    It is called when the user inputs an incorrect file or inputs --help '''
def help():
    print('Hello! You are likely seeing this message because you need help.'
          '\nDo not worry, this program is not too hard to understand. First,'
          '\nyou want to input a txt file that includes data you want to turn into a'
          '\nsankey diagram. What is a sankey diagram you may ask? Well, a sankey '
          '\ndiagram is a helpful way to represent data. It represents data as a '
          '\nsource and then visually divides it into categories. To learn more '
          '\nabout sankey diagrams, please visit https://en.wikipedia.org/wiki/Sankey_diagram')


# make dictionary function - returns dictionary
''' This function creates the basic dictionary that is used throughout the program. 
    It sets the string values to the keys and the ints to the values'''
def  makeDictionary(fileName):
    # initialize
    # file processing
    infile = open(fileName, 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    line6 = infile.readline()
    line7 = infile.readline()
    line8 = infile.readline()
    line9 = infile.readline()
    line10 = infile.readline()

    # removes the newline character from the lines
    line4 = line4.rstrip('\n')
    line5 = line5.rstrip('\n')
    line6 = line6.rstrip('\n')
    line7 = line7.rstrip('\n')
    line8 = line8.rstrip('\n')
    line9 = line9.rstrip('\n')
    line10 = line10.rstrip('\n')

    # creates a string that combines all the lines with commas
    dictStr = line4 + "," + line5 + "," + line6 + "," + line7 + "," + line8 + "," + line9 + "," + line10

    # splits the comma on every comma into a list
    dictList = dictStr.split(',')

    # removes and possible blank lines
    while ('' in dictList):
        dictList.remove("")

    # creates the dictionary
    dictionary = {}
    n = 0
    i = int(len(dictList) / 2)

    # initiates the keys and the values
    for numbers in range(i):
        dictionary[dictList[n]] = float(dictList[n + 1])
        n = n + 2

    # returns the dictionary
    return dictionary

# draw sankey diagram function - returns nothing
''' This is the function of the program that does most of the work. It calculates the 
    dimensions for every polygon and draws most of the as well. It also handles the 
     color aspects '''
def drawSankey(window, dictionary):
    # gets all the values from the dictionary and calculates the sum
    values = dictionary.values()
    totalFlow = sum(values)

    # creates a list with rgb values for twelve differnt colors
    colorList = (255,0,0), (255, 64, 0), (255,191,0), (255,255,0), (191, 255, 0), (64,255,0), (0,255,191), (0,128,255), (0,0,255), (128,0,255), (255,0,255), (255,0,102)

   # rgb value for the source color (purple)
    sourceColor = 64, 0, 255

    # possible amount of pixels
    pixels = 600 - (len(dictionary) - 1) * 10

    # pixels per unit of total flow
    ppf = pixels / totalFlow

    # pixel height of source bar
    heightSource = totalFlow * ppf

    # creates a dictionary with all the heights of the keys
    heightDict = dictionary

    for key in heightDict:
        heightDict[key] = heightDict[key] * ppf

    # value used to calculate source bar y values
    x = (900 - pixels) / 2

    # source rectangle creation
    sourceRect = Rectangle(Point(150, x), Point(180, 900 - x))
    sourceRect.setFill(color_rgb(sourceColor[0], sourceColor[1], sourceColor[2]))
    sourceRect.draw(window)

    # value in between flows
    space = (600 - pixels) / len(dictionary)

    # variables used in following for loop to create flow rectangles
    y = 150
    z = 150
    n = 0

    # for loop that iterates through height Dictionary keys
    for key in heightDict:

        # percent value for each flow (extra credit)
        percent = round((((heightDict[key] / ppf) / totalFlow) * 100), 1)

        # rectangle y values
        y = z + space
        z = y + heightDict[key]

        # rectangle creation
        rect = Rectangle(Point(720, y), Point(750, z))

        # line creation (used for black outlines
        line = Line(Point(750, y), Point(750, z))
        lineTop = Line(Point(720, y), Point(750, y))
        lineBot = Line(Point(720, z), Point(750, z))

        # poly = Polygon(Point(180, x), Point(720, y), Point(720, z), Point(180, x + heightDict[key]))

        # iterates through the color list, also turns tuple values into list values
        color = colorList[n]
        color = list(color)
        n = n + 1

        # for loop used to create the small rectangles, step value = how many rectangles
        step = 500
        for j in range(step):

            # ratio based off how close to right side
            ratio = j / step

            # ratio modified used to create sin curve for the flows
            ratio2 = ratio * pi - pi / 2
            ratio2 = (sin(ratio2) + 1) / 2

            # points used for rectangles
            point1 = Point((180 + (540 * ratio)), (x + ((y - x) * ratio2)))
            point2 = Point((181 + (540 * ratio)), (x + heightDict[key] + ((y - x) * ratio2)))

            # lines used for black outlines
            line1 = Line(point1, Point((181 + (540 * ratio)), (x + ((y - x) * ratio2))))
            line2 = Line(point2, Point((179 + (540 * ratio)), (x + heightDict[key] + ((y - x) * ratio2))) )

            # creation of rectangle
            rectangle = Rectangle(point1, point2)

            # rgb modification to create fade
            r = (int(color[0] * ratio) + int((1 - ratio) * sourceColor[0]))
            g = (int(color[1] * ratio) + int((1 - ratio) * sourceColor[1]))
            b = (int(color[2] * ratio) + int((1 - ratio) * sourceColor[2]))

            # set color and draw rectangle and lines
            rectangle.setOutline(color_rgb(r, g, b))
            rectangle.draw(window)
            line1.draw(window)
            line2.draw(window)

        # modify x for next iteration of loop
        x = x + heightDict[key]

        # creation of flow labels and percentage label
        dLabel = Text(Point(800, y + ((z - y) / 2)), key)
        pLabel = Text(Point(875, y + ((z - y) / 2)), str(percent) + '%')

        # poly.setFill('black')
        # poly.draw(window)

        # colors and drawing
        rect.setFill(color_rgb(color[0], color[1], color[2]))
        rect.setOutline(color_rgb(color[0], color[1], color[2]))
        rect.draw(window)
        line.draw(window)
        lineTop.draw(window)
        lineBot.draw(window)
        dLabel.draw(window)
        pLabel.draw(window)

# main function
''' This is the main function of the program. It is used to test all the other 
    functions of the program. It also serves as the users hub of the program.'''
def main():
    # input
    # user input
    fileName = input('Enter the name of the data file you want to diagram: (enter --help for help) ')

    # calls the help function if user needs
    if fileName == '--help':
        help()
        quit()

    # error catching just in case user inputs incorrect file
    try:
        infile = open(fileName, 'r')
    except FileNotFoundError:
        print("file not found")
        help()
        exit()

    # input file reading
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # initiates graphic window
    win = GraphWin(fileName, 900, 900)
    win.setBackground("gray")

    # creates and draws title
    title = Text(Point(450, 120), line2)
    title.setSize(20)
    title.setStyle('bold')
    title.draw(win)

    #creates and draws source label
    label = Text(Point(75, 450), line3)
    labelp = Text((Point(75, 475)), '100%')
    label.draw(win)
    labelp.draw(win)

    # creates and draws file label
    fileLabel = Text(Point(85, 880), fileName)
    fileLabel.draw(win)

    # creates and draws name and date
    name = Text(Point(800, 880), "Ben Charest 04/18/2021")
    name.draw(win)

    # calls the makeDictionary function for the user specified file
    dictionary = makeDictionary(fileName)

    # process and output
    # calls the drawSankey diagram - uses the created window and the user inputted file
    drawSankey(win, dictionary)

    # saves the diagram to a .ps file name 'fileName'.ps
    win.postscript(file=fileName[:-4] + '.ps', colormode='color')

    # terminate
    # closes and terminates
    win.getMouse()
    win.close()
    infile.close()

# main function calling
if __name__ == '__main__':
    main()