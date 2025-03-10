from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecreto'  # Necesario para usar flash()

# Devuelve el template index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<edad>')
def saludo(nombre, edad):
    return f"¡Hola {nombre}, tienes {edad} años!"

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['username']
    password = request.form['password']
    if usuario == 'admin' and password == 'admin':
        return redirect(url_for('admin'))  
    flash('Usuario o contraseña incorrectos', 'error')  # Envía un mensaje de error a la vista
    return redirect(url_for('index'))  # Redirige a index con el mensaje

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')



# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=80)