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
                git pull --tags;
                cd projectPlan;
                make html;
                make latexpdf;
                chmod 777 build -R
                '''
    }

  }
  stage('DeployToGIT') {
    steps {
        sh 'git pull --tags'
        sh '''
          if [ ! -d Team105 ]; then
            git clone --depth=1 git@github.com:sebuaa2019/Team105.git;
          else
            cd Team105;
            git pull --depth=1;
          fi
        '''
        //重新发布项目计划书
        sh 'rm -f Team105/项目计划书*'
        sh 'cp projectPlan/build/latex/shattuckite.pdf Team105/项目计划书-$(git describe).pdf'

        sh '''git config --global user.email "cn_lhc@qq.com";
        git config --global user.name "Jenkins-Bot"
        '''

        sh '''
          cd Team105;
          git add -A;
          echo auto CI build  >/tmp/message;
          git commit -F /tmp/message;
          git push origin master;
          '''
        //需要手动删除。因为build产生的文件隶属于root用户组，jenkins用户无权删除。
        sh 'rm projectPlan/build -Rf;'
      }
    } 
  }
}
