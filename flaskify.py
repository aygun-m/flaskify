#!/usr/bin/python3
from sys import argv
import os
version = '1.3'
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
                    main_file = f"""from {webapp_name} import app
app.run(debug=True)"""
                    views_file = f"""from flask import Blueprint, render_template, request, session, url_for
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')"""
                    #Blueprints handling
                    if blueprints == []:
                        init_file = f"""from flask import Flask
from .views import views
app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.config['SECRET_KEY'] = 'mysecretkey'"""
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
                                string += ''
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
                    mk_webapp_name = os.path.join(dir, webapp_name)
                    os.mkdir(mk_webapp_name)
                    print(f"Created directory at: {mk_webapp_name}")
                    mk_main_name = os.path.join(mk_webapp_name, main_name)
                    with open(mk_main_name, 'w') as f:f.write(main_file)
                    print(f"Created file at: {mk_main_name}")
                    mk_app_name = os.path.join(mk_webapp_name, webapp_name)
                    os.mkdir(mk_app_name)
                    print(f"Created directory at: {mk_app_name}")
                    mk_init_name = os.path.join(mk_app_name, init_name)
                    with open(mk_init_name, 'w') as f: f.write(init_file)
                    print(f'Created file at: {mk_init_name}')
                    mk_views_name = os.path.join(mk_app_name, views_name)
                    with open(mk_views_name, 'w') as f: f.write(views_file)
                    print(f"Created file at: {mk_views_name}")
                    mk_static_name = os.path.join(mk_app_name, static_directory_name)
                    os.mkdir(mk_static_name)
                    print(f"Created directory at: {mk_static_name}")
                    mk_templates_name = os.path.join(mk_app_name, template_directory_name)
                    os.mkdir(mk_templates_name)
                    print(f"Created directory at: {mk_templates_name}")
                    mk_js_file = os.path.join(mk_static_name, js_name)
                    with open(mk_js_file, 'w') as f:f.write("")
                    print(f"Created file at: {mk_js_file}")
                    mk_stylesheet_name = os.path.join(mk_static_name, stylesheet_name)
                    with open(mk_stylesheet_name, 'w') as f: f.write("""* {
    margin:0;
    padding:0;
    box-sizing:border-box;
}""")
                    print(f'Created file at: {mk_stylesheet_name}')
                    mk_template_name = os.path.join(mk_templates_name, index_name)
                    with open(mk_template_name, 'w') as f:f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="{{url_for('static', filename='styles.css')}}">
    <script src="{{url_for('static', filename='index.js')}}"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
</head>
<body>
    
</body>
</html>""")
                    print(f'Created file at: {mk_template_name}')
                    if blueprints != []:
                        for x in blueprints:
                            if x[-3:] != '.py': x+='.py'
                            path = os.path.join(dir, webapp_name)
                            path = os.path.join(path, webapp_name)
                            path = os.path.join(path, x)
                            f = open(path, 'w')
                            if x[-3:] == '.py': x=x[:-3]
                            f.write(f"""from flask import Blueprint, render_template, request, session, url_for
{x} = Blueprint('{x}', __name__)""")
                            f.close()
                    if stylesheets != []:
                        for x in stylesheets:
                            if x[-4:] != '.css': x+='.css'
                            path = os.path.join(dir, webapp_name)
                            path = os.path.join(path, f'{webapp_name}/static')
                            path = os.path.join(path, x)
                            with open(path, 'w') as f:f.write("")
                    if templates != []:
                        for x in templates:
                            if x[-5:] != '.html': x+= '.html'
                            path = os.path.join(dir, webapp_name)
                            path = os.path.join(path, f'{webapp_name}/templates')
                            path = os.path.join(path, x)
                            with open(path, 'w') as f:f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="{{url_for('static', filename='styles.css')}}">
    <script src="{{url_for('static', filename='index.js')}}"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>""")
        elif os.path.isdir(path) == False:print(f"{path} is not a directory")
checkArgs(args)
#felsef