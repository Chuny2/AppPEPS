from flask import request, session
import json
import decimal
from __main__ import app
import controlador_citas

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/citas",methods=["GET"])
def citas():
    citas,code= controlador_citas.obtener_citas()
    return json.dumps(citas, cls = Encoder),code

@app.route("/cita/<id>",methods=["GET"])
def cita_por_id(id):
    cita,code = controlador_citas.obtener_cita_por_id(id)
    return json.dumps(cita, cls = Encoder),code

@app.route("/citas",methods=["POST"])
def guardar_cita():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        cita_json = request.json
        ret,code=controlador_citas.insertar_cita(cita_json["paciente_id"],cita_json["fecha_hora"], cita_json["observaciones"], (cita_json["tratamiento"]), (cita_json["costo"]))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/citas/<id>", methods=["DELETE"])
def eliminar_cita(id):
    ret,code=controlador_citas.eliminar_cita(id)
    return json.dumps(ret), code

@app.route("/citas", methods=["PUT"])
def actualizar_cita():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        cita_json = request.json
        ret,code=controlador_citas.actualizar_cita(cita_json["id"],cita_json["paciente_id"],cita_json["fecha_hora"], cita_json["observaciones"], (cita_json["tratamiento"]), (cita_json["costo"]))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code