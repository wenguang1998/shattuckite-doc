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
                cd projectPlan;
                make html;
                make latexpdf;
                '''
      }
    }
    stage('DeployToGIT') {
      steps {
          sh 'ls $HOME/.ssh'
          sh 'cat $HOME/.ssh/id_rsa.pub'
          sh 'git submodule update --init'
          sh 'cp projectPlan/build/latex/shattuckite.pdf dist/项目计划书.pdf'
          sh 'git add dist'
          sh 'git config --global user.email "cn_lhc@qq.com"'
          sh 'git config --global user.name "Jenkins-Bot"'
          sh '''
           cd dist;
           git checkout master;
           git add -A;
           echo auto CI build  >message;
           git commit -F message;
           git push origin master'''
          }
    } }
}