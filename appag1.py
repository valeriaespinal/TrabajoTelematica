import flask, render_template, request, xlsxwriter

app1 = flask.Flask(__main__)

@app1.route('/') #url principal
def inicio():
	return "pagina de inicio de la red social"

@app1.route ('/iniciar_sesion')
def iniciar():
	return "iniciar sesión"

@app1.route('/registro')
def registrar:
	return render_template("form.html")
@app1.route ('/crear_usuario')
def crear():
	nombre_comp = request.form['nombre_comp']
	correo = request.form['correo']
	clave = request.form['clave']
	libro = xlsxwriter.Book('/data/basedatos.xlsx')
	pagina = libro.add_sheet()
	fila = 0
	columna = 0
	contenido = [nombre, correo, clave]
	
	for elemento in contenido:
		pagina.write(fila, columna, elemento)
		columna += 1
	
	
return "Su nombre es " + nombre_comp + ", su correo es " + correo + ", inicie sesión con su correo y contraseña "
	


@app1.route ('/crear_perfil')
def crear_perfil():
	return "crear perfil"

@app1.route ('/cerrar_sesion')
def cerrar_sesion():
	return "cerrando sesión del usuario "

@app1.route ('/irperfil')
def navegar_perfil():
	return "navegando por un perfil publico"


@app1.route ('/irperfilprivado')
def navegar_perfil_priv():
	return "navegando por un perfil privado"



if __name__ == ‘__main__’:
	app1.run(host=’0.0.0.0’, port=80)
