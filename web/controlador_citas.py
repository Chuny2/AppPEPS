from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_cita(paciente_id, fecha_hora,observaciones,tratamiento,costo):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO citas(paciente_id, fecha_hora,observaciones,tratamiento,costo) VALUES (%s, %s,%s,%s,%f)",
                       (paciente_id, fecha_hora,observaciones,tratamiento,costo))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un cita", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_cita_a_json(cita):
    d = {}
    d['paciente_id'] = cita[0]
    d['fecha_hora'] = cita[1]
    d['observaciones'] = cita[2]
    d['tratamiento'] = cita[3]
    d['costo'] = cita[4]
    return d

def obtener_citas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT paciente_id, fecha_hora,observaciones,tratamiento,costo FROM citas")
            citas = cursor.fetchall()
            citasjson=[]
            if citas:
                for cita in citas:
                    citasjson.append(convertir_cita_a_json(cita))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los citas", file=sys.stdout)
        citasjson=[]
        code=500
    return citasjson,code

def obtener_cita_por_id(id):
    citajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento,foto FROM citas WHERE id = %s", (id,))
            cursor.execute("SELECT paciente_id, fecha_hora,observaciones,tratamiento,costo FROM citas WHERE id =" + id)
            cita = cursor.fetchone()
            if cita is not None:
                citajson = convertir_cita_a_json(cita)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un cita", file=sys.stdout)
        code=500
    return citajson,code


def eliminar_cita(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM citas WHERE id = %s", (id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un cita", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_cita(id, paciente_id, fecha_hora, observaciones, tratamiento,costo):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE citas SET paciente_id = %s, fecha_hora = %s, observaciones = %s, tratamiento = %s, costo= %f WHERE id = %s",
                       (paciente_id, fecha_hora, observaciones, tratamiento,costo,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un cita", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
