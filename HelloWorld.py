#!/usr/bin/env python
#my first python scrit

def wrapper(numberOfWordsInLine):
	#my first python scrit

	multiplier = 10
	print "Hello World"*multiplier
	print ("the world" " " "is beatutiful")
	print (2.3 + 8)

	#printing strings
	first = "This"
	second = " Is"
	third   = " Fucking"
	forth = " Awesome"
	print ("%s%s%s%s")  % (first,second,third,forth)

	#printing numbers
	one = 1
	two = 2
	three = 3
	print ("%d...%d...%d...GO!") % (one,two,three)

	#some logic in printing 
	print ("To! Python! Is it true that 5>2?")
	logic = 5 > 2
	print (logic)
	print ("-"*75)

	#putting shit inside other shit
	string = "Some string with '%s' sting inside" % "string"
	print "\nYo! I put you a %r inside your string so you can string while you string yo!" % string

	formatter = "\n %r %r %r %r"

	print formatter % ("big", "city", "lights", 123)

	#input = raw_input()
	#print (input)

	Text = """When you typed raw_input() you were typing the ( and ) characters which are parenthesis. 
	This is similar to when you used them to do a format with extra variables, as in "%s %s" % (x, y). 
	For raw_input you can also put in a prompt to show to a person so they know what to type."""

	#print Text.count
	array = []
	string1 = " "
	numberOfWordsInLine = 6
	begining = 0
	end = numberOfWordsInLine

	for i in Text:
		
		string1 = string1+i
		if i==" ":
			array.append(string1)
			string1 = ""
		
	for i in range(0,len(array)):
			if  i == end:
				print ' '.join((array[begining:end]))
				begining = end
				end += numberOfWordsInLine
			


