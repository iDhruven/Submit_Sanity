pipeline {
    agent any

    stages {
        stage('Build') {
            parallel {
                stage ('Parallel Stage 1'){
                    steps{
                            sh "echo "Stage P1""
                            sh "echo "Hello world!""
                    }
      
                stage ('Parallel Stage 2'){
                    steps{
                        sh "echo Stage P2"
                    }
                }
            }
        }
        
        stage('Test') {
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
