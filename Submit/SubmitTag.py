import os

from SubmitProjectSettings import *

print ("TAG HERE")
print (PROJECT)
os.system ('git tag -l | grep "$PROJECT-"')
