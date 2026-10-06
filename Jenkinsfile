pipeline {
  agent any
  environment { IMAGE = 'portfolio' }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps {
        sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt && pytest'
      }
    }
    stage('Build Image') {
      steps { sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .' }
    }
    stage('Deploy to Azure VM') {
      steps {
        sh '''
          docker rm -f portfolio || true
          docker run -d --restart always --name portfolio -p 80:5000 $IMAGE:latest
        '''
      }
    }
  }
}