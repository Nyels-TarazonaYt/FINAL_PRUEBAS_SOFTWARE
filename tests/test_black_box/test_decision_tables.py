import unittest
from app import app

class TestDecisionTables(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_detalle_producto(self):
        response = self.app.get('/producto/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa', response.data)  # Ajuste el texto para que coincida con el nombre real del producto

    def test_producto_no_existente(self):
        response = self.app.get('/producto/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
