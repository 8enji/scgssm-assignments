#--------------------------------
#TITLE:  Lab 01: print()
#FILE: lab1.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 1/11/2021
#DATE SUBMITTED: 1/12/2021
#DESCRIPTION: Learning how to use the print function and it's different operators
#--------------------------------

print('delete the hashtag before the problems at the end to see the code outputs')

def prob1():
    print('prob1')
    print('Hello World');
    print('Hello World')
    print('Hello', 'World');
    print('Hello', 'World', 'third');

def prob2():
    print('prob2')
    print  ( 'Hello' , 'World' )   ;
    print('Hello ','World');

def prob3():
    print('prob3')
    print('problem 3 is answered in the comments')
    #Print('Hi');
    #- does not work because print is capitalized. In python, the print function needs to be lowercase.
    #print(hi);
    # - does not work because hi is not inside apostrophes and is not a variable.

def prob4():
    print('prob4')
    print();
    print();

    print("I", "love", "coding!", sep="+");
    print("Two", "four", "six", "eight", sep=", ", end="; ");
    print("who do we appreciate?");

def prob5():
    print('prob5')
    print('She said \"Hello.\"')
     #use \ and then the character to include it
    print('She said \"Hello, have you said the word \'python\' yet today?\"')
     #use \ and then the character to include it
    print('this is a \ntest \tfor n and t')
     #\n creates a new line, and \t creates a tab

def quickcheck():
    print('quickcheck')
    print('spam', 'eggs', sep = '+')
    print('Yay! \nIt\'s summer!')

#1) a. there is no difference
#   b. Yes you can. the comma also creates a space.
#   c. Note to self - semi-colons are not needed, but they should still be added


#2) a. the space only makes a difference if it is inside the apostrophes
#   b. you can add a space before the apostrophe set, between the comma and the
#       apostrophe, after the apostrophe set, and before and after the parenthesis set

#3)
    #Print('Hi');
      #- does not work because print is capitalized. In python, the print function needs to be lowercase.
    #print(hi);
      # - does not work because hi is not inside apostrophes and is not a variable.

#4) a. if the print function is not given an argument, it prints a blank line
#   b. the sep argument sets the commas equal to something. Normally they would be spaces,
#       but in the example the sep argument sets the to plus signs. The end argument sets what the
#       end of the print function ends with. This can be used to make it so the print function does
#       not print to a new line

#4)
#   a. use \ and then the character to include it
#   b. use \ and then the character to include it
#   c. \n creates a new line, and \t creates a tab
'''what even is a triple quote string
o it is a comment
that you can eaisly span multiple
lines with'''
#   d. a triple-quote string is a way to create long multi line comments without having
#       to type hashtags on every line

#quick check!



#prob1()
#prob2()
#prob3()
#prob4()
#prob5()
quickcheck()