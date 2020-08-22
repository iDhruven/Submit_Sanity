
print ("------------The Submit Script Begins here------------------")

import os
os.system('echo "Hello World!"')
os.system('pip --version')

#print('\033[31m' + 'some red text')
#print('\033[39m') # and reset to default color

SUBMIT_VERSION=2
DEBUG_MODE=1

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)
print (""\e[31mHello\e[0m\n"")

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")

print ("------------The Submit Script Ends here------------------")
