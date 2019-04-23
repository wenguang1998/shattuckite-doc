pipeline {
  agent {
    docker {
      image 'buaase-docenv'
      args '-u root -v $HOME/.ssh:/root/.ssh'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh ''' 
        umask 000;
        mkdir -p build;
        cd build;
        rm * -Rf;
        cmake ..;
        make;
        '''
    }
  }
  stage('DeployToGIT') {
  }

  stage('DeployToWebServer') {
    steps{
      sh './deployTools/deployToServer.sh'
    }
  }

  post {
    always {
        archiveArtifacts artifacts: 'build/shattuckite-v*.*.pdf', fingerprint: true
    }
  }
}
