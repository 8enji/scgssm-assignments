##Prints a silly song
##Illustrates how to define and call a custom function

def funnyFruit(letter) :
    """ Create and print a silly message """
    message = letter + "pples and b" + letter + "n" \
        + letter + "n" + letter + "s"
    print(message)

##Main program
print("I like to eat, eat, eat...")
alphabet = ['a', 'b' , 'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i', 'j' , 'k', 'l', 'm', 'n' ,'o','p','q','r','s','t','u','v','w','x','y','z']
for character in alphabet:
    funnyFruit(character)
