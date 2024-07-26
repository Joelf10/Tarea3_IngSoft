from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Base de datos de usuarios (simulada)
usuarios = [
    {"nombre": "august", "contraseña": "pass1", "fecha_nacimiento": "01/01/1990", "cedula": "1234567890"},
    # Agrega más usuarios según sea necesario
]

# Doctores disponibles
doctores_disponibles = [
    {"nombre": "Alberto", "contraseña": "pass_doc1"},
    {"nombre": "Bob", "contraseña": "pass_doc2"},
    {"nombre": "Caseres", "contraseña": "pass_doc3"},
    # Puedes agregar más doctores según sea necesario
]

# Citas disponibles (específicas)
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

# Almacena la asignación de doctor y fecha por usuario
asignaciones_doctores_fechas = {}

@app.route('/')
def index():
    return render_template('main_pacientes.html', usuario=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        contraseña = request.form['contraseña']

        # Verificación de usuario
        for usuario in usuarios:
            if usuario['nombre'] == nombre_usuario and usuario['contraseña'] == contraseña:
                return redirect(url_for('main_pacientes', usuario=nombre_usuario))

        # Verificación de doctor
        for doctor in doctores_disponibles:
            if doctor['nombre'] == nombre_usuario and doctor['contraseña'] == contraseña:
                return render_template('main_consultas.html', usuario=nombre_usuario)

        return 'Usuario o contraseña incorrectos'

    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        contraseña = request.form['contraseña']
        fecha_nacimiento = request.form['fecha_nacimiento']
        cedula = request.form['cedula']

        # Registro de usuario
        usuarios.append({
            'nombre': nombre_usuario,
            'contraseña': contraseña,
            'fecha_nacimiento': fecha_nacimiento,
            'cedula': cedula
        })

        return redirect(url_for('login'))

    return render_template('registro.html')

@app.route('/registro_doctor', methods=['GET', 'POST'])
def registro_doctor():
    if request.method == 'POST':
        nombre_doctor = request.form['nombre']
        contraseña_doctor = request.form['contraseña']

        # Registro de doctor
        doctores_disponibles.append({
            'nombre': nombre_doctor,
            'contraseña': contraseña_doctor
        })

        return redirect(url_for('login'))

    return render_template('registro_doctor.html')

@app.route('/citas/<usuario>', methods=['GET', 'POST'])
def citas(usuario):
    asignacion = asignaciones_doctores_fechas.get(usuario, {})

    if request.method == 'POST':
        if 'fecha_cita' in request.form:
            fecha_seleccionada = datetime.strptime(request.form['fecha_cita'], '%Y-%m-%d')

            if fecha_seleccionada in fechas_disponibles and fecha_seleccionada not in asignacion.get('fechas', []):
                asignacion['fechas'] = [fecha_seleccionada]
                asignacion['doctor'] = request.form['doctor']

                # Almacena la información seleccionada para el usuario
                asignaciones_doctores_fechas[usuario] = asignacion

                # Imprime para depurar
                print(asignaciones_doctores_fechas)

                # Redirección a la página de main_pacientes después de programar una cita
                return redirect(url_for('main_pacientes', usuario=usuario))

    return render_template('citas.html', usuario=usuario, asignacion=asignacion, fechas_disponibles=fechas_disponibles, doctores_disponibles=doctores_disponibles)

@app.route('/main_pacientes/<usuario>', methods=['GET'])
def main_pacientes(usuario):
    return render_template('main_pacientes.html', usuario=usuario)

@app.route('/main_consultas', methods=['GET'])
def main_consultas():
    print(asignaciones_doctores_fechas)  # Añade esta línea para imprimir en la consola
    return render_template('main_consultas.html', asignaciones_doctores_fechas=asignaciones_doctores_fechas)

@app.route('/eliminar_asignacion/<usuario>', methods=['POST'])
def eliminar_asignacion(usuario):
    asignaciones_doctores_fechas.pop(usuario, None)
    return redirect(url_for('login', usuario=usuario))



if __name__ == '__main__':
    app.run(debug=True)
