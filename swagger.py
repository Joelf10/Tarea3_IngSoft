from flask import Flask,jsonify,request
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://localhost:5000/swagger'  # Our API url (can of course be a local resource)

class ConsultaMedica:
    def __init__(self, paciente, doctor, fecha, pago):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.pago = pago

class RegistroConsultas:
    def __init__(self):
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)

    def obtener_consultas(self):
        return [vars(consulta) for consulta in self.consultas]

    def borrar_todas_consultas(self):
        self.consultas = []

registro = RegistroConsultas()

@app.route("/swagger")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Api Consultas medicas"
    return jsonify(swag)

@app.route('/registrar_consulta', methods=['POST'])
def registrar_consulta():
    """
        Registrar una consulta
        ---
        parameters:
          - in: body
            name: body
            schema:
              id: Consulta
              required:
                - doctor
                - paciente
                - pago
              properties:
                doctor:
                  type: string
                paciente:
                  type: string
                pago:
                  type: number
        responses:
          201:
            description: Consulta registrada con éxito
    """
    datos_consulta = request.get_json()
    paciente = datos_consulta['paciente']
    doctor = datos_consulta['doctor']
    
    # Verificar si se proporcionó la fecha en el cuerpo de la solicitud
    if 'fecha' in datos_consulta:
        fecha = datos_consulta['fecha']
    else:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pago = datos_consulta['pago']

    nueva_consulta = ConsultaMedica(paciente, doctor, fecha, pago)
    registro.agregar_consulta(nueva_consulta)

    print(f"Datos de la consulta recibidos: {datos_consulta}")

    # Incluir la fecha en la respuesta JSON
    response_data = {
        "mensaje": "Consulta registrada con éxito",
        "fecha_registro": fecha
    }

    return jsonify(response_data)

@app.route('/consultas', methods=['GET'])
def obtener_consultas():
    """
        Obtener consultas
        ---
        responses:
          200:
            description: Listado obtenido con éxito
            content:
            application/json:
                example: [{"paciente": "Baltazar Andrade", "doctor": "Pedro Cazares"}]
    """
    consultas = registro.obtener_consultas()
    return jsonify({"consultas": consultas})

@app.route('/borrar_consultas', methods=['DELETE'])
def borrar_todas_consultas():
    """
    Borrar todas las consultas
    ---
    delete:
        responses:
          200:
            description: Listado eliminado con éxito
    """
    registro.borrar_todas_consultas()
    return jsonify({"mensaje": "Todas las consultas han sido eliminadas"})


# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Consultas medicas"
    },
)

app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
