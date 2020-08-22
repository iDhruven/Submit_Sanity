import os

os.system('printf "\e[31m------------The Submit Script Begins here------------------\e[0m\n"')

#print('\033[31m' + 'some red text')
#print('\033[39m') # and reset to default color

SUBMIT_VERSION=2
DEBUG_MODE=1

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")

os.system('printf "\\e[31m------------The Submit Script Begins here------------------\\e[0m\\n"')
