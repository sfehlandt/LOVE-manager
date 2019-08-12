pipeline {
  agent any
  environment {
    dockerBaseImageName = "inriachile/love-manager:"
    dockerImage = ""
    registryCredential = "dockerhub-inriachile"
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
          def git_tag = sh(returnStdout: true, script: "git tag --points-at")
          echo "git_tag: ${git_tag}"
          def git_branch = ${GIT_BRANCH}
          echo "git_branch: ${git_branch}"
          echo "GIT_BRANCH: ${GIT_BRANCH}"
          if (git_branch == "master" && git_tag != "" && git_tag != null) {
            def image_tag = git_tag
          } else {
            def image_tag = git_branch
          }
          echo "image_tag: ${image_tag}"
          dockerImageName = dockerBaseImageName + "${image_tag}"
        }
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
