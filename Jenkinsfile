pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-portfolio-app'
        CONTAINER_NAME = 'devops-portfolio-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm ${IMAGE_NAME} pytest
                '''
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh '''
                        docker rm -f ${CONTAINER_NAME} || true
                        docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
