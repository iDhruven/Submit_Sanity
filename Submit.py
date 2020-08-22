import os
import git

print ("-----------The Submit Script Begins here------------------")

SUBMIT_VERSION=2
DEBUG_MODE=os.environ['DEBUG_MODE']

print ("Submit script version:", SUBMIT_VERSION)
print ("Debug Mode:", DEBUG_MODE)

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")
  
# Project settings
PROJECT="Morphun"
SUBMIT_TO="GoldenGate Azul Hunter Archer"
MA_PROJECT="Morphun_AzulAssets"
GIT_REPO_URL="https://github.siri.apple.com/cslt/morphun.git"
ARTIFACTORY_URL="https://artifactory.siri.apple.com"
RELEASE_EMAIL_FROM= os.system('git --version')
RELEASE_EMAIL_TO="morphun-discussion@group.apple.com"

print ("EMAIL:", RELEASE_EMAIL_FROM)

print ("-----------The Submit Script Ends here------------------")
