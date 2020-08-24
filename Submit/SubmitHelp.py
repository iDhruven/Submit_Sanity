from SubmitProjectSettings import *

#Print Help
def print_help():
    print ("---------------Help Manual------------")
    print ("")
    print  "Using the script without any options will result in a full submission of : ", PROJECT
    print ("")
    print ("Any combination of Major, Minor version is allowed. This allows for future submissions as well as resubmissions.")
    print ("")
    print ("Example usage:")
    print ("Full submission: ./submit or ./submit -a")
    print  "Submit ", PROJECT, "to B&I only: ./submit -b"
    print ("Submit MobileAssets and artifactory package: ./submit -mp")
    print ("")
    print ("Using any combination of options is allowed.")
    print ("")
    print ("  -a : full submission")
    print ("  -i : initialize submission")
    print  "  -b : submit ", PROJECT, "to B&I"
    print ("  -t : tag submission and push to github")
    print ("  -p : submit macOS artifactory package")
    print ("  -m : submit MobileAssets")
    print ("  -l : submit python Morphun")
    print ("  -e : send release email")
    print ("  -h,? : this help message")
    print ("")