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
# oc set env bc/deploy-services FROM_IMAGE=<Project>/<image-to-promote> TO_PROJECT=<destination-project> SERVICE_NAME=<service name>

oc set env bc/deploy-services FROM_IMAGE=Dev/frontend:latest TO_PROJECT=UAT/frontend:uat SERVICE_NAME=frontend 

## Remember to set your private key in case you use a private Repo.
#  oc create secret generic gitsecret --from-file=ssh-privatekey=$HOME/.ssh/privatekey --type=kubernetes.io/ssh-auth
```

Before doing anything now you need to provide permissions to the Jenkins service account to perform actions in the desired project ``uat``.  

```sh
  oc adm policy add-role-to-user admin system:serviceaccount:ctest:jenkins -n uat
```


## Scripts 

### Build 

This scripts as mentioned before handles the object creation, to create this objects it uses ``yaml templates`` like this one. 

```yml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: %name% 
  labels:
    app: %name%
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: %name%
    spec:
      containers:
      - name: default-container
        image: busybox:latest
        ports:
        - containerPort: 8080 
```

> Those ``%name%`` are placeholders that you can use to replace the values at runtime. 


The script basically read all the templates inside the folder and create each one in the specified project: 

```sh
python build.py project=${NAMESPACE} name=${SERVICE_NAME}
``` 


![](https://github.com/cesarvr/py-build/blob/master/docs/automatic-build.gif?raw=true)

> The name parameter replace **%name%** in the template. This attribute in particular (**name**) has a special meaning for the script so **please don't change it**. 


### Customizing  


To customize your build is recommended that you use the patch.py script, and define your updates as files patches that will help you to cut the problem into smaller ones. 


So let's say you want to limit the amount of RAM memory your container will use, you can start by defining the patch file inside the patch folder like this: 


```yml
spec:
  template:
    spec:
      containers:
      - name: default-container
        resources:
            limits:
              memory: 80Mi
```

> Save this file as ``limit_ram.yml``. 


And run the script to automatically inject your changes to your service: 

```sh
python patch.py project=my-project name=httpd-frontend
```
> This will apply all the patch in the ``patches`` folder. OC will handle the update for us, it will ignore the patch if they are the same.


#### Dynamic Values 

Let's use the above example and choose a dynamic memory value: 

```yml
spec:
  template:
    spec:
      containers:
      - name: default-container
        resources:
            limits:
              memory: %memory%Mi
```

> We can set a placeholder using this ``%value%`` notation. 


Then we run the script like this: 

```sh
python patch.py project=my-project name=httpd-frontend memory=140
```

> Now the container will run under a 140MB of RAM limit. 











