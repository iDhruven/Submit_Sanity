pipeline {
    agent any

    stages {
        stage('Submit Sanity Check'){
            steps{
                print ("This is the Sanity Check Step!")
            }
        }
        stage('Submit Script') {
            parallel {
                stage ('Submit Script Testing'){
                    steps{  
                        sh 'python Submit/Submit.py'
                    }
                }
      
                stage ('Parallel Stage 2'){
                    when {
                        expression {
                                CHOICE == (H || H,A)
                        }
                    }
                    steps{
                        sh "echo Stage P2 Choice Condition"
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
