pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "premk26"
        BACKEND_IMAGE = "two-tier-backend"
        FRONTEND_IMAGE = "two-tier-frontend"
    }

    stages {
        stage('Build Docker Images') {
            steps {
                bat '''
                docker build -t %DOCKERHUB_USERNAME%/%BACKEND_IMAGE% ./backend
                docker build -t %DOCKERHUB_USERNAME%/%FRONTEND_IMAGE% ./frontend
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    bat 'docker login -u %USER% -p %PASS%'
                }
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                bat '''
                docker push %DOCKERHUB_USERNAME%/%BACKEND_IMAGE%
                docker push %DOCKERHUB_USERNAME%/%FRONTEND_IMAGE%
                '''
            }
        }
    }
}