#!/bin/python

import subprocess
from args import getUserArguments  #args.py
import tmpl  #tmpl.py

def buildComponents(parsedTemplates, ns):
 cmd = ["oc", "apply", "-n", ns, "-f", "-"]

 for template in parsedTemplates: 
    ocProcess = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    ocProcess.communicate(template)
    ocProcess.wait()

def run(arguments):
    template_folder = "templates"
    patches_folder  = "patches"

    print "Creating Openshift Generic Structure"
    parsedTemplates = tmpl.parseBuildTemplate(template_folder, arguments) 
    buildComponents(parsedTemplates, arguments['project'])

arguments = getUserArguments()
run(arguments)
