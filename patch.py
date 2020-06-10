#!/bin/python

import subprocess
from args import getUserArguments  #args.py
from tmpl import loadTemplates  #tmpl.py

def applyPatches(patchTemplates, arguments):
    name = arguments['name']
    ns   = arguments['project']

    for template in patchTemplates: 
        cmd  = ["oc", "patch", "dc", name, "-n", ns, "--patch", template]
        oc_proc = subprocess.Popen(cmd,  stdin=subprocess.PIPE)
        oc_proc.wait()

arguments = getUserArguments()
templates = loadTemplates(arguments)
applyPatches(templates, arguments)
