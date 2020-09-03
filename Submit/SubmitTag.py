import os

from SubmitProjectSettings import *

print ("TAG HERE ---->", VERSION)
print (PROJECT)
os.system ('git tag -l | grep "$PROJECT-"')
