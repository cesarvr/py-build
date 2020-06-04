
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

