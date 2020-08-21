pipeline {
    agent any

    stages {
        stage('Submit Script') {
            parallel {
                stage ('Submit Script Testing'){
                    steps{
                            sh '''echo "---------------The Submit Script Begins----------------"

                                  git config --list
                                  
                                  SUBMIT_VERSION=2
                                  DEBUG_MODE=1
                                  
                                  echo "Submit script version $SUBMIT_VERSION"
                                  
                                  if [ $DEBUG_MODE -eq 1 ]; then 
                                     echo "$(tput setaf 208)DEBUG MODE ENABLED$(tput sgr0)"
                                  fi      
                                  
                                  #Project settings
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
                                     GREEN_TEXT=$(tput setaf 2)
                                     RED_TEXT=$(tput setaf 1)
                                     CLEAR_TEXT=$(tput sgr0)

                                   

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
