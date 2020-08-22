pipeline {
    agent any

    stages {
        stage('Submit Script') {
            parallel {
                stage ('Submit Script Testing'){
                    steps{                                  
                                  python submit.py
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
