#--------------------------------
#TITLE:  PROGRAM: Are you Ready?
#FILE: HiddenImages.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 3/7/2021
#DATE SUBMITTED: 3/7/2021
#DESCRIPTION: Program to decrypt five different images using five different methods
#--------------------------------

# imports
import math
import random
from graphics import *

# first decryption algorithm function
''' used to decrypt the first image. Multiples the red value by 10, and
    then sets each of the rgb values to the red value. This makes it grayscale'''
def decryptA01(rd, grn, bl):
    # multiply the red value by 10
    rd *= 10

    # set the rgb values to the new red value (this makes it grayscale)
    return rd, rd, rd


# second decryption algorithm function
''' used to decrypt the second image. Sets the red value to 0 and 
    multiplies  the red and green values by 20'''
def decryptA02(rd, grn, bl):
    # set red value to 0, this removes the noise
    rd = 0

    # multiply blue and green by 20
    grn *= 20
    bl *= 20

    # return the new rgb values
    return rd, grn, bl


# third decryption algorithm function
''' used to decrypt the third image. If the blue si less than 16, it 
    multiplies it by 16. If not, it sets it to 255.'''
def decryptA03(rd, grn, bl):
    # if blue is less than 16, multiply it by 16
    if (bl < 16):
        bl *= 16
    # if it is 16 or greater, set it to 255
    else:
        bl = 255

    # set all the rgb values to the new blue value and return them
    return bl, bl, bl


# fourth decryption algorithm function
''' used to decrypt the fourth image. uses the chinese remainder theorem'''
def decryptA04(rd, grn, bl):
    # set the red value using the formula below. This is the chinese remainder theorem
    rd = (rd*85 + grn*51 + bl*120) % 255

    # set all the rgb values to the new red value and return them
    return rd, rd, rd


# fifth decryption algorithm function
''' used to decrypt the fifth image. uses binary conversions.'''
def decryptA05(rd, grn, bl):
    # converts red value to binary
    byte = format(rd, '08b')
    # takes the last four values from the binary value and store it in a new variable
    last4 = byte[4:]
    # creates a new variable with the previous values at the first four and the last four as 0000
    newByte = last4 + "0000"

    # converts the binary to the new red value
    rd = int(newByte, 2)

    # repeats the same formula but for the green value
    byte = format(grn, '08b')
    last4 = byte[4:]
    newByte = last4 + "0000"

    grn = int(newByte, 2)

    # repeats the same formula but for the blue value
    byte = format(bl, '08b')
    last4 = byte[4:]
    newByte = last4 + "0000"

    bl = int(newByte, 2)

    # returns the new rgb values
    return rd, grn, bl



# definition of main function
''' this is the main function. it runs and decrypts the images based 
    off the previous algorithms and user inputs'''
def main():
    # initialization
    fileName = None
    algorithm = None
    imgX = 0
    imgY = 0

    # input
    # prompt user inputs for filename and algorithm
    fileName = input('Enter the name of the image file you want to decode: ')
    algorithm = eval(input('What decryption algorithm do you want to use (1-5): '))

    # format the output file name correctly
    outputFileName = fileName[:8] + '_OutA0' + str(algorithm) + '.ppm'

    # open the files to read and right
    infile = open(fileName, 'r')
    outfile = open(outputFileName, 'w')

    # read the metadata
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    # processing
    # print the metadata in the output file
    print(line1, file = outfile)
    print('# Benjamin Charest 03/07/2021', file = outfile)
    print(line3, file = outfile)
    print(line4, file = outfile)

    # split the line 3 of the meta data and set it to the dimensions
    dimlst = line3.split()
    w = eval(dimlst[0])
    h = eval(dimlst[1])

    # create the input and output windows using Zelle's graphics
    inputWin = GraphWin('INPUT', w, h)
    outputWin = GraphWin('OUTPUT', w, h)

    # set blank images into the windows
    inputImg = Image(Point(w // 2, h // 2), '')
    outputImg = Image(Point(w // 2, h // 2), '')

    # read the rest of the input file and split it into a list
    imgData = infile.read()
    imgDataLst = imgData.split()

    # initialize pixpos variable and set it to 0
    pixpos = 0

    # use a nested for loop to go through all the pixel values
    # height for loop
    for r in range(h):
        # width for loop
        for c in range(w):

            # set the rd, grn, bl variables equal to their respective value
            # from the input file
            rd = eval(imgDataLst[pixpos])
            grn = eval(imgDataLst[pixpos + 1])
            bl = eval(imgDataLst[pixpos + 2])

            # if statements to determine what algorithm to use
            if algorithm == 1:
                rgb = decryptA01(rd, grn, bl)
            if algorithm == 2:
                rgb = decryptA02(rd, grn, bl)
            if algorithm == 3:
                rgb = decryptA03(rd, grn, bl)
            if algorithm == 4:
                rgb = decryptA04(rd, grn, bl)
            if algorithm == 5:
                rgb = decryptA05(rd, grn, bl)

            # set new variables equal to the new rgb values
            rd2 = rgb[0]
            bl2 = rgb[1]
            grn2 = rgb[2]

            # add 3 to the pixpos variable so it moves on
            pixpos += 3

            #set the inputImg pixels to the original rgb values
            inputImg.setPixel(imgX, imgY, color_rgb(rd, grn, bl))

            # set the outputImg pixels to the new rgb values
            outputImg.setPixel(imgX, imgY, color_rgb(rd2, grn2, bl2))

            # print the new values into the outfile
            print(rd2, grn2, bl2, file=outfile)

            # add one to img x
            imgX += 1
        #add one to imgY
        imgY += 1
        # set imgX back to 0 so it starts on the new row
        imgX = 0
        # give the user a status update
        print('Working...', imgY)

    # output
    # draw the output and input images
    inputImg.draw(inputWin)
    outputImg.draw(outputWin)


    # close the windows once you click
    inputWin.getMouse()
    inputWin.close()
    outputWin.getMouse()
    outputWin.close()
    infile.close()
    outfile.close()

# call the main function
main()

# terminate

