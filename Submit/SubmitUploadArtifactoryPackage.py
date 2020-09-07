from SubmitProjectSettings import *
from SubmitMajorTag import *

ARTIFACTORY_PATH= ARTIFACTORY_URL + "/libs-release-local/com/apple/csl/morphun/" + str(New_Version)
TGZ_NAME="morphun-",(New_Version),"-mac.tgz"

print(ARTIFACTORY_PATH)
print(TGZ_NAME)
