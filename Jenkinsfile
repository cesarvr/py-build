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
        echo "FROM_IMAGE: ${FROM_IMAGE}"
        echo "TO_PROJECT: ${TO_PROJECT}"

        echo "NAMESPACE: ${NAMESPACE}"
        echo "IMAGE: ${IMAGE}"
        sh "oc tag ${FROM_IMAGE} ${TO_PROJECT}"
        sh "python build.py project=${NAMESPACE} name=${SERVICE_NAME}"
        sh "python patch.py project=${NAMESPACE} name=${SERVICE_NAME} image=${IMAGE}"
      }
    }

    /** node **/
  }

}


