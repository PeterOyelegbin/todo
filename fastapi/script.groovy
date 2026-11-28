#!/usr/bin/env groovy

def buildImage(String imageTag) {
    echo "building the application docker image..."
    withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
        sh "sudo docker build -t peteroyelegbin/todo-fastapi:$imageTag ."
        sh "echo '${script.DOCKERHUB_PASSWORD}' | sudo docker login -u '${script.DOCKERHUB_USERNAME}' --password-stdin"
        // sh "sudo docker push peteroyelegbin/todo-fastapi:$imageTag"
    }
}

def deployApp(){
  echo "deploying the application..."
  echo "deploying version ${params.VERSION}"
}

return this
