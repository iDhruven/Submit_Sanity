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
                sh '''
                    python3 Submit/Submit.py
                    python Submit/SubmitLogo.py
                    python3 Submit/SubmitClean.py
                '''
                echo "All Steps Passed!"
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
                            python3 Submit/SubmitMajorTag.py > File.py
                            cat File.py
                            python3 DelFile.py
                            cat File.py
                        '''
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
                            sh '''
                                python3 Submit/SubmitMinorTag.py > File.py
                                cat File.py
                                python3 DelFile.py
                                cat File.py
                            '''
                        } else {
                            echo "Nothing here!"
                            sh '''
                                python3 Submit/SubmitCurrentTag.py > File.py
                                cat File.py
                                python3 DelFile.py
                                cat File.py
                            '''
                            NEW_VERSION=params.VERSION
                            echo "New Version is still the same as the Current Version ---> $NEW_VERSION"
                        }
                        print ("Validating NOOO the Submits here!")
                    }
                }
              
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
                            return params.CHOICE.contains('L') | params.CHOICE.contains('A')
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
                                sh 'python3 SubmitPyMorphun.py'
                            }
                        }
                     }
                  }
                
                stage ('Mobile Assests'){
                    agent any
                    when {
                        expression {
                            return params.CHOICE.contains('M')| params.CHOICE.contains('A')
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
                                sh 'python Submit/SubmitMobileAssets.py'
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
                                sh 'python3 Submit/SubmitUploadArtifactoryPackage.py'
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
                //sh 'python SubmitMobileAssets.py'
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
                deleteDir()
            }
        }
    }
}
