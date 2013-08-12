from sys import argv

script, filename = argv

print "this is a script name: %s" % script
print "this is  filename: %s" %  filename

def openfile(file,mode):
	text = ""
	if mode == "write": 
		text = open(file,'w')
		return text
	else if mode == "read":
		text = open(file,'r'')
		return text
	
#input = raw_input()

text = openfile(filename,"read")
print "I'm going to write these to the file."
print text.read()
text.close()

text = openfile(filename,"write")
text.write("I'm going to write these to the file.")
text.close()

