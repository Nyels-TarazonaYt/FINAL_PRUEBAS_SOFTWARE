#Cobertura de Sentencias
import unittest
from app import app

class TestStatementCoverage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_detalle_producto(self):
        response = self.app.get('/producto/1')  # Verifica que la URL es correcta
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa', response.data)  # Ajuste el texto para que coincida con el nombre real del producto

if __name__ == '__main__':
    unittest.main()
