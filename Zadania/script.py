#!/usr/bin/python
import sys
import getopt
import argparse
import subprocess
import time
import re

import xlwt

def CreateXLS(value):
	# kodowanie arkusza
	book = xlwt.Workbook(encoding="utf-8")

	# tworzymy dowolną ilość arkuszy (zakładek)
	sheet1 = book.add_sheet("Results")

	# umieszczamy w nich dane
	sheet1.write(0, 0, "score")
	sheet1.write(1, 0, value)

	# zapisujemy do pliku
	book.save("raport.xls")

def OpenXLS(file_name):
	book = xlrd.open_workbook("raport.xls")
	return book

press_key_cmd = "input keyevent "
adb_path      = "./home/luze/Programs/sdk/platform-tools/adb"
app_name      = ''
app_package   = ''

def PrintRes(log):
	log = re.search('(?<=score)\w+',log)
	print "Result = " + log[0]

def WaitFor(_time):
"""
 Suspend execution for the given number of seconds. The argument may be a
 floating point number to indicate a more precise sleep time.
 _time - int, floating point
"""
	time.sleep(_time)

def ExecuteCMD(cmd):
	_p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
	_log = _p.communicate()
	print "stdout " + _log[0]
	print "stderr " + _log[1] 

ADB_CMD = {
	'INSTALL'   : adb_path + " install " +  app_name
	'UNINSTALL' : adb_path + " uninstall " + app_package
	'START_APP' : adb_path + ' am start -a ' + app_package
	'LOGCAT'    : adb_path + ' logcat -d'
	}
ADB_KEY_LIB = {
		'UP'     : press_key_cmd + '19',
		'DOWN'   : press_key_cmd + '20',
        'LEFT'   : press_key_cmd + '21',
		'RIGHT'  : press_key_cmd + '22',
		'CENTER' : press_key_cmd + '23',
		'BACK'   : press_key_cmd + '3' ,
		'Menu'   : press_key_cmd + '82',
	}

def Tutorial1LoadData(argv):
	if argv is None:
		print "end of program"
		sys.exit()
	_sDesc = "this is a small application which does not do nothing"          
	_objParser = argparse.ArgumentParser(description=_sDesc)
	_objParser.add_argument('-i', '--input-file', help='path with xml file')
	_objParser.add_argument('-o','--output-file', help='path to output file')

	_arrArgs = _objParser.parse_args()
	print _arrArgs

def Tutorial1LoadData2(argv):
	try:
		print argv
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
			print inputfile
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			print outputfile


def main(argv = None):

#loading arguments first way
	Tutorial1LoadData(argv)

#Check loading arguments 2
	print "2"
	Tutorial1LoadData2(argv)

	name = raw_input("Tell me your name")
        print "Hi %s, how are you today"
        print "    "
        print "1. Good, everything is okay"
        print "2. Bad. " 
        print "3. Don't ask, or I will kill you"
        answer = raw_input("what you choose :")

if __name__ == "__main__":
    main(sys.argv)

