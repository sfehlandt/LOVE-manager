pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    script {
      git_tag = sh(returnStdout: true, script: "git tag --points-at")
      echo "git_tag: ${git_tag}"
      git_branch = ${GIT_BRANCH}
      echo "git_branch: ${git_branch}"
      echo "GIT_BRANCH: ${GIT_BRANCH}"
      if (git_branch == "master" && git_tag != "" && git_tag != null) {
        image_tag = git_tag
      } else {
        image_tag = git_branch
      }
      echo "image_tag: ${image_tag}"
    }
    dockerImageName = "inriachile/love-manager:${image_tag}"
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
