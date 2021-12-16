from graphics import *

def main():
    infile=open('minion.ppm', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    print(line1, end = '')
    print(line2, end = '')
    print(line3, end = '')
    print(line4, end = '')

    dimen = line3.split()
    w = eval(dimen[0])
    h = eval(dimen[1])
    print(w, h , w * h * 3)

    mydata = infile.read()
    print(mydata)

    infile.close()

main()
