import os

print ("-----------The Submit Script Begins here------------------")

SUBMIT_VERSION=2
DEBUG_MODE=$DEBUG_MODE
print(os.environ['HOME'])

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")

print ("-----------The Submit Script Ends here------------------")
