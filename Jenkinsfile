pipeline {
    agent any

    environment {
        PYTHON_ENV = 'myenv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $PYTHON_ENV
                source $PYTHON_ENV/bin/activate
                pip install selenium pytest
                '''
            }
        }
        stage('Install WebDriver') {
            steps {
                script {
                    // Download and install ChromeDriver
                    def CHROMEDRIVER_VERSION = sh(script: 'curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE', returnStdout: true).trim()
                    sh """
                    wget -N https://chromedriver.storage.googleapis.com/\${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip
                    unzip chromedriver_linux64.zip
                    sudo mv chromedriver /usr/local/bin/
                    rm chromedriver_linux64.zip
                    """
                    
                    // Optionally, install Google Chrome
                    sh '''
                    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
                    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
                    sudo apt-get update
                    sudo apt-get install -y google-chrome-stable
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source $PYTHON_ENV/bin/activate
                pytest --junitxml=reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/results.xml'
        }
    }
}
