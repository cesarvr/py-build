# Build Script 

This script automates the deployment generic containers Openshift. We can use these templates to decouple the container creation like image tagging or S2I from the deployment configuration. 

I separated this process in two folder: 

  - In the ``templates`` folder we define the objects we want to create

  - The ``patches`` folder we define the updates we want to apply to these objects. Here we do things like secret injection, customizing limits, adding environment variables, etc. 


## Installing 

To install this pipeline example you just need to run:

```sh
oc new-build <the-url-for-this-repo> --name=deploy-services --strategy=pipeline
# Now you need to add the environment variables
# oc set env bc/deploy-services FROM_IMAGE=<Project>/<image-to-promote> TO_PROJECT=<destination-project>

oc set env bc/deploy-services FROM_IMAGE=Dev/frontend:latest TO_PROJECT=UAT/frontend:uat 

## Remember to set your private key in case you use a private Repo.
#  oc create secret generic gitsecret --from-file=ssh-privatekey=$HOME/.ssh/privatekey --type=kubernetes.io/ssh-auth
```

Before doing anything now you need to provide permissions to the Jenkins service account to perform actions in the desired project ``uat``.  

```sh
  oc adm policy add-role-to-user admin system:serviceaccount:ctest:jenkins -n uat
```

