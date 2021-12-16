##Gets length and width from the user and calculates area
##Uses robust input technique
##Illustrates a funciton with a return value


def getNumber():
    """ Get a number from the user and return it """
    number = None;
    #prompt = input('How would you like me to prompt you to add an integer? ')
    while number == None:
        try :

            number = int(input(prompt));
        except ValueError :
            print("Not a valid input.");
    return number

##Main program
prompt = input('How would you like me to prompt you to add an integer? ')
x = getNumber();
y = getNumber();
print('If the length is', x, 'and the width is',y,\
    'then the area is',x*y);
