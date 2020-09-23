import os

from SubmitProjectSettings import *

VERSION=os.environ['VERSION'] 
Float_Version = float(VERSION)

NEW_VERSION = Float_Version + 1

print ("#The New Version is ----->" ,(NEW_VERSION))
print ("NEW_VERSION =", NEW_VERSION)

