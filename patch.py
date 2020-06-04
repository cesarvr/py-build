#!/bin/python

import subprocess
from args import getUserArguments
import tmpl

def applyPatches(patchTemplates, name, ns):

    for template in patchTemplates: 
        cmd  = ["oc", "patch", "dc", name, "-n", ns, "--patch", template]
        oc_proc = subprocess.Popen(cmd,  stdin=subprocess.PIPE)
        oc_proc.communicate(template)
        oc_proc.wait()

def run(arguments):
    patches_folder  = "patches"

    print "Patching Deployment"
    parsedPatchTemplates = tmpl.parseBuildTemplate(patches_folder, arguments) 
    applyPatches(parsedPatchTemplates, arguments["name"], arguments["project"])

arguments = getUserArguments()
run(arguments)
