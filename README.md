# Build Script 

This script automates the deployment generic containers Openshift. We can use these templates to decouple the container creation like image tagging or S2I from the deployment configuration. 

I separated this process in two folder: 

  - In the ``templates`` folder we define the objects we want to create

  - The ``patches`` folder we define the updates we want to apply to these objects. Here we do things like secret injection, customizing limits, adding environment variables, etc. 



