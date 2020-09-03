import os

from SubmitProjectSettings import *

VERSION=[os.environ('VERSION')] 
print ("TAG HERE ---->", VERSION)
print (PROJECT)
os.system ('git tag -l | grep "$PROJECT-"')
