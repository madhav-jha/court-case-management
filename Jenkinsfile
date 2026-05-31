pipeline {
    agent any

    stages {

        stage('SCM_Checkout') {
            steps {
                echo 'Perform SCM Checkout from GitHub Repository'
                checkout scm
            }
        }

        stage('Docker_Image_Build') {
            steps {
                echo 'Build Docker Image'
                sh 'docker build -t court-app:v1 .'
            }
        }

        stage('Application_Deploy') {
            steps {
                echo 'Deploy Application Container'

                sh 'docker rm -f court-container || true'

                sh 'docker run -d --name court-container -p 8080:80 court-app:v1'
            }
        }

        stage('Application_Verification') {
            steps {
                echo 'Verify Running Container'
                sh 'docker ps'
            }
        }
    }
}