import flask
app2 = flask.Flask(__main__)

@app2.route('/') #url principal
def inicio():
	return "pagina de inicio del perfil del usuario”

@app2.route('/cerrar_sesión’) 
def cerrar():
	return "borrar_perfil"

@app2.route('/borrar_perfil') 
def borrar():
	return "borrar perfil"
