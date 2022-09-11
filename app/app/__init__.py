
from flask import Flask
from .views import views
from .auth import auth 

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.register_blueprint( auth , url_prefix='/') 

app.config['SECRET_KEY'] = 'mysecretkey'
                        