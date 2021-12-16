#--------------------------------
#TITLE:  Lab 09: For loop and range
#FILE: lab9.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 3/9/2021
#DATE SUBMITTED: 3/9/2021
#DESCRIPTION: Learning about for loops and ranges
#--------------------------------

#I did all the code is this file instead of creating seperate ones

# evens_2_to_20 = range(2,22,2)
# for ii in evens_2_to_20 :
#     		print(ii)

# for ii in range(2,22,2) :
#     		print(ii)

# for ii in range(0,10001,5) :
#     		print(ii)

# for ii in range(5000,-200,-6):
#     print(ii)

# squares = ()
# for ii in range(1,11) :
#    	squares = squares + (ii*ii,)
#
# print(squares)

# runs = (2, 3, 5, 6)
# total = 0
# for ii in range(0,len(runs)) :
#     total = total + runs[ii]
#
# average = total/len(runs)
# print(average)

# text = "Hello my name is Benjamin Carter Charest!"
# special_letter = 'e'
# ocurrences = 0
# for ii in range(len(text)) :
#     print(ii, text[ii])
#     if (text[ii] == special_letter):
#         ocurrences += 1
#
# print("The letter '",special_letter,"' ocurrs ",ocurrences," times in the text:", sep="")
# print(text)

# crazy_list = ('hi', 42, True, (1, 3, 5), 1/4)
# for element in crazy_list :
#      print(element)

# text = "Here is some text. It is boring. Replace it with your own text."
# special_letter = 'e';
# ocurrences = 0;
# for letter in text:
#     print(letter)
#     if (letter == special_letter) :
#        ocurrences += 1;
#
# print("The letter",special_letter,"ocurrs",ocurrences,"times in the text:");
# print(text);

# MAX = 10
# for ii in range(1, MAX+1):
#      for jj in range(1, ii+1) :
#         print(ii,'\t',end = "");
#      print();

fib = (0, 1, 1)
for i in range(2,100):
    fib = fib + (fib[i] + fib [i-1],)

print(fib)




