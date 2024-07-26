from flask import Flask,jsonify,request, abort
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import datetime
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app,allow_headers=['*'])

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://localhost:5000/swagger'  # Our API url (can of course be a local resource)

# Base de datos de usuarios (simulada)
usuarios = [
    {"nombre": "august", "contraseña": "pass1", "fecha_nacimiento": "01/01/1990", "cedula": "1234567890"},
    {'nombre': 'joel', 'contraseña': '123'}
]

# Doctores disponibles
doctores_disponibles = [
    {"nombre": "Alberto", "contraseña": "pass_doc1"},
    {"nombre": "Bob", "contraseña": "pass_doc2"},
    {"nombre": "Caseres", "contraseña": "pass_doc3"},
    {"nombre": "doctor1", "contraseña": "123"},
    # Puedes agregar más doctores según sea necesario
]

# Almacena la asignación de doctor y fecha por usuario
asignaciones_doctores_fechas = {}


fechas_disponibles = [
    datetime(2024, 1, 10),
    datetime(2024, 1, 11),
    datetime(2024, 1, 12),
    datetime(2024, 1, 13),
    datetime(2024, 1, 14),
    datetime(2024, 1, 15),
    datetime(2024, 1, 16),
    datetime(2024, 1, 17),
    datetime(2024, 1, 18),
    datetime(2024, 1, 19),
]

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

@app.route('/api/registrar_consulta', methods=['POST'])
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
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

@app.route('/api/consultas', methods=['GET'])
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

@app.route('/api/borrar_consultas', methods=['DELETE'])
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

@app.route('/api/login', methods=['POST'])
def login():
  """
    Login
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: Login
          required:
            - nombre
            - contraseña
          properties:
            nombre:
              type: string
            contraseña:
              type: string
    responses:
      201:
        description: Login exitoso, datos del usuario y el rol
    """
  if not 'nombre' in request.json or not 'contraseña' in request.json:
    return {'error':'Debe enviar el nombre y contraseña en formato JSON'},400
  nombre_usuario = request.json['nombre']
  contraseña = request.json['contraseña']

  # Verificación de usuario
  for usuario in usuarios:
    if usuario['nombre'] == nombre_usuario and usuario['contraseña'] == contraseña:
      return jsonify({
        'rol': 'usuario',
        'nombre':usuario['nombre'],            
      })

  # Verificación de doctor
  for doctor in doctores_disponibles:
    if doctor['nombre'] == nombre_usuario and doctor['contraseña'] == contraseña:
      return jsonify({
        'rol': 'doctor',
        'nombre': doctor['nombre'],
      })
  
  return {'error':'Credenciales incorrectas!'}, 400

@app.route('/api/registro', methods=['POST'])
def registro():
  """
    Registro
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: Registro
          required:
            - nombre
            - contraseña
            - fecha_namiento
            - cedula
          properties:
            nombre:
              type: string
            contraseña:
              type: string
            fecha_nacimiento:
              type: string
            cedula:
              type: string
    responses:
      201:
        description: Login exitoso, datos del usuario y el rol
  """
  if not 'nombre' in request.json or not 'contraseña' in request.json or not 'fecha_nacimiento' in request.json or not 'cedula' in request.json:
    return {'error': 'Debe enviar todo los campos'},400
  nombre_usuario = request.json['nombre']
  contraseña = request.json['contraseña']
  fecha_nacimiento = request.json['fecha_nacimiento']
  cedula = request.json['cedula']

  # Registro de usuario
  usuarios.append({
    'nombre': nombre_usuario,
    'contraseña': contraseña,
    'fecha_nacimiento': fecha_nacimiento,
    'cedula': cedula
  })

  return request.json

@app.route('/api/registro_doctor', methods=['POST'])
def registro_doctor():
  """
    Registro Doctor
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: RegistroDoctor
          required:
            - nombre
            - contraseña
          properties:
            nombre:
              type: string
            contraseña:
              type: string
    responses:
      201:
        description: Login exitoso, datos del usuario y el rol
  """
  if not 'nombre' in request.json or not 'contraseña' in request.json:
    return {'error': 'Debe enviar todo los campos'}, 400
     
  nombre_doctor = request.json['nombre']
  contraseña_doctor = request.json['contraseña']

  # Registro de doctor
  doctores_disponibles.append({
    'nombre': nombre_doctor,
    'contraseña': contraseña_doctor
  })
  
  return request.json

@app.route('/api/citas/<usuario>', methods=['GET'])
def citas(usuario):
  """
    Consultar cita
    ---
    parameters:
      - in: path
        name: usuario
        required: true
        schema:
          type: string
    responses:
      201:
        description: Cita medica del usuario
  """
  return asignaciones_doctores_fechas.get(usuario, {})

@app.route('/api/citas/<usuario>', methods=['POST'])
def crear_cita(usuario):
  """
    Crear cita
    ---
    parameters:
      - in: path
        name: usuario
        required: true
        schema:
          type: string
      - in: body
        name: body
        schema:
          id: CrearCita
          required:
            - fecha_cita
            - doctor
          properties:
            fecha_cita:
              type: string
            doctor:
              type: string
    responses:
      201:
        description: Cita medica del usuario
  """
  asignacion = asignaciones_doctores_fechas.get(usuario, {})
  fecha_seleccionada = datetime.strptime(request.json['fecha_cita'], '%Y-%m-%d')

  if fecha_seleccionada in fechas_disponibles and fecha_seleccionada not in asignacion.get('fechas', []):
    asignacion['fechas'] = [fecha_seleccionada]
    asignacion['doctor'] = request.json['doctor']

    # Almacena la información seleccionada para el usuario
    asignaciones_doctores_fechas[usuario] = asignacion
  return asignaciones_doctores_fechas.get(usuario, {})

@app.route('/api/citas/<usuario>', methods=['DELETE'])
def eliminar_cita(usuario):
  """
    Eliminar cita
    ---
    parameters:
      - in: path
        name: usuario
        required: true
        schema:
          type: string
    responses:
      201:
        description: Cita eliminada
  """
  asignaciones_doctores_fechas.pop(usuario, None)
  return usuario

@app.route('/api/datos-citas', methods=['GET'])
def datos_citas():
  """
    Datos para la citas
    ---
    responses:
      201:
        description: Datos generales
  """
  return {'fechas_disponibles':fechas_disponibles, 'doctores_disponibles':doctores_disponibles}

@app.route('/api/asignaciones', methods=['GET'])
def asignaciones():
  """
    Obtener consultas
    ---
    responses:
      201:
        description: Consultas
  """
  return {'asignaciones': asignaciones_doctores_fechas}

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