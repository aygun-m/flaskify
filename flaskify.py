#!/usr/bin/python3

from sys import argv
import os
version = '1.0'
whatisthis = 'Flaskify can generate a flask application based on given criteria.'
args = argv
args = args[1:]
help = f"""flaskify version {version}

{whatisthis}

Usage: flaskify.py <directory> [options]"""

"""
-b='<BPName>'
-d='<DBName>'
-s='<SSName>'
-t='<TPName>'
"""




def checkArgs(args):
    if len(args) < 1: print(help)
    else:
        #check if args[0] is a file or directory
        path = args[0]
        if os.path.isdir(path):
            dir = path
            #check for options
            blueprintsArgs = []
            databasesArgs = []
            stylesheetsArgs = []
            templatesArgs = []
            blueprints = []
            databases = []
            stylesheets = []
            templates = []
            for x in args:
                if x[:3] == '-b=':blueprintsArgs.append(x)
                if x[:3] == '-d=':databasesArgs.append(x)
                if x[:3] == '-s=':stylesheetsArgs.append(x)
                if x[:3] == '-t=':templatesArgs.append(x)
            for x in blueprintsArgs:blueprints.append(x[3:])
            for x in databasesArgs:databases.append(x[3:])
            for x in stylesheetsArgs:stylesheets.append(x[3:])
            for x in templatesArgs:templates.append(x[3:])
            
        elif os.path.isdir(path) == False:print(f"{path} is not a directory")
        

checkArgs(args)