#!/bin/python
import subprocess
from args import getUserArguments
import tmpl

def buildComponents(parsedTemplates, ns):
 cmd = ["oc", "apply", "-n", ns, "-f", "-"]

 for template in parsedTemplates: 
    oc_proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    oc_proc.communicate(template)
    oc_proc.wait()

def run(arguments):
    template_folder = "templates"
    patches_folder  = "patches"

    print "Creating Openshift Generic Structure"
    parsedTemplates = tmpl.parseBuildTemplate(template_folder, arguments) 
    buildComponents(parsedTemplates, arguments['project'])

arguments = getUserArguments()
run(arguments)
