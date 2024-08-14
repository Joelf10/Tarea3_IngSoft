from api import ConsultaMedica, RegistroConsultas
from mockito import when, verify
import unittest

# Doctest
def test_consulta_medica():
    """
    Prueba de creación de un objeto ConsultaMedica.
   
    >>> consulta = ConsultaMedica("Paciente 1", "Doctor 1", "2024-01-10", 100.0)
    >>> consulta.paciente
    'Paciente 1'
    >>> consulta.doctor
    'Doctor 1'
    >>> consulta.fecha
    '2024-01-10'
    >>> consulta.pago
    100.0
    """

def test_registro_consultas():  
    """
    Prueba de los métodos de RegistroConsultas.
   
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
    """

# Unittest
class TestConsultaMedica(unittest.TestCase):
    def test_creacion_consulta_medica(self):
        consulta = ConsultaMedica("Paciente 1", "Doctor 1", "2024-01-10", 100.0)
        self.assertEqual(consulta.paciente, "Paciente 1")
        self.assertEqual(consulta.doctor, "Doctor 1")
        self.assertEqual(consulta.fecha, "2024-01-10")
        self.assertEqual(consulta.pago, 100.0)

class TestRegistroConsultas(unittest.TestCase):
    def test_agregar_consulta(self):
        registro = RegistroConsultas()
        consulta = ConsultaMedica("Paciente 1", "Doctor 1", "2024-01-10", 100.0)
        registro.agregar_consulta(consulta)
        self.assertEqual(len(registro.obtener_consultas()), 1)
        self.assertEqual(registro.obtener_consultas()[0]['paciente'], "Paciente 1")

    def test_borrar_consultas(self):
        registro = RegistroConsultas()
        registro.borrar_todas_consultas()
        self.assertEqual(len(registro.obtener_consultas()), 0)

if __name__ == "__main__":
    # Ejecutar Doctest
    import doctest
    doctest.testmod()

    # Ejecutar Unittest
    unittest.main(exit=False)

    # Ejemplo de uso de Mockito
    registro = RegistroConsultas()
    consulta = ConsultaMedica("Paciente Mock", "Doctor Mock", "2024-01-10", 100.0)

    # Mocking del método agregar_consulta
    when(registro).agregar_consulta(consulta).thenReturn(None)
   
    # Verificar que se llamó al método
    registro.agregar_consulta(consulta)
    verify(registro, times=1).agregar_consulta(consulta)
