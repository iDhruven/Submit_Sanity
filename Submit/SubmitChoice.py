import os

#ChoiceSelection

CHOICE=[os.environ['CHOICE']] 
print "You have selected :", CHOICE

H = 'H'
A = 'A'
B = 'B'
E = 'E'
I = 'I'
L = 'L'
M = 'M'
P = 'P'
T = 'T'
R = 'R'
H = [i for i in CHOICE if H in i]
A = [i for i in CHOICE if A in i]
B = [i for i in CHOICE if B in i]
E = [i for i in CHOICE if E in i]
I = [i for i in CHOICE if I in i]
L = [i for i in CHOICE if L in i]
M = [i for i in CHOICE if M in i]
P = [i for i in CHOICE if P in i]
T = [i for i in CHOICE if T in i]
R = [i for i in CHOICE if R in i]
