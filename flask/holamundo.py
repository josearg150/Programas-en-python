from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'
    
#GET, POST, PUT, PATCH, DELETE

@app.route('/post/<post_id>', methods=['GET', 'POST'])
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


@app.route('/lele')
def lele():
    return 'lele'