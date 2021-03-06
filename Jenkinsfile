def JENKINS_SLAVE = "registry.redhat.io/openshift3/jenkins-slave-base-rhel7:v3.11"
def JNLP_CONTAINER = 'jnlp'
def tokens = TO_PROJECT.tokenize('/')
def NAMESPACE = tokens[0]
def IMAGE = tokens[1]

podTemplate(cloud:'openshift', label: BUILD_TAG,
    serviceAccount: 'jenkins',
    containers: [ containerTemplate(name: "jnlp", image: JENKINS_SLAVE) ],
    ) {
  node(BUILD_TAG) {

    container(JNLP_CONTAINER) {
      stage('Tagging Image') {
        checkout scm
          echo "FROM_IMAGE: ${FROM_IMAGE}"
          echo "TO_PROJECT: ${TO_PROJECT}"

          echo "NAMESPACE: ${NAMESPACE}"
          echo "IMAGE: ${IMAGE}"
          sh "oc tag ${FROM_IMAGE} ${TO_PROJECT}"

      }


      stage('Creating Objects') {
        sh "python build.py project=${NAMESPACE} name=${SERVICE_NAME}"
      }

      stage('Updating Objects') {
        sh "python patch.py project=${NAMESPACE} name=${SERVICE_NAME} image=${IMAGE}"

        sh "oc wait -n ${NAMESPACE} dc/${SERVICE_NAME} --for condition=available --timeout=-1s"
      }

      stage('Smoke Test') {
        def route = sh(
            script: "oc -n ${NAMESPACE} get route ${SERVICE_NAME} -o=jsonpath={.spec.host}",
            returnStdout: true ).trim()
          echo "Running Smoke Tests: ${route}"
          sh "python smoke.py https://${route}"
      }

      stage('Validating'){
        echo "Ready for Prod"
      }
    }

    /** node **/
  }

}


