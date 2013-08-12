#!/usr/bin/python

import sys
import argparse
import re
import os

def LoadArgument(argv):
	if argv is None:
		print "end of program"
		sys.exit()
	_sDesc = "this is a small application which does not do nothing"
	_objParser = argparse.ArgumentParser(description=_sDesc)
	_objParser.add_argument('-i', '--input-file', help='Input file')

	_arrArgs = _objParser.parse_args()
        return _arrArgs.input_file

def CheckPathFile(input_file):

    path = os.path.abspath(input_file)
    exists = os.path.exists(path)

    #if file does not exist you are asked to re-type path
    if (not exists):
        print "\nData does not exists, Please check path\n"
        decide = raw_input("Do you want correct your path?(Y/N)")

        if (decide=='Y' or decide=='y'):
            print "\nOld path is: %s" % path
            path = raw_input("\nPlease enter new path ")
            CheckPathFile(os.path.basename(path))

    #if you don't want to edit path, script ends
        else:
            print "\nBye Bye"
            sys.exit()

    #if file has been found just return it's path and filename
    else:
        print "\nSuccess! File has been found"
        return str(input_file), str(path)

def ReadInfo():
    file = open('info.txt','r')
    if file is None:
        print "\nLack of info.txt file\n"
    else:
        info = file.read()

        autor = re.search('(?<=autor : ").*(?=")',info)
        version = re.search('(?<=ver : ").*(?=")',info)
        release_date = re.search('(?<=rel_data : \()\d+\-\d+\-\d+',info)

        myArray= []

        if autor:
            myArray.append(autor.group())
        else:
            myArray.append("No author!!")

        if version:
            myArray.append(version.group())
        else:
            myArray.append("No version!!")

        if release_date:
            myArray.append(release_date.group())
        else:
            myArray.append("No release date!!")

        return myArray


def main(argv = None):
    input_file,path = CheckPathFile(LoadArgument(argv))
    if input_file is not None or path is not None:
        print "\nAll clear, let's proceed"
        #here we could send path and filename to ReadInfo function
        #but for now let's just use it without arguments
    myArray = ReadInfo();

    for i in range(0,len(myArray)):
        print myArray[i]


if __name__ == "__main__":
        main(sys.argv)


