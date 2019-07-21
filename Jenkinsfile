pipeline {
  agent any
  stages {
    stage('error') {
      parallel {
        stage('error') {
          steps {
            sh 'echo "First step for pipeline"'
          }
        }
        stage('') {
          steps {
            node(label: 'N1_Arjun') {
              sleep 20
              build(job: 'J1', quietPeriod: 1, wait: true)
            }

          }
        }
      }
    }
  }
}