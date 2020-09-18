import os

from SubmitProjectSettings import *
from SubmitMajorTag import *

print ("Building MobileAssets...")
os.system('cd MobileAssets | ./PopulateAssets.sh clean | ./PopulateAssets.sh macos')

FQ_MAPROJECT = MA_PROJECT + "-" + str(New_Version)
print(FQ_MAPROJECT)

print ("Submitting " + FQ_MAPROJECT + " to Speedwagon... (5 min, alert on completion)")
os.system('touch ../build/ma_submit.txt')
