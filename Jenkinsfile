pipeline {
    agent any

    stages {
        stage('Submit Sanity Check'){
            steps{
                print ("This is the Sanity Check Step!")
            }
        }
        
        stage('Submit Script'){
            steps{
                print ("Submit Script begins!")
                sh 'python Submit/Submit.py'
            }
        }
        
        stage('Submit Script Execution') {
            parallel {
                stages{
                    stage('B&I'){
                        
                    when{
                        expression {
                            return params.CHOICE.contains('B')
                        }
                    stages{
                        stage('B&I Sanity'){
                            steps{
                                print("This is a BNI Sanity check!")
                            }
                        }
                        stage ('B&I Execution'){
                            steps{
                                print ("This is B&I Submission Step!")
                            }
                        }
                    }
                }
                
                stage ('Submit MacOS Artifactory Pacakage'){
                    when {
                        expression {
                            return params.CHOICE.contains('P')
                        }
                    }
                    steps{
                        print ("MacOS Submission Step!")
                    }
                }
                
                stage ('Submit Mobile Assests'){
                    when {
                        expression {
                            return params.CHOICE.contains('M')
                        }
                    }
                    steps{
                        print ("Mobile Assests Submission Step!")
                    }
                }
                
                stage ('Submit Python Morphun'){
                    when {
                        expression {
                            return params.CHOICE.contains('L')
                        }
                    }
                    steps{
                        print ("Python Morphun Submission Step!")
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
}
