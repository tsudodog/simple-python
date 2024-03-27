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
                    cd app
                    python3 main.py
                '''
                app = docker.build('app')
            }
        }

        stage('Test With Params') {
            steps {
                echo 'Testing...'

                sh '''
                    echo "doing test stuff"
                    cd app
                    python3 main.py --name=Tsudo
                '''
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    app = docker.build('my-test-app')
                }
            }
        }
        stage('Deliver') {
            steps {
                script {
                    echo 'Delivering'
                    docker.withRegistry('https://888974021974.dkr.ecr.us-east-1.amazonaws.com/tsudo-repository', 'ecr:us-east-1:aws-credentials')
                    app.push("${env.BUILD_NUMBER}")
                    app.push('latest')
                }
            }
        }
    }
}
