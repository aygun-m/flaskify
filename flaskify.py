#!/usr/bin/python3

from operator import index
from readline import append_history_file
from sys import argv
import os
from urllib.parse import ParseResultBytes
version = '1.0'
whatisthis = 'Flaskify can generate a flask application based on given criteria.'
args = argv
args = args[1:]
help = f"""flaskify version {version}

{whatisthis}

Usage: flaskify.py <directory> -n=<app name> [options]"""

"""
-b='<BPName>'
-d='<DBName>'
-s='<SSName>'
-t='<TPName>'
"""




def checkArgs(args):
    if len(args) < 1:print(help)
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
            nameArgs= []
            blueprints = []
            databases = []
            stylesheets = []
            templates = []
            name = []
            for x in args:
                if x[:3] == '-b=':blueprintsArgs.append(x)
                if x[:3] == '-d=':databasesArgs.append(x)
                if x[:3] == '-s=':stylesheetsArgs.append(x)
                if x[:3] == '-t=':templatesArgs.append(x)
                if x[:3] == '-n=':nameArgs.append(x)
            for x in nameArgs:name.append(x[3:])
            for x in blueprintsArgs:blueprints.append(x[3:])
            for x in databasesArgs:databases.append(x[3:])
            for x in stylesheetsArgs:stylesheets.append(x[3:])
            for x in templatesArgs:templates.append(x[3:])
            if len(name) < 1:print(help)
            else:
                if dir == '.': dir = os.getcwd()
                #create flask_app/
                webapp_name = name[0]
                if ' ' in webapp_name: print("Flask application name cannot include spaces")
                else:
                    main_name = 'main.py'
                    init_name = '__init__.py'
                    views_name = 'views.py'
                    static_directory_name = 'static/'
                    stylesheet_name = 'styles.css'
                    js_name = 'index.js'
                    template_directory_name = 'templates/'
                    index_name = 'index.html'

                    #flaskify/blackroses/ 1
                    #flaskify/main.py 1
                    #flaskify/blackroses/ 1
                        #flaskify/__init__.py 1
                        #flaskify/views.py 1
                        #flaskify/static/ 1
                            #flaskify/styles.css 1
                        #flaskify/templates 1
                            #flaskify/index.html 1
                    main_file = f"""
                    from {webapp_name} import app
                    app.run(debug=True)
                    """
                    if blueprints == []:
                        init_file = f"""from flask import Flask
from .views import views
app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.config['SECRET_KEY] = 'mysecretkey'"""
                    else:
                        #Check for extra blueprints
                        forLoopBlueprints = []
                        forLoopRegister = []
                        init_file_prep = ""
                        init_file_reg = ""
                        for x in blueprints:
                            loopBP = []
                            string = ''
                            loopBP.append('from')
                            loopBP.append(f'.{x}')
                            loopBP.append('import')
                            loopBP.append(f'{x}')
                            for y in loopBP:
                                string += y
                                string += ' '
                            forLoopBlueprints.append(string)
                            for x in forLoopBlueprints:
                                init_file_prep += x
                                init_file_prep += '\n'
                        for x in blueprints:
                            loop_RG = []
                            string = ''
                            loop_RG.append('app.register_blueprint(')
                            loop_RG.append(x)
                            loop_RG.append(', url_prefix=\'/\')')
                            for y in loop_RG:
                                string += y
                                string += ' '
                            forLoopRegister.append(string)
                            for x in forLoopRegister:
                                init_file_reg += x
                                init_file_reg += '\n'
                        init_file = f"""from flask import Flask
from .views import views
{init_file_prep}
app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
{init_file_reg}
app.config['SECRET_KEY'] = 'mysecretkey'"""
                    
                   #Init File done
                        
                        

                    mk_webapp_name = os.path.join(dir, webapp_name)
                    os.mkdir(mk_webapp_name)
                    print(f"Created directory at: {mk_webapp_name}")
                    mk_main_name = os.path.join(mk_webapp_name, main_name)
                    with open(mk_main_name, 'w') as f:f.write("This is main.py")
                    print(f"Created file at: {mk_main_name}")
                    mk_app_name = os.path.join(mk_webapp_name, webapp_name)
                    os.mkdir(mk_app_name)
                    print(f"Created directory at: {mk_app_name}")
                    mk_init_name = os.path.join(mk_app_name, init_name)
                    with open(mk_init_name, 'w') as f: f.write(init_file)
                    print(f'Created file at: {mk_init_name}')
                    mk_views_name = os.path.join(mk_app_name, views_name)
                    with open(mk_views_name, 'w') as f: f.write("This is views.py")
                    print(f"Created file at: {mk_views_name}")
                    mk_static_name = os.path.join(mk_app_name, static_directory_name)
                    os.mkdir(mk_static_name)
                    print(f"Created direcotry at: {mk_static_name}")
                    mk_templates_name = os.path.join(mk_app_name, template_directory_name)
                    os.mkdir(mk_templates_name)
                    print(f"Created directory at: {mk_templates_name}")
                    mk_stylesheet_name = os.path.join(mk_static_name, stylesheet_name)
                    with open(mk_stylesheet_name, 'w') as f: f.write('This is styles.css')
                    print(f'Created file at: {mk_stylesheet_name}')
                    mk_template_name = os.path.join(mk_templates_name, index_name)
                    with open(mk_template_name, 'w') as f:f.write("This is index.html")
                    print(f'Created file at: {mk_template_name}')
        elif os.path.isdir(path) == False:print(f"{path} is not a directory")
        

checkArgs(args)
