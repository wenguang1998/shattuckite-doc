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
                cd architectureDesign;
                umask 000;make html;
                umask 000;make latexpdf;
                chmod 777 build -R
                '''
    }

  }
  stage('DeployToGIT') {
    when {
       not {
          anyOf {
            branch 'master';
            branch 'SDD-dev';
            branch 'PRD-dev'
          }
       }
    }
    steps {
        sh 'git pull --tags'
        //保持发布子仓库处于最新提交
        sh '''
        if [ ! -d Team105 ]; then
            git clone --depth=5 git@github.com:sebuaa2019/Team105.git;
        fi
        '''

        //重新发布项目计划书
        sh 'rm -f Team105/设计文档*'
        sh 'cp architectureDesign/build/latex/shattuckite-design.pdf Team105/设计文档-$(git describe --always).pdf'

        sh '''git config user.email "1216573454@qq.com";
        git config user.name "Jenkins-Bot"
        '''
        
        sh '''
          cd Team105;
          git add -A;
          echo auto CI build  >/tmp/message;
          git commit -F /tmp/message;
          git push origin master;
          '''
        //需要手动删除。因为build产生的文件隶属于root用户组，jenkins用户无权删除。
        sh 'rm architectureDesign/build -Rf;'
      }
    } 
  }
}
