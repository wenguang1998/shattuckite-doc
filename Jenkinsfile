pipeline {
  agent {
    docker {
      image 'buaase-docenv'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh ''' 
                cd projectPlan;
                make html;
                make latexpdf;
                '''
      }
    }
  }
}