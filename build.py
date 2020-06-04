#!/bin/python

from os import listdir
import sys
import subprocess
from args import getUserArguments

def readTemplates(file, arguments):
	content = open(file, "r").read()
        for name in arguments.keys():
            content =  content.replace("%" + name + "%", arguments[name])
        return content

def parseBuildTemplate(path, arguments):
	templates = listdir(path)
        templates = map(lambda template: path + "/" + template, templates)
	return map(lambda template: readTemplates(template, arguments), templates)

def runTemplates(parsedTemplates):
 for template in parsedTemplates: 
    oc_proc = subprocess.Popen(["oc", "apply", "-f", "-"],  stdin=subprocess.PIPE)
    oc_proc.communicate(template)
    oc_proc.wait()

def applyPatches(patchTemplates, arguments):
    for template in patchTemplates: 
        oc_proc = subprocess.Popen(["oc", "patch", "dc", arguments["name"], "--patch", template],  stdin=subprocess.PIPE)
        oc_proc.communicate(template)
        oc_proc.wait()


def run(arguments):
    template_folder = "templates"
    patches_folder  = "patches"

    print "Creating Openshift Generic Structure"
    parsedTemplates = parseBuildTemplate(template_folder, arguments) 
    runTemplates(parsedTemplates)

    print "Patching Deployment"
    parsedPatchTemplates = parseBuildTemplate(patches_folder, arguments) 
    applyPatches(parsedPatchTemplates, arguments)


arguments = getUserArguments()
print "arguments ->", arguments
run(arguments)
