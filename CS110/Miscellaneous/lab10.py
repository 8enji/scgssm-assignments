#--------------------------------
#TITLE:  Lab 10: Lists (and Dictionaries)
#FILE: lab10.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 3/22/2021
#DATE SUBMITTED: 3/28/2021
#DESCRIPTION: Learning about lists and dictionaries
#--------------------------------

# from random import *
#
# torisGrades = [80, 95, 88, 73, 92];
# bensGrades = []
#
# for i in range(len(torisGrades)):
#     bensGrades.append(randint(50,100))
#
# print(bensGrades)



# torisGrades = [80, 95, 88, 73, 92];
# torisGrades.sort()
#
# n = len(torisGrades)
# median = 0
#
# if ((n % 2) == 0):
#     i = int(n/2)
#     median = (torisGrades[i - 1] + torisGrades[i]) / 2
# else:
#     i = int(n/2)
#     median = torisGrades[int(i +.5)]
# print(torisGrades)
# print(median)

# from random import *
#
# suits = ['S', 'C', 'H', 'D'];
# ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'];
# deck = [];
#
# for c in suits:
#     for r in ranks:
#         deck.append(r + c)
#
# print(len(deck))
# print(deck)
#
# top = len(deck) - 1
# def shuffle():
#     for i in range(len(deck)):
#         top = len(deck) - 1
#         randIndex = randint(0, 51)
#         ranCard = deck[randIndex]
#         topCard = deck[top]
#         deck[randIndex] = topCard
#         deck[top] = ranCard
#
#
# shuffle()
#
# print(len(deck))
# print(deck)
#
# j = eval(input('How many times would you like to use for the calculation? '))
# count = 0
# ace or club
# for k in range(j):
#     card = deck[randint(0, top)]
#     if card[1] == 'C' or card[0] == 'A':
#         count = count + 1

# pair
# for k in range(j):
#     shuffle()
#     card1 = deck[51]
#     card2 = deck[50]
#     if card1[1] == card2[1]:
#         count = count + 1
#
# print(count)
# percent = count / j
# print('Experimental Probability:', percent)

scores = {"Ben": 4.1, "Angie": 3.7, "Liz": 2.5, "Heather": 3.3}
# if 4.1 in scores.values():
#     print('True')
# else:
#     print('False')
scores['String'] = 'int'
print(scores)