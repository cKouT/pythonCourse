glossary = {
	"script": "piece of programm how automate thing for you",
	"cd": "change directory",
	"ls": "list directory",
	"pwd": "print working directory",
	"cat": "show content file",
}

for k, v in glossary.items():
	print('command : ' + k.lower() + "---> " + v.capitalize())