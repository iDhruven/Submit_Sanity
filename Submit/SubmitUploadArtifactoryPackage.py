import os
import shutil

from Submit import *
from SubmitProjectSettings import *
from SubmitMajorTag import *

DEBUG_MODE=os.environ['DEBUG_MODE']
NEW_VERSION=os.environ['NEW_VERSION']

print (NEW_VERSION)

print ("Ready to upload to", ARTIFACTORY_URL)
ARTIFACTORY_PATH= ARTIFACTORY_URL + "/libs-release-local/com/apple/csl/morphun/" + str(NEW_VERSION)
TGZ_NAME="morphun-"+ str(NEW_VERSION) + "-mac.tgz"

print("Artifactory Path:", ARTIFACTORY_PATH)
print("TGZ Name:", TGZ_NAME)

ARTIFACTORY_USERNAME=os.environ['ARTIFACTORY_USERNAME']
ARTIFACTORY_PASSWORD=os.environ['ARTIFACTORY_PASSWORD']

print ("Artifactory Username:", ARTIFACTORY_USERNAME)
print ("Artifactory Password:", ARTIFACTORY_PASSWORD)

if 1 == 0:
#if curl --head -f -s -u $ARTIFACTORY_USERNAME:$ARTIFACTORY_PASSWORD $ARTIFACTORY_PATH/$TGZ_NAME > /dev/null:
    print ("Version " + str(NEW_VERSION) + " already exists in artifactory. Skipping upload.")
else:
  
#------------------------------------------------------------------#
  print ("Compiling and preparing macOS distributable package...")

  os.system('make clean > /dev/null')
  Dest = "build/" + TGZ_NAME
  print (Dest)
  #shutil.move('build/morphun-snapshot-mac.tgz', Dest)

#------------------------------------------------------------------#

  print ("Uploading...")
            
            
  if DEBUG_MODE == 'TRUE':
    #curl -X PUT -f -u $ARTIFACTORY_USERNAME:$ARTIFACTORY_PASSWORD --upload-file build/$TGZ_NAME -i $ARTIFACTORY_PATH > /dev/null
    #UPLOAD_STATUS=$?
    print ("Upload Status Q")
  else:    
    UPLOAD_STATUS=0
    print (UPLOAD_STATUS)
  
  print ("Upload of",TGZ_NAME)
  if UPLOAD_STATUS == 0:
    print ("SUCCEEDED!")
  else:
    print ("FAILED!")


