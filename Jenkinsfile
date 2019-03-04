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
    stage('DeployToGIT') {
      steps {
        sh ''' 
                cp projectPlan/build/latex/shattuckite.pdf dist/项目计划书.pdf;
                cd dist
                git add *
                git commit -m "auto commit from CI"
                git push 
                '''
      }
    }
  }
}