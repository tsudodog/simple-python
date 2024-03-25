pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    echo "doing build stuff"
                    cd app
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'

                sh '''
                    echo "doing test stuff"
                    python3 hello.py
                '''
            }
        }

        stage('Test With Params') {
            steps {
                echo 'Testing...'

                sh '''
                    echo "doing test stuff"
                    python3 hello.py --name=Tsudo
                '''
            }
                }
        stage('Deliver') {
            steps {
                echo 'Delivering'
                sh '''
                     echo "doing delivery stuff"
                 '''
            }
        }
    }
}
