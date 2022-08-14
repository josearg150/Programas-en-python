#from crypt import methods
from flask import Flask, render_template, request, url_for,redirect,abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'
    
#GET, POST, PUT, PATCH, DELETE

@app.route('/post/<post_id>')
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este no es el metodo get'


# @app.route('/post/<post_id>', methods=['GET'])
# def lala(post_id):
#     return 'El id del post es: ' + post_id

# @app.route('/post/<post_id>', methods=['POST'])
# def lili(post_id):
#     return 'El id del post es: ' + post_id


@app.route('/lele', methods = ['POST','GET'])
def lele():
    #abort(401)
    ##return redirect(url_for('lala', post_id = 2))
    #print(url_for('index'))
    #print(url_for('lala',post_id=2))
    #print(request.form)
    #print(request.form['llave1'])
    #return render_template('lele.html')
    return {
        "username": 'perrito feliz',
        "email": 'perrito@feliz.com'
    }