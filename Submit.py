import os

os.system("cls")

r = "\u001b[33m"
print ("------------The Submit Script Begins here------------------")

print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color

SUBMIT_VERSION=2
DEBUG_MODE=1

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)

if DEBUG_MODE == 1:
  print 'r + "DEBUG MODE ENABLED"'

print ("------------The Submit Script Ends here------------------")
