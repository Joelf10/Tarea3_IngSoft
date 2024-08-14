python -m doctest -v test_api2.py

from api import ConsultaMedica, RegistroConsultas
from mockito import when, verify

def test_consulta_medica():
    #Prueba de creación de un objeto ConsultaMedica.
    
    >>> consulta = ConsultaMedica("Paciente 1", "Doctor 1", "2024-01-10", 100.0)
    >>> consulta.paciente
    'Paciente 1'
    >>> consulta.doctor
    'Doctor 1'
    >>> consulta.fecha
    '2024-01-10'
    >>> consulta.pago
    100.0
    

def test_registro_consultas():  
    #Prueba de los métodos de RegistroConsultas.
    
    >>> registro = RegistroConsultas()
    >>> consulta = ConsultaMedica("Paciente 1", "Doctor 1", "2024-01-10", 100.0)
    >>> registro.agregar_consulta(consulta)
    >>> len(registro.obtener_consultas())
    1
    >>> registro.obtener_consultas()[0]['paciente']
    'Paciente 1'
    >>> registro.borrar_todas_consultas()
    >>> len(registro.obtener_consultas())
    0
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Ejemplo de uso de Mockito
    registro = RegistroConsultas()
    consulta = ConsultaMedica("Paciente Mock", "Doctor Mock", "2024-01-10", 100.0)

    # Mocking del método agregar_consulta
    when(registro).agregar_consulta(consulta).thenReturn(None)
    
    # Verificar que se llamó al método
    registro.agregar_consulta(consulta)
    verify(registro, times=1).agregar_consulta(consulta)
