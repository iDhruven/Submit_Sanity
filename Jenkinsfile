pipeline {
    agent any

    stages {
        stage('Submit Script') {
            parallel {
                stage ('Submit Script Testing'){
                    steps{
                            sh '''echo "---------------The Submit Script Begins----------------"
                                  
                                  SUBMIT_VERSION=2
                                  DEBUG_MODE=1
                                  
                                  echo "Submit script version $SUBMIT_VERSION"
                                  
                                  if [ $DEBUG_MODE -eq 1 ]; then 
                                     echo "$(tput setaf 208)DEBUG MODE ENABLED$(tput sgr0)"
                                  fi      
                                  
                                  # Project settings
                                    PROJECT="Morphun"
                                    SUBMIT_TO="GoldenGate Azul Hunter Archer"
                                    MA_PROJECT="Morphun_AzulAssets"
                                    GIT_REPO_URL="https://github.siri.apple.com/cslt/morphun.git"
                                    ARTIFACTORY_URL="https://artifactory.siri.apple.com"
                                    RELEASE_EMAIL_FROM=`git config user.email`
                                    RELEASE_EMAIL_TO="morphun-discussion@group.apple.com"
                                   
                                   # Files 
                                     GIT_IGNORE=".gitignore"
                                     SUBMIT_IGNORE=("gradle/wrapper/gradle-wrapper.jar")

                                   # Reset in case getopts has been used previously
                                     OPTIND=1

                                   # Assigned later
                                     RADARS=
                                     BUG_RADARS=
                                     API_CHANGES=

                                   # Text colors
                                     #GREEN_TEXT=$(tput setaf 2)
                                     #RED_TEXT=$(tput setaf 1)
                                     #CLEAR_TEXT=$(tput sgr0)
                                     
                                     
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
                                      print_help() {
                                        echo ""
                                        echo "Using the script without any options will result in a full submission of $PROJECT."
                                        echo ""
                                        echo "Any combination of Major, Minor version is allowed. This allows for future submissions as well as resubmissions."
                                        echo ""
                                        echo "Example usage:"
                                        echo "• Full submission: ./submit or ./submit -a"
                                        echo "• Submit $PROJECT to B&I only: ./submit -b"
                                        echo "• Submit MobileAssets and artifactory package: ./submit -mp"
                                        echo ""
                                        echo "Using any combination of options is allowed."
                                        echo ""
                                        echo "  -a : full submission"
                                        echo "  -i : initialize submission"
                                        echo "  -b : submit $PROJECT to B&I"
                                        echo "  -t : tag submission and push to github"
                                        echo "  -p : submit macOS artifactory package"
                                        echo "  -m : submit MobileAssets"
                                        echo "  -l : submit python Morphun"
                                        echo "  -e : send release email"
                                        echo "  -h,? : this help message"
                                        echo ""
                                      }
                                      
                                      
                                      while getopts "h?abitlpmer" opt; do
                                        case "$opt" in
                                        h|?)
                                            print_help
                                            exit 0
                                            ;;
                                      
                                        
                                        i)  INIT_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        t)  TAG_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        b)  PROJECT_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        p)  ARTIFACTORY_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        m)  MOBILE_ASSETS_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        l)  PYTHON_MORPHUN_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        e)  RELEASE_EMAIL_SUBMIT=1
                                            FULL_SUBMIT=0
                                            ;;
                                        a)  FULL_SUBMIT=1
                                            ;;
                                        r)  RESUBMIT=1
                                            ;;
                                        esac
                                      done
                                      
                                      # TODO: check for OS and exit if not macOS

                                      # Cool logo goes here
                               echo " $(tput setaf 196)    ______  _______   
                                         |      \\/       \\  
                                        /          /\\     \\ 
                                       /     /\\   / /\\     |
                                      /     /\\ \\_/ / /    /|
                                     |     |  \\|_|/ /    / |
                                     |     |       |    |  |
                                     |\\____\\       |____|  /$(tput setaf 196)O$(tput setaf 202)R$(tput setaf 208)P$(tput setaf 214)H$(tput setaf 220)U$(tput setaf 226)N$(tput setaf 196)
                                     | |    |      |    | / 
                                      \\|____|      |____|/${CLEAR_TEXT}
                                       "
                                       
                                       
                                      # Actual script begins here
                                        PROJECT_TAG=`git tag -l | grep "$PROJECT-*" | sed "s/$PROJECT-//" | sort -n | tail -1`
                                      
                                      # Parse out major identifier only
                                        PROJECT_MAJOR_VERSION=`echo $PROJECT_TAG | egrep -o '\\d+' | head -1`
                                      
                                      # Get everything else
                                        PROJECT_MINOR_VERSION=`sed -E "s/^[^\\.]*\\.?//" <<< $PROJECT_TAG`
                                        if [ -z "$PROJECT_MINOR_VERSION" ]; then
                                            PROJECT_MINOR_VERSION=0
                                        fi
                                        
                                        echo "Current project version: $PROJECT_MAJOR_VERSION.$PROJECT_MINOR_VERSION"
                                        echo "The PROJECT Major Version is --> : " $PROJECT_MAJOR_VERSION
                                        echo "The PROJECT Tag is --> : " $PROJECT_TAG
                                        
                                #        PROJECT_PROPOSED_MAJOR_VERSION=$(expr $PROJECT_MAJOR_VERSION + 1)
                                #        PROJECT_PROPOSED_MINOR_VERSION=0
                                #        if [ "$PROJECT_MINOR_VERSION" -gt "0" ]; then
                                #            PROJECT_PROPOSED_MAJOR_VERSION=$PROJECT_MAJOR_VERSION
                                #            PROJECT_PROPOSED_MINOR_VERSION=$(expr $PROJECT_MINOR_VERSION + 1)
                                #        fi
                                #        echo "Proposed new version: ${GREEN_TEXT}${PROJECT_PROPOSED_MAJOR_VERSION}.${PROJECT_PROPOSED_MINOR_VERSION}${CLEAR_TEXT}"








                                   

                                  echo "---------------The Submit Script Ends----------------"'''
                    }
                }
      
                stage ('Parallel Stage 2'){
                    steps{
                        sh "echo Stage P2"
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
