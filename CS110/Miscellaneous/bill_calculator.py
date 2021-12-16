# Your Name
# Python For Scientists
# 
# A program that simulates a customer/server interaction

# Assign values to variables
guest_name = input('What is the guest name?')
entree_cost = float(input('What is the entree cost?'))
ap_cost = float(input('What is the appetizer cost?'))
tip = float(input('What percentage tip do yu want to leave (0.00)'))
tax_rate = .095;

# Calculate the tax and total bill
tax_owed = round(entree_cost*tax_rate + ap_cost*tax_rate, 2)
total_owed = round(entree_cost + ap_cost + tax_owed, 2)
totalwithtip_owed = round(total_owed + total_owed * tip, 2)

# Print the simulated conversation
print("Hello,", guest_name);
print("Your entree cost $", entree_cost, sep="");
print("Your appetizer cost $", ap_cost, sep="");
print("Including tax, your total bill is $", totalwithtip_owed,sep="");

