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
