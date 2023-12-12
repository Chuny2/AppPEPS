from flask import request, session
import json
import decimal
from __main__ import app
import controlador_pacientes

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/pacientes",methods=["GET"])
def pacientes():
    pacientes,code= controlador_pacientes.obtener_pacientes()
    return json.dumps(pacientes, cls = Encoder),code

@app.route("/paciente/<id>",methods=["GET"])
def paciente_por_id(id):
    paciente,code = controlador_pacientes.obtener_paciente_por_id(id)
    return json.dumps(paciente, cls = Encoder),code

@app.route("/pacientes",methods=["POST"])
def guardar_paciente():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        paciente_json = request.json
        ret,code=controlador_pacientes.insertar_paciente(paciente_json["nombre"], paciente_json["apellido"], (paciente_json["direccion"]), (paciente_json["telefono"]))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/pacientes/<id>", methods=["DELETE"])
def eliminar_paciente(id):
    ret,code=controlador_pacientes.eliminar_paciente(id)
    return json.dumps(ret), code

@app.route("/pacientes", methods=["PUT"])
def actualizar_paciente():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        paciente_json = request.json
        ret,code=controlador_pacientes.actualizar_paciente(paciente_json["id"],paciente_json["nombre"], paciente_json["apellido"], (paciente_json["direccion"]), (paciente_json["telefono"]))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code