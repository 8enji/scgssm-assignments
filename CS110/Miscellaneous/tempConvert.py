#tempConvert.py
#A program to convert Celsius temps to Fahrenheit
#by: Ben Charest
def main():
    print('CONVERT CELSIUS TO FAHRENHEIT \n')
    x = eval(input('Enter a celsius temp to convert it to fahrenheit: '))
    y = ((9/5) * x) + 32
    print('Celcius:', x, '\nFahrenheit:', y)

main()