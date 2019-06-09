pipeline {
  agent {
    docker {
      image 'buaase-docenv'
      args '-u root -v $HOME/.ssh:/root/.ssh'
    }
  }
  stages{
    stage('Build') {
      steps {
        sh ''' 
        git pull --tags;
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
      steps{
        sh 'chmod a+x ./deployTools/deployToGit.sh'
        sh './deployTools/deployToGit.sh'
      }
    }
    stage('DeployToWebServer') {
      steps{
        sh 'chmod a+x ./deployTools/deployToServer.sh'
        sh './deployTools/deployToServer.sh'
      }
    }
  }
  post {
    always {
        archiveArtifacts artifacts: 'build/shattuckite-v*.*.pdf', fingerprint: true
    }
  }
}
