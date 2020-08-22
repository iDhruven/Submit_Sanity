import os

print ("------------------------------The Submit Script Begins here--------------------------------------")

SUBMIT_VERSION=2
DEBUG_MODE=os.environ['DEBUG_MODE']

print "Submit script version:", SUBMIT_VERSION
print "Debug Mode:", DEBUG_MODE

if DEBUG_MODE == 1:
  print ("DEBUG MODE ENABLED")
  
# Project settings
PROJECT="Morphun"
SUBMIT_TO="GoldenGate Azul Hunter Archer"
MA_PROJECT="Morphun_AzulAssets"
GIT_REPO_URL="https://github.siri.apple.com/cslt/morphun.git"
ARTIFACTORY_URL="https://artifactory.siri.apple.com"

RELEASE_EMAIL_FROM= os.system('git config user.email')

RELEASE_EMAIL_TO="morphun-discussion@group.apple.com"

print ("EMAIL:", RELEASE_EMAIL_FROM)

# Files 
GIT_IGNORE=".gitignore"
SUBMIT_IGNORE=("gradle/wrapper/gradle-wrapper.jar")

# Reset in case getopts has been used previously
OPTIND=1

# getopts
RESUBMIT=0
FULL_SUBMIT=1
PROJECT_SUBMIT=0
INIT_SUBMIT=0
TAG_SUBMIT=0
ARTIFACTORY_SUBMIT=0
MOBILE_ASSETS_SUBMIT=0
PYTHON_MORPHUN_SUBMIT=0
RELEASE_EMAIL_SUBMIT=0

# print help
def print_help():
    print ("")
    print "Using the script without any options will result in a full submission of : ", PROJECT
    print ("")
    print ("Any combination of Major, Minor version is allowed. This allows for future submissions as well as resubmissions.")
    print ("")
    print ("Example usage:")
    print ("Full submission: ./submit or ./submit -a")
    print "Submit ", PROJECT, "to B&I only: ./submit -b"
    print ("Submit MobileAssets and artifactory package: ./submit -mp")
    print ("")
    print ("Using any combination of options is allowed.")
    print ("")
    print ("  -a : full submission")
    print ("  -i : initialize submission")
    print "  -b : submit ", PROJECT, "to B&I"
    print ("  -t : tag submission and push to github")
    print ("  -p : submit macOS artifactory package")
    print ("  -m : submit MobileAssets")
    print ("  -l : submit python Morphun")
    print ("  -e : send release email")
    print ("  -h,? : this help message")
    print ("")

    
CHOICE=[os.environ['CHOICE']] 
print CHOICE

HELP = "H"
result = [i for i in CHOICE if HELP in i]
print result

if CHOICE == "H" or "H,A" or "H,A,B" or "H,A,B,I" or "H,A,B,I,T": 
  print_help()


print ("--------------------------------The Submit Script Ends here-------------------------------------------")
