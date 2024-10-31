from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/respuesta',methods=['post'])
def respuesta():
    nom = str(request.form['nombre'])
    mensaje = str(request.form['mensaje'])
    return render_template('formulario.html', res=nom, men=mensaje)

@app.route('/sobre')
def sobre():
    return render_template('sobre mi.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')


@app.route('/facebook')
def facebook():
    return render_template('https://web.facebook.com/profile.php?id=100041065063181')

@app.route('/linkedin')
def linkedin():
    return render_template('https://www.linkedin.com/in/the-ghost-787778327/')

if __name__ == '__main__':
    app.run(debug=True)   


