pipeline {
    agent any

    stages {
        stage('Submit Script') {
            parallel {
                stage ('Submit Script Testing'){
                    steps{                                  
                                  sh 'python submit.py'
                                  sh 'printf "\\e[31mHello\\e[0m\\n"'
                                  print('\033[31m' + 'some red text')
                                  print('\033[39m') # and reset to default color
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
