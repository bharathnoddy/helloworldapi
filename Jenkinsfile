pipeline {
    agent any

    parameters {
// 1.variables for the parametrized execution of the test: Text and options
        choice(choices: 'Build\nDeploy', description: 'build or deploy', name: 'MODE')
        choice(choices: 'yes\nno', description: 'Deploy new Deployment', name: 'DEPLOYMENT')
        string(defaultValue: '<kubernetes cluster endpoint>', description: 'K8s Env', name: 'k8s_CLUSTER')
        string(defaultValue: 'ENV', description: 'dev stage or prod', name: 'ENV')
    }
//2. Environment variables
environment {
  registry = "<repo details"
  registryCredential = "<credentialsId">
}
//3. Stages
    stages {

        stage('Build_and_Push'){
             //conditional for parameter
          when {
              environment name: 'MODE', value: 'Build'
            }
          steps{
            script {
              dockerImage = docker.build registry + "helloworld:1.0.$BUILD_NUMBER"
              docker.withRegistry( registry , registryCredential ) {
                dockerImage.push()

            }

                 }
             }
        }
        stage('Deploy'){
          when {
              environment name: 'mode', value: 'Deploy'
          }
          steps{
            script {
              wget <download requried kubeconfig file>
              kubectl config --kubeconfig=<path to config  set-cluster $ENV --server=$k8s_CLUSTER
              helm install deploy/
              //we can extend this script to roll back if the deployment fails to the earlier version

          


        }
    }
 }
}

