def JENKINS_SLAVE = "registry.redhat.io/openshift3/jenkins-slave-base-rhel7:v3.11"
def JNLP_CONTAINER = 'jnlp'

podTemplate(cloud:'openshift', label: BUILD_TAG,
    containers: [ containerTemplate(name: "jnlp", image: JENKINS_SLAVE) ]
    ) {
  node(BUILD_TAG) {

    container(JNLP_CONTAINER) {
      stage('Tagging Image') {
        echo "${NAMESPACE}"
          echo "${IMAGE}"
      }
    }

    /** node **/
  }

}


