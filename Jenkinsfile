pipeline {
  agent any
  triggers{
  pollSCM('* * * * *')
  }
  stages {
    stage('error') {
      parallel {
        stage('test') {
          steps {
            sh 'echo "First step for pipeline"'
          }
        }
        stage('nv') {
          steps {
            sh 'echo "2nd step for pipeline"'
          }
        }
      }
    }
  }
}
