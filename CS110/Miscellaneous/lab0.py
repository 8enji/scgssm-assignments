#--------------------------------
#   Name: Ben Charest
#   Course: CSC110, semester, Python for Scientists
#   Date: 1/4/2021
#   Filename lab0.py
#   Peers: N/A
#   References: geeksforgeeks.org , how to print without newline
#--------------------------------

#### Introduction
print("Step 0: Answer\n")

#### Step #0 - On which device did you install Thonny?
print("I chose not to install Thonny, but rather use pyCharm. I installed pyCharm on my pc.")

print("Step 1: Answer\n")
#### Step #1
name = "Jordan"
scgiik = "Smith College"
age = 33
year = 2020
year_born = year - age
print(name, "goes to", scgiik, "and is", age, "years old ")
print(name, "was born in", year_born)

print("Step 2: Answer\n")
#### Step #2
word1 = "hello "
word2 = "there!"
print(word1 * 4 + word2)
word1 = "hello"
word2 = "there! "
print(word1, word2 * 5 + word1)
word2 = "there!"


print("Step 3: Answer\n")
#### Step #3

print((word1 + word2) * 5)

print("Step 4: Answer\n")
#### Step #4
for name in ["Aleah", "Belle", "Chen", "Ben", "Jo", "Sarah"]:
    print(name, end = " ")
#for name in ["Aleah", "Belle", "Chen"]:
#    print(name, "-" * len(name))



print(" ")
print("Step 5: Answer\n")
#### Step #5
for name in ["Aleah", "Belle", "Chen"]:
    print(name)
    print('-' * len(name))

print("Step 6: Answer\n")
#### Step #6
for name in ["Aleah", "Belle", "Chen"]:
    print('-' * len(name))
    print(name)
    print('-' * len(name))
    print(' ')
print("Step 7: Answer\n")
#### Step #7

for name in ["Julia Child", "Gloria Steinem"]:
    nameLen = len(name)
    nameLen4 = len(name) + 4
    nameLen2 = len(name) + 2
    x = 10
    bar1 = '-' * x
    bar2 = bar1 + '|'
    bar3 = '<' + bar1 + '>'
    bar4 = '-' * nameLen
    bar5 = bar4 + '-' * 4

    print(bar5)
    print("|", name, "|")
    print(bar5)
    print("nameLen =", nameLen)
    print('nameLen4 =', nameLen4)
    print('nameLen2 =', nameLen2)
    print('x =', x)
    print('bar1 = ', bar1)
    print('bar2 =', bar2)
    print('bar3 = ', bar3)
    print('bar4 = ', bar4)
#When I changed the name, nameLen changes. This makes it so every single variable dependent on nameLen also chnages.

print("Step 8: Answer\n")
#### Step #8
# One issue I am concerned about is the morals in the Tech World.
# Many big companies value profits over being morally correct.
# An example of this being tech companies such as Microsoft developing AI
# software that they are selling to the US military that will be used to create
# automated drones for the purpose of killing. The reason this is a problem is
# because it shows how big tech companies will value profit over human lives.
# The lack of morals of these big companies could also lead to worse situations
# in the future.


print("Bonus\n")
#### Bonus
for name in ['Aleah', 'Belle', 'Chen']:
    barLength = len(name) + 2
    bar = '-' * barLength
    print('+' + bar + '+')
    print('|', name, '|')
    print('+' + bar + '+')

for name in ['Ali', 'Balwin', 'Chen']:
        bar = '-' * 8
        nameLen = len(name)
        x = 6 - nameLen
        print('+' + bar + '+')
        print('|', name + ' ' * x, '|')
        print('+' + bar + '+')
