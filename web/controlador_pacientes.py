from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_paciente(nombre, apellido, direccion,telefono):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pacientes(nombre, apellido,direccion,telefono) VALUES (%s, %s,%s,%s)",
                       (nombre, apellido, direccion, telefono))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un paciente", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_paciente_a_json(paciente):
    d = {}
    d['id'] = paciente[0]
    d['nombre'] = paciente[1]
    d['apellido'] = paciente[2]
    d['direccion'] = paciente[3]
    d['telefono'] = paciente[4]
    return d

def obtener_pacientes():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, apellido, direccion,telefono FROM pacientes")
            pacientes = cursor.fetchall()
            pacientesjson=[]
            if pacientes:
                for paciente in pacientes:
                    pacientesjson.append(convertir_paciente_a_json(paciente))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los pacientes", file=sys.stdout)
        pacientesjson=[]
        code=500
    return pacientesjson,code

def obtener_paciente_por_id(id):
    pacientejson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento,foto FROM pacientes WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, apellido, direccion,telefono FROM pacientes WHERE id =" + id)
            paciente = cursor.fetchone()
            if paciente is not None:
                pacientejson = convertir_paciente_a_json(paciente)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un paciente", file=sys.stdout)
        code=500
    return pacientejson,code


def eliminar_paciente(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM pacientes WHERE id = %s", (id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un paciente", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_paciente(id, nombre, apellido, direccion, telefono):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE pacientes SET nombre = %s, apellido = %s, direccion = %s, telefono = %s WHERE id = %s",
                       (nombre, apellido, direccion, telefono,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un paciente", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
