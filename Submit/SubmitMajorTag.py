import os

from SubmitProjectSettings import *

VERSION=os.environ['VERSION'] 
New_Major_Version = int(VERSION)
print ("The New Version is ----->" ,(New_Major_Version + 1))
#print ("TAG HERE ---->", VERSION)
#print (PROJECT)
#os.system ('git tag -l | grep "Morphun-" | sort -n | tail -1')
