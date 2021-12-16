#--------------------------------
#TITLE:  Lab 08: Tuples and Strings
#FILE: lab8.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 3/1/2021
#DATE SUBMITTED: 3/1/2021
#DESCRIPTION: Learning about tuples and strings, and how to use them


Mariners_runs = (10, 8, 8, 2, 3, 3, 5, 0, 6, 1)
Opponents_runs = (3, 5, 2, 3, 1, 6, 3, 2, 4, 3)
#
# w, l, d = 0, 0, 0

# for i in range(10):
#     if(Mariners_runs[i] > Opponents_runs[i]):
#         w += 1
#
#     if (Mariners_runs[i] < Opponents_runs[i]):
#         l += 1
#
#     if (Mariners_runs[i] == Opponents_runs[i]):
#         d += 1
#
# print('Wins / Losses / Draws:', w, '/', l, '/', d)

scores = [(10,3), (8,5), (8, 2), (2, 3), (3, 1), (3,6 ), (5, 3), (0, 2), (6, 4), (1, 3)]
print(scores[0][0])
print(scores[6][1])