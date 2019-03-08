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
                chmod 777 build -R
                '''
    }

  }
  stage('DeployToGIT') {
    steps {
        sh 'git pull --tags'
        sh 'git submodule update --init'
        //保持发布子仓库处于最新提交
        sh 'cd dist; git checkout master;git pull;'

        //重新发布项目计划书
        sh 'rm -f dist/项目计划书*'
        sh 'cp projectPlan/build/latex/shattuckite.pdf dist/项目计划书-$(git describe).pdf'

        sh 'git add dist'

        sh '''git config --global user.email "cn_lhc@qq.com";
        git config --global user.name "Jenkins-Bot"
        '''

        sh '''
          cd dist;
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