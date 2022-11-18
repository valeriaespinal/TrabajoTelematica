import flask, render_template, request, xlsxwriter, openpyxl

app1 = flask.Flask(__main__)
libro = xlsxwriter.Book('/data/basedatos.xlsx')
pagina = libro.add_sheet()
fila = 0
columna = 0

@app1.route('/') #url principal
def inicio():
	return "pagina de inicio de la red social"
@app1.route ('/inicio_sesion')
def iniciar_sesion():
        return render_template("/templates/iniciosesion.html")

@app1.route ('/iniciar_sesion')
def iniciar():
        correo = request.form['correo']
        clave = request.form['clave']
        ps = openpyxl.load_workbook('basedatos.xlsx')
        pagina1 = ps['Sheet1']
        correo_existe = False
        for columna in range(1, pagina1.max_row + 1):
                correo1 = pagina1['B' + str(columna)].value
                if(correo1==correo):
                        correo_existe = True
                        if(pagina1['C' + str(columna)].value=clave):
                                return ("Sesión correctamente iniciada")
                        else return("La clavae es incorrecta.")

        if(correo_existe = False):
                return("El correo no existe.")

@app1.route('/registro')
def registrar:
	return render_template("registro.html")
@app1.route ('/crear_usuario',methods=['POST'])
def crear():
	nombre_comp = request.form['nombre_comp']
	correo = request.form['correo']
	clave = request.form['clave']
	
	contenido = [nombre, correo, clave]
	
	for elemento in contenido:
		pagina.write(fila, columna, elemento)
		columna += 1

	fila += 1
	
	
return "Su nombre es " + nombre_comp + ", su correo es " + correo + ", inicie sesión con su correo y contraseña "
	


@app1.route ('/crear_perfil')
def crear_perfil():
	return "crear perfil"

@app1.route ('/cerrar_sesion')
def cerrar_sesion():
	return render_template('/templates/cerrar_sesion.html')

@app1.route ('/irperfil')
def navegar_perfil():
        
	return "navegando por un perfil publico"


@app1.route ('/irperfilprivado')
def navegar_perfil_priv():
	return "navegando por un perfil privado"



if __name__ == ‘__main__’:
	app1.run(host=’0.0.0.0’, port=80)
