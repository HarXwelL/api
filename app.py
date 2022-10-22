from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion =MySQL(app)

#----------------------CRUD USUARIO -----------------------------
#LISTAR
@app.route('/usuarios')
def listar_usuarios():
    try:
        user = conexion.connection.cursor()
        sql = "SELECT * FROM Usuario"
        user.execute(sql)
        datos = user.fetchall()
        usuarios=[]
        for fila in datos:
            usuario={'id_usuario':fila[0],'nro_dni':fila[1], 'nombres':fila[2], 'apellidos':fila[3], 'direccion':fila[4], 'telefono':fila[5], 'correo':fila[6]}
            usuarios.append(usuario)
        return jsonify({'usuarios':usuarios, 'mensaje':'usuarios listados'})
    except Exception as ex:
        return jsonify({'mensaje':'ERROR CRITICO TE ENTRO VIRUS ALV'})

@app.route('/usuarios/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        user = conexion.connection.cursor()
        sql = "SELECT * FROM Usuario WHERE id_usuario = '{0}'".format(codigo)
        user.execute(sql)
        datos = user.fetchone()
        if datos != None:
            usuario = {'id_usuario':datos[0],'nro_dni':datos[1], 'nombres':datos[2], 'apellidos':datos[3], 'direccion':datos[4], 'telefono':datos[5], 'correo':datos[6]}
        return jsonify({'usuario':usuario, 'mensaje':'usuario encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})


#ENVIAR
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    try:
        user = conexion.connection.cursor()
        sql = "INSERT INTO Usuario (id_usuario, nro_dni, nombres, apellidos, direccion, telefono, correo, foto) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
            request.json['id_usuario'], request.json['nro_dni'], request.json['nombres'],
            request.json['apellidos'], request.json['direccion'], request.json['telefono'],
            request.json['correo'], request.json['foto'])
        user.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Usuario registrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR
@app.route('/usuarios/<codigo>', methods=['PUT'])
def actualizar_usuario(codigo):
    try:
        user = conexion.connection.cursor()
        sql = "UPDATE Usuario SET nro_dni = '{0}', nombres = '{1}', apellidos = '{2}', direccion = '{3}', telefono = '{4}', correo = '{5}', foto = '{6}' WHERE id_usuario = '{7}' ".format(
            request.json['nro_dni'], request.json['nombres'],
            request.json['apellidos'], request.json['direccion'], request.json['telefono'],
            request.json['correo'], request.json['foto'], codigo)
        user.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Usuario actualizado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ELIMINAR
@app.route('/usuarios/<codigo>', methods=['DELETE'])
def eliminar_usuario(codigo):
    try:
        user = conexion.connection.cursor()
        sql = "DELETE FROM Usuario WHERE id_usuario = '{0}'".format(codigo)
        user.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':'usuario eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})

#----------------------FIN CRUD USUARIO-----------------------------

#----------------------CRUD EVENTO -----------------------------
#LISTAR
@app.route('/eventos')
def listar_eventos():
    try:
        event = conexion.connection.cursor()
        sql = "SELECT id_evento, nombre, descripcion, aforo, ubicacion, estado, id_tipo_evento, id_usuario FROM Evento"
        event.execute(sql)
        dato = event.fetchall()
        eventos =[]
        for fila in dato:
            evento ={'id_evento':fila[0],'nombre':fila[1], 'descripcion':fila[2], 'aforo':fila[3], 'ubicacion':fila[4], 'estado':fila[5], 'id_tipo_evento':fila[6], 'id_usuario':fila[7]}
            eventos.append(evento)
        return jsonify({'eventos':eventos, 'mensaje':'eventos listados'})
    except Exception as ex:
        return jsonify({'mensaje':'ERROR CRITICO TE ENTRO VIRUS ALV'})

@app.route('/eventos/<codigo>', methods=['GET'])
def leer_evento(codigo):
    try:
        event = conexion.connection.cursor()
        sql = "SELECT id_evento, nombre, descripcion, aforo, ubicacion, estado, id_tipo_evento, id_usuario FROM Evento WHERE id_evento = '{0}'".format(codigo)
        event.execute(sql)
        datos = event.fetchone()
        if datos != None:
            evento = {'id_evento':datos[0],'nombre':datos[1], 'descripcion':datos[2], 'aforo':datos[3], 'ubicacion':datos[4], 'estado':datos[5], 'id_tipo_evento':datos[6], 'id_usuario':datos[7]}
        return jsonify({'evento':evento, 'mensaje':'evento encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})


#ENVIAR
@app.route('/eventos', methods=['POST'])
def registrar_evento():
    try:
        event = conexion.connection.cursor()
        sql = "INSERT INTO Evento (id_evento, nombre, descripcion, aforo, fecha, hora, ubicacion, imagen, estado, id_tipo_evento, id_usuario) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')".format(
            request.json['id_evento'], request.json['nombre'], request.json['descripcion'],
            request.json['aforo'], request.json['fecha'], request.json['hora'], request.json['ubicacion'], request.json['imagen'], request.json['estado'],
            request.json['id_tipo_evento'], request.json['id_usuario'])
        event.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Evento registrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR
@app.route('/eventos/<codigo>', methods=['PUT'])
def actualizar_evento(codigo):
    try:
        event = conexion.connection.cursor()
        sql = "UPDATE Evento SET nombre = '{0}', descripcion = '{1}', aforo = '{2}', fecha = '{3}', hora = '{4}', ubicacion = '{5}', imagen = '{6}' , estado = '{7}', id_tipo_evento = '{8}', id_usuario = '{9}' WHERE id_evento = '{10}' ".format(
            request.json['nombre'], request.json['descripcion'],
            request.json['aforo'], request.json['fecha'], request.json['hora'], request.json['ubicacion'], request.json['imagen'], request.json['estado'],
            request.json['id_tipo_evento'], request.json['id_usuario'], codigo)
        event.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Evento actualizado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ELIMINAR
@app.route('/eventos/<codigo>', methods=['DELETE'])
def eliminar_evento(codigo):
    try:
        event = conexion.connection.cursor()
        sql = "DELETE FROM Evento WHERE id_evento = '{0}'".format(codigo)
        event.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':'Evento eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})


#----------------------FIN CRUD EVENTO -----------------------------

#----------------------CRUD TIPO EVENTO -----------------------------
#LISTAR
@app.route('/tipo_eventos')
def listar_tipo_eventos():
    try:
        tevent = conexion.connection.cursor()
        sql = "SELECT * FROM Tipo_evento"
        tevent.execute(sql)
        dato = tevent.fetchall()
        teventos =[]
        for fila in dato:
            tevento ={'id_tipo_evento':fila[0],'descripcion':fila[1]}
            teventos.append(tevento)
        return jsonify({'tipo_eventos':teventos, 'mensaje':'tipo de eventos listados'})
    except Exception as ex:
        return jsonify({'mensaje':'ERROR CRITICO TE ENTRO VIRUS ALV'})

@app.route('/tipo_eventos/<codigo>', methods=['GET'])
def leer_tevento(codigo):
    try:
        tevent = conexion.connection.cursor()
        sql = "SELECT * FROM Tipo_evento WHERE id_tipo_evento = '{0}'".format(codigo)
        tevent.execute(sql)
        datos = tevent.fetchone()
        if datos != None:
            tevento = {'id_tipo_evento':datos[0],'descripcion':datos[1]}
        return jsonify({'tipo_evento':tevento, 'mensaje':'tipo de evento encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})

#ENVIAR
@app.route('/tipo_eventos', methods=['POST'])
def registrar_tevento():
    try:
        tevent = conexion.connection.cursor()
        sql = "INSERT INTO Tipo_evento (id_tipo_evento, descripcion) VALUES ('{0}', '{1}')".format(
            request.json['id_tipo_evento'], request.json['descripcion'])
        tevent.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Tipo de evento registrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR
@app.route('/tipo_eventos/<codigo>', methods=['PUT'])
def actualizar_tevento(codigo):
    try:
        tevent = conexion.connection.cursor()
        sql = "UPDATE Tipo_evento SET descripcion = '{0}' WHERE id_tipo_evento = '{1}' ".format(
            request.json['descripcion'], codigo)
        tevent.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Tipo de evento actualizado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ELIMINAR
@app.route('/tipo_eventos/<codigo>', methods=['DELETE'])
def eliminar_tevento(codigo):
    try:
        tevent = conexion.connection.cursor()
        sql = "DELETE FROM Tipo_evento WHERE id_tipo_evento = '{0}'".format(codigo)
        tevent.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':'Tipo de evento eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})


#----------------------FIN CRUD TIPO EVENTO -----------------------------

#----------------------CRUD INVITADO_EVENTO-----------------------------
#LISTAR
@app.route('/invitado_eventos')
def listar_invi_eventos():
    try:
        invi = conexion.connection.cursor()
        sql = "SELECT * FROM Invitado_Evento"
        invi.execute(sql)
        dato = invi.fetchall()
        invitados =[]
        for fila in dato:
            invitado ={'id_invitado_evento':fila[0],'id_usuario':fila[1],'id_evento':fila[2],'clave':fila[3]}
            invitados.append(invitado)
        return jsonify({'inivtado_eventos':invitados, 'mensaje':'invitados de evento listados'})
    except Exception as ex:
        return jsonify({'mensaje':'ERROR CRITICO TE ENTRO VIRUS ALV'})

@app.route('/invitado_eventos/<codigo>', methods=['GET'])
def leer_invi_evento(codigo):
    try:
        invi = conexion.connection.cursor()
        sql = "SELECT * FROM Invitado_Evento WHERE id_invitado_evento = '{0}'".format(codigo)
        invi.execute(sql)
        datos = invi.fetchone()
        if datos != None:
            invitado = {'id_invitado_evento':datos[0],'id_usuario':datos[1],'id_evento':datos[2],'clave':datos[3]}
        return jsonify({'tipo_evento':invitado, 'mensaje':'invitado de evento encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})



#ENVIAR
@app.route('/invitado_eventos', methods=['POST'])
def registrar_invi_evento():
    try:
        invi = conexion.connection.cursor()
        sql = "INSERT INTO Invitado_Evento (id_invitado_evento, id_usuario, id_evento, clave) VALUES ('{0}', '{1}', '{2}', '{3}')".format(
            request.json['id_invitado_evento'], request.json['id_usuario'], request.json['id_evento'], request.json['clave'])
        invi.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Invitado de evento registrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR
@app.route('/invitado_eventos/<codigo>', methods=['PUT'])
def actualizar_invi_evento(codigo):
    try:
        invi = conexion.connection.cursor()
        sql = "UPDATE Invitado_Evento SET id_usuario = '{0}', id_evento = '{1}', clave = '{2}' WHERE id_invitado_evento = '{3}' ".format(
            request.json['id_usuario'], request.json['id_evento'], request.json['clave'], codigo)
        invi.execute(sql)
        conexion.connection.commit() #confirma accion de insercion
        return jsonify({'mensaje': 'Invitado de evento actualizado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})



#ELIMINAR
@app.route('/invitado_eventos/<codigo>', methods=['DELETE'])
def eliminar_invi_evento(codigo):
    try:
        invi = conexion.connection.cursor()
        sql = "DELETE FROM Invitado_Evento WHERE id_invitado_evento = '{0}'".format(codigo)
        invi.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':'Invitado de evento eliminado.'})
    except Exception as ex:
        return jsonify({'mensaje':'NO ENCONTRADO'})


#----------------------FIN CRUD INVITADO EVENTO -----------------------------




def pagina_no_encontrada(error):
    return "<h1>ERROR NO SE QUE BUSCAS :P </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(port=5000)


