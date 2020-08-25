import os
import turtle
import pyfiglet 

import SubmitHelp
import SubmitLogo

from SubmitProjectSettings import *

print ("------------------------------The Submit Script Begins here--------------------------------------")

SUBMIT_VERSION=2
DEBUG_MODE=os.environ['DEBUG_MODE']

print "Submit script version:", SUBMIT_VERSION
print "Debug Mode:", DEBUG_MODE

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")
  
# Files 
GIT_IGNORE=".gitignore"
SUBMIT_IGNORE=("gradle/wrapper/gradle-wrapper.jar")

# Reset in case getopts has been used previously
OPTIND=1

# getopts
RESUBMIT=0
FULL_SUBMIT=1
PROJECT_SUBMIT=0
INIT_SUBMIT=0
TAG_SUBMIT=0
ARTIFACTORY_SUBMIT=0
MOBILE_ASSETS_SUBMIT=0
PYTHON_MORPHUN_SUBMIT=0
RELEASE_EMAIL_SUBMIT=0

#Choice Selection
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

if CHOICE == H:
  SubmitHelp.print_help()
if CHOICE == A:
  print ("Full Submission Script comes here!")
  FULL_SUBMIT=1
if CHOICE == B:
  print "Submit ", PROJECT ,"to B&I Script comes here!"
  PROJECT_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == E:
  print ("Sending Release Email Script comes here!")
  RELEASE_EMAIL_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == I:
  print ("Initialize Submission Script comes here!")
  INIT_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == L:
  print ("Submit Python Morphun Script comes here!")
  PYTHON_MORPHUN_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == M:
  print ("Submit Mobile Assests Script comes here!")
  MOBILE_ASSETS_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == P:
  print ("Submit macOS Artifactory Package Script comes here!")
  ARTIFACTORY_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == T:
  print ("Tag Submission and push to GitHub Script comes here!")
  TAG_SUBMIT=1
  FULL_SUBMIT=0
if CHOICE == R:
  print ("Resubmit Script comes here!")
  RESUBMIT=1
           
#Print Logo  
python3 SubmitLogo.py



print ("--------------------------------The Submit Script Ends here-------------------------------------------")
