
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        PYTHON = 'C:\\Users\\Snehal Ninawe\\OneDrive\\Desktop\\Don Bosco\\.myenv\\Scripts\\python.exe'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install selenium pytest openpyxl'
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat '"%PYTHON%" -m pytest automation -v --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit(
                testResults: 'test-results.xml',
                allowEmptyResults: true
            )
        }
    }
}
