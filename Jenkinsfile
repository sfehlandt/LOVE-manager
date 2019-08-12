pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    script {
      def gitTag = sh(returnStdout: true, script: "git tag --points-at")
      echo "gitTag: ${gitTag}"
      def gitBranch = ${GIT_BRANCH}
      echo "gitBranch: ${gitBranch}"
      echo "GIT_BRANCH: ${GIT_BRANCH}"
      if (gitBranch == "master" && gitTag != "" && gitTag != null) {
        def imageTag = gitTag
      } else {
        def imageTag = gitBranch
      }
      echo "imageTag: ${imageTag}"
    }
    dockerImageName = "inriachile/love-manager:${GIT_BRANCH}"
    dockerImage = ""
  }

  stages {
    stage("Build Docker image") {
      when {
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          dockerImage = docker.build dockerImageName
        }
      }
    }
    // stage("Push Docker image") {
    //   when {
    //     anyOf {
    //       branch "master"
    //       branch "develop"
    //     }
    //   }
    //   steps {
    //     script {
    //       docker.withRegistry("", registryCredential) {
    //         dockerImage.push()
    //       }
    //     }
    //   }
    // }
    //
    // stage("Trigger develop deployment") {
    //   when {
    //     branch "develop"
    //   }
    //   steps {
    //     build(job: '../LOVE-integration-tools/develop', wait: false)
    //   }
    // }
    // stage("Trigger master deployment") {
    //   when {
    //     branch "master"
    //   }
    //   steps {
    //     build(job: '../LOVE-integration-tools/master', wait: false)
    //   }
    // }
  }
}
