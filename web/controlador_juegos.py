from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_juego(nombre, apellido, fecha_nacimientO):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pacientes(nombre, apellido, fecha_nacimiento) VALUES (%s, %s, %f)",
                       (nombre, apellido, fecha_nacimiento))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un juego", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_juego_a_json(juego):
    d = {}
    d['id'] = juego[0]
    d['nombre'] = juego[1]
    d['apellido'] = juego[2]
    d['fecha_nacimiento'] = juego[3]
    return d

def obtener_juegos():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento FROM pacientes")
            juegos = cursor.fetchall()
            juegosjson=[]
            if juegos:
                for juego in juegos:
                    juegosjson.append(convertir_juego_a_json(juego))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los juegos", file=sys.stdout)
        juegosjson=[]
        code=500
    return juegosjson,code

def obtener_juego_por_id(id):
    juegojson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento,foto FROM juegos WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento FROM pacientes WHERE id =" + id)
            juego = cursor.fetchone()
            if juego is not None:
                juegojson = convertir_juego_a_json(juego)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un juego", file=sys.stdout)
        code=500
    return juegojson,code


def eliminar_juego(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un juego", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_juego(id, nombre, apellido, fecha_nacimiento, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE pacientes SET nombre = %s, apellido = %s, fecha_nacimiento = %s WHERE id = %s",
                       (nombre, apellido, fecha_nacimiento, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un juego", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
