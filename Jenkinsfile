pipeline {
  agent {
    docker {
      image 'buaase-docenv'
      args "-v ${pwd()}:/exchange -w /exchange"
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