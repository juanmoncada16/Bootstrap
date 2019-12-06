from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/reservaciones')
def reservaciones():
    return render_template('reservaciones.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')

if __name__ == '__main__':
    app.run()
