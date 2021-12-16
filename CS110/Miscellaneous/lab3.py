#--------------------------------
#TITLE:  Lab 03: Input and Type Conversion
#FILE: lab3.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 1/25/2021
#DATE SUBMITTED: 1/27/2021
#--------------------------------

# name = input('Enter your name: ');
# print('Hello,', name);
# print(type(name))

# x = input("Enter a number: ");
# y = input("Enter another number: ");
# z = x + y;
# print("The sum of", x, "and", y, "is", z);
# print("Twice", x, "is", 2*x);
# type_of_x = type(x);
# print("The variable x is of type: ", type_of_x);

# string_5 = "5";
# string_6 = "6";
# integer_5 = int(string_5);
# integer_6 = int(string_6);
# string_sum = string_5 + string_6;
# integer_sum = integer_5 + integer_6;
# print("Does",string_5,"plus",string_6,"equal",string_sum,"...");
# print("or does",integer_5,"plus",integer_6,"equal",integer_sum);

# side_length = int(input("Enter a number: "));
# text1 = "A square of side length";
# text2 = "has an area of";
# print(text1, side_length, text2, side_length**2);

# print("I ran " + str(26.2) + " miles." )

# guest_name = input('What is the guest name?')
# entree_cost = float(input('What is the entree cost?'))
# ap_cost = float(input('What is the appetizer cost?'))
# tip = float(input('What percentage tip do yu want to leave (0.00)'))
# tax_rate = .095;
#
# # Calculate the tax and total bill
# tax_owed = round(entree_cost*tax_rate + ap_cost*tax_rate, 2)
# total_owed = round(entree_cost + ap_cost + tax_owed, 2)
# totalwithtip_owed = round(total_owed + total_owed * tip, 2)
#
# # Print the simulated conversation
# print("Hello,", guest_name);
# print("Your entree cost $", entree_cost, sep="");
# print("Your appetizer cost $", ap_cost, sep="");
# print("Including tax, your total bill is $", totalwithtip_owed,sep="");

print('CONVERT FAHRENHEIT TO CELCIUS \n')
tempF = float(input('Enter a fahrenheit temp: '))
tempC = (tempF - 32) * (5/9)
outputMessage = 'Initial fahrenheit temp: ' + str(tempF) + '\nCalculated celcius temp: ' + str(tempC)
print(outputMessage)




