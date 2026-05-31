pipeline {
    agent any

    environment {
        DOCKER = '/usr/local/bin/docker'
        DOCKER_HUB_USER = 'jhamadhav2025'
    }

    stages {

        stage('SCM_Checkout') {
            steps {
                echo 'Checkout Source Code'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Build Frontend Image'
                sh '${DOCKER} build -t ${DOCKER_HUB_USER}/court-frontend:v1 ./frontend'

                echo 'Build Backend Image'
                sh '${DOCKER} build -t ${DOCKER_HUB_USER}/court-backend:v1 ./backend'
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | /usr/local/bin/docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Images To Docker Hub') {
            steps {

                sh '${DOCKER} push ${DOCKER_HUB_USER}/court-frontend:v1'

                sh '${DOCKER} push ${DOCKER_HUB_USER}/court-backend:v1'
            }
        }

        stage('Deploy Using Docker Compose') {
            steps {

                sh '${DOCKER} compose down'

                sh '${DOCKER} compose up -d --build'
            }
        }

        stage('Verify Containers') {
            steps {

                sh '${DOCKER} compose ps'
            }
        }
    }
}