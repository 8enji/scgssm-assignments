# File: chaos.py
# A simple program illustrating chaotic behavior


def main():
        print('This program illustrates a chaotic function')
        #eval translates string to int, input is scanner
        x = eval(input('Enter a number between 0 and 1: '))
        # for loop repeats 100 times
        for i in range(100):
            x = 3.9 * x * (1- x)
            print(x)

main()