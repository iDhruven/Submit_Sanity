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
                sh 'python3 Submit.py'
                sh 'python SubmitLogo.py'
                sh 'python3 SubmitClean.py'
                
                echo "All Steps Passed!"
                //input('Do you want to proceed?')
                script{
                    //
                    def USER_INPUT = input(
                        message: 'User input required - Do you want to make a Major Submit?',
                        parameters: [
                                [$class: 'ChoiceParameterDefinition',
                                choices: ['no','yes'].join('\n'),
                                name: 'input',
                                description: 'Menu - select box option']
                        ])

                    echo "The answer is: ${USER_INPUT}"

                    if( "${USER_INPUT}" == "yes"){
                        print ("Versioning the Submits here!")
                        sh '''
                            Num="1"
                            NEW_VERSION=$(echo "$VERSION 1" | awk '{print $1 + $2}')
                            echo "New Version is ---> $NEW_VERSION"
                        '''
                        env.NEW_VERSION = sh(script: "python3 MajorTag.py")//,
                             //returnStdout: true).trim()
                        //sh 'echo "New Version is ---> $NEW_VERSION"'
                        //env.NEW_VERSION="${NEW_VERSION}"
                        echo "NEW_VERSION: ${env.NEW_VERSION}"
                        //sh 'python3 SubmitMajorTag.py'
                    } else {
                        def USER_INPUT2 = input(
                        message: 'User input required - Do you want to make a Minor Submit?',
                        parameters: [
                                [$class: 'ChoiceParameterDefinition',
                                choices: ['no','yes'].join('\n'),
                                name: 'input',
                                description: 'Menu - select box option']
                        ])
                        
                        echo "The answer is: ${USER_INPUT2}"
                        
                        if( "${USER_INPUT2}" == "yes"){
                            echo "Minor Increasing"
                            //sh '''
                                sh 'Num="0.1"'
                                sh 'NEW_VERSION=$(echo "$VERSION $Num" | awk '{print $1 + $2}')'
                                sh 'echo "New Version is ---> $NEW_VERSION"'
                            //'''
                            //sh 'python3 SubmitMinorTag.py'
                        } else {
                            echo "Nothing here!"
                            sh 'NEW_VERSION=$VERSION'
                            sh 'echo "New Version is ---> $NEW_VERSION"'
                        }
                        print ("Validating NOOO the Submits here!")
                    }
                }
              
            }
            environment{
                NEW_VERSION="${NEW_VERSION}"
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
                print ("Validating the final Submits here!")
                sh 'echo "New Version is ---> $NEW_VERSION"'
                sh 'python3 SubmitUploadArtifactoryPackage.py'
                sh 'python3 SubmitMobileAssets.py'
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
               //deleteDir()
            }
        }
    }
}
