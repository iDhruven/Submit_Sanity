import os
import subprocess
import osascript

from SubmitProjectSettings import *
from SubmitMajorTag import *

from File import *

DEBUG_MODE=os.environ['DEBUG_MODE']


print ("------------------------------The MobileAssets Script Begins here--------------------------------------")

PROJECT_FQNAME = PROJECT + "-" + str(NEW_VERSION)
print(PROJECT_FQNAME)

print ("Building MobileAssets...")
os.system('cd MobileAssets | ./PopulateAssets.sh clean | ./PopulateAssets.sh macos')

FQ_MAPROJECT = MA_PROJECT + "-" + str(NEW_VERSION)
print(FQ_MAPROJECT)

print ("Submitting " + FQ_MAPROJECT + " to Speedwagon... (5 min, alert on completion)")
os.system('touch ../build/ma_submit.txt')

#---------------------------------------------------------------------------------------------------------------

if DEBUG_MODE == 'FALSE':
  os.system('xbs submitproject -version ${FQ_MAPROJECT} . Speedwagon')
else:
  os.system('xbs submitproject -noSubmit -version ${FQ_MAPROJECT} . Speedwagon')
 
os.system('SUBMISSION_STATUS=$? | echo ${SUBMISSION_STATUS}')

print (FQ_MAPROJECT, " submission")
subprocess.call(['sh', './test.sh'])


rest_command = """'display notification "{} Submitted!" with title "{}"'""".format(PROJECT_FQNAME,PROJECT_FQNAME)
os.system("osascript -e "+ rest_command)


#print (SUBMISSION_STATUS)

#os.system('''
#          if [ $SUBMISSION_STATUS -eq 0 ]; then        
#            echo "${GREEN_TEXT}successful${CLEAR_TEXT}."
#            osascript -e "display notification \"${FQ_MAPROJECT} Submitted!\" with title \"$PROJECT_FQNAME\""
#          else
#            echo "${RED_TEXT}failed${CLEAR_TEXT}. Scroll up to see why."
#            osascript -e "display notification \"${FQ_MAPROJECT} submission failed.\" with title \"$PROJECT_FQNAME\""
#          exit
#          fi
#          ''')
#    cd ..

#---------------------------------------------------------------------------------------------------------------

print ("------------------------------The MobileAssets Script Ends here--------------------------------------")
