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
          echo "GIT_BRANCH: ${GIT_BRANCH}"
          def git_branch = "${GIT_BRANCH}"
          echo "git_branch: ${git_branch}"
          def image_tag = git_branch

          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_branch = git_branch.substring(0, slashPosition)
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            echo "new git_branch: ${git_branch}"
            echo "git_tag: ${git_tag}"
            if (git_branch == "release") {
              image_tag = git_tag
            }
          }

          echo "image_tag: ${image_tag}"
          def dockerImageName = dockerBaseImageName + image_tag
          echo "dockerImageName: ${dockerImageName}"
          dockerImage = docker.build(dockerImageName)
        }
        // script {
        //   dockerImage = docker.build dockerImageName
        // }
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
