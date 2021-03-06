#!/bin/python

import subprocess
from args import getUserArguments  #args.py
from tmpl import loadTemplates  #tmpl.py

def buildComponents(parsedTemplates, arguments):
 ns = arguments['project']
 cmd = ["oc", "apply", "-n", ns, "-f", "-"]

 for template in parsedTemplates: 
    ocProcess = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    ocProcess.communicate(template)
    ocProcess.wait()


arguments = getUserArguments()
if 'from' not in arguments:
    arguments['from'] = "templates"
    print "Using templates folder"

# Load the templates from arguments['from'] parameter
templates = loadTemplates(arguments)  

buildComponents(templates, arguments)
