import os

os.system('printf "\e[31m------------The Submit Script Begins here------------------\e[0m\n"')

#print('\033[31m' + 'some red text')
#print('\033[39m') # and reset to default color

SUBMIT_VERSION=2
DEBUG_MODE=1

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)

if DEBUG_MODE == 1:
  os.system('printf ("\033[31mDEBUG MODE ENABLED\033[0m\n")

os.system('printf "\\e[31m------------The Submit Script Ends here------------------\\e[0m\\n"')
