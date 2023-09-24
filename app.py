from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask em execução!...' 

@app.route('/<nome>')
def home_nome(nome):
    return f'Hello, {nome}'

if __name__=='_main_':
    app.run(debug=True)
