##Program to explore scope

def what_is_accessible(parameter_in_function) :
    global message_in_main;
    """ Helper function to explore variable scope """
    print("First print in function: ", parameter_in_function);
    parameter_in_function += "More important information.";
    print("Second print in function: ",parameter_in_function);
    message_created_in_function = "...and don't foget this information.";
    print("Third print in function: ", message_created_in_function);
    print("Fourth print in function:", message_in_main);
    message_in_main = 'test'

    return message_created_in_function;

#"Main program" to explore scope of variables with functions
message_in_main = "Important information.";
print("First print in main:", message_in_main);
value_returned_from_function = what_is_accessible(message_in_main);
print("Second print in main:", value_returned_from_function);
print("Third print in main:", message_in_main);
# try:
#     print(parameter_in_function);
# except NameError:
#     print("The parameter name is not valid back in the main program.")
#
# try:
#     print(message_created_in_function);
# except NameError:
#     print("The parameter name is not valid back in the main program.")
