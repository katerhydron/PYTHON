#!/usr/bin/python

def WelcomeAndReturnName():
    print " Hi, what's your name?"
    name = raw_input()
    print " Nice to meet you %s" % name.title()
    return name.title()

def CheckPermission():
    name = WelcomeAndReturnName()
    try :
        guests[name]
        print "Access Granted"
    except KeyError:
        print "Access Denied"

guests = {'Ala':'room 6','Wojtek':'room 2a','Anna':'4','Waldemar':'33','Lech':'13','Czech':'34','Rus':'50','Terran':'36','Protoss':'31','Zerg':'32'}
CheckPermission()



