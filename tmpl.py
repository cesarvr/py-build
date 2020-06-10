
from os import listdir

def readTemplates(file, arguments):
	content = open(file, "r").read()
        for name in arguments.keys():
            content =  content.replace("%" + name + "%", arguments[name])
        return content

def parseBuildTemplate(path, arguments):
	templates = listdir(path)
        templates = map(lambda template: path + "/" + template, templates)
	return map(lambda template: readTemplates(template, arguments), templates)


def loadTemplates(arguments):
    if "from" not in arguments:
        patches_folder  = "patches"
    else:
        patches_folder  = arguments["from"]

    print "Patching Deployment"
    return parseBuildTemplate(patches_folder, arguments) 


