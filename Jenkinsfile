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
                sh 'cd /Users/idhruven/.jenkins/workspace/PythonSanity'
                sh 'python Submit/Submit.py'
            }
        }
        
        stage('Submit Script Execution') {
            parallel {
                stage ('B&I'){
                    agent any
                    when {
                        expression {
                            return params.CHOICE.contains('B')
                        }
                    }
                    stages{
                        stage ('B&I Sanity Check'){
                            steps{
                                echo "B&I Sanity Check happens here"
                            }
                        }
                        stage ('Submit to B&I'){
                            steps{
                                //
                                print ("This is B&I Submission Step!")
                            }
                        }
                     }           
                  }

                stage ('Python Morphun'){
                    agent any
                    when {
                        expression {
                            return params.CHOICE.contains('L')
                        }
                    }
                    stages{
                        stage ('Python Morphun Sanity Check'){
                            steps{
                                echo "Python Morphun Sanity Check happens here"
                            }
                        }
                        stage ('Submit to Python Morphun'){
                            steps{
                                print ("This is Python Morphun Submission Step!")
                            }
                        }
                     }           
                  }
                
                stage ('Mobile Assests'){
                    agent any
                    when {
                        expression {
                            return params.CHOICE.contains('M')
                        }
                    }
                    stages{
                        stage ('Mobile Assests Sanity Check'){
                            steps{
                                echo "Mobile Assests Sanity Check happens here"
                            }
                        }
                        stage ('Submit to Mobile Assests'){
                            steps{
                                print ("This is Mobile Assests Submission Step!")
                            }
                        }
                     }           
                  }
                //
                stage ('macOS Artifactory Packages'){
                    agent any
                    when {
                        expression {
                            return params.CHOICE.contains('P')
                        }
                    }
                    stages{
                        stage ('macOS Artifactory Package Sanity Check'){
                            steps{
                                echo "macOS Artifactory Package Sanity Check happens here"
                            }
                        }
                        stage ('Submit to macOS Artifactory Package'){
                            steps{
                                //
                                print ("This is macOS Artifactory Package Submission Step!")
                            }
                        }
                     }           
                  }
                

                
            }
        }
        
        stage ('Validate'){
            steps{
                print ("Validating the Submits here!")
            }
        }
        
        stage('Notify') {
            steps {
                echo 'Sending Email..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
               // deleteDir()
            }
        }
    }
}
