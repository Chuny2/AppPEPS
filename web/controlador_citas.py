from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_cita(paciente_id, fecha,observaciones,tratamiento,costo):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO citas(paciente_id, fecha,observaciones,tratamiento,costo) VALUES (%s, %s,%s,%s,%s)",
                       (paciente_id, fecha,observaciones,tratamiento,costo))
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

def convertir_cita_a_json(cita, incluir_iva=False):
    d = {}
    d['paciente_id'] = cita[0]
    d['fecha'] = cita[1]
    d['observaciones'] = cita[2]
    d['tratamiento'] = cita[3]

    costo = cita[4]
    if costo is not None:  # Verificar si costo no es null
        try:
            costo_float = float(costo)  # Intentar convertir el costo a float
            if incluir_iva:
                costo_float += calculariva(costo_float)  # Calcular y añadir el IVA
            d['costo'] = costo_float
        except ValueError:
            print(f"Error al convertir el costo a número en la cita {cita[5]}")
            d['costo'] = None  # O asignar otro valor predeterminado en caso de error
    else:
        d['costo'] = 0  # Mantener costo como null si originalmente es null

    d['id'] = cita[5]
    return d

def calculariva(importe):
    return importe * 0.21

def obtener_citas():
    try:
        conexion = obtener_conexion()
        citasjson = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT paciente_id, fecha, observaciones, tratamiento, costo, id FROM citas")
            citas = cursor.fetchall()
            if citas:
                for cita in citas:
                    try:
                        citasjson.append(convertir_cita_a_json(cita, incluir_iva=True))
                    except ValueError:
                        print(f"Error al convertir el costo a número en la cita {cita[5]}")
        conexion.close()
        code = 200
    except Exception as e:
        print(f"Excepción al obtener las citas: {e}", file=sys.stdout)
        citasjson = []
        code = 500
    return citasjson, code


def obtener_cita_por_id(id):
    citajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento,foto FROM citas WHERE id = %s", (id,))
            cursor.execute("SELECT paciente_id, fecha,observaciones,tratamiento,costo,id FROM citas WHERE id =" + id)
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

def actualizar_cita(id, paciente_id, fecha, observaciones, tratamiento,costo):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE citas SET paciente_id = %s, fecha = %s, observaciones = %s, tratamiento = %s, costo= %s WHERE id = %s",
                       (paciente_id, fecha, observaciones, tratamiento,costo,id))
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
