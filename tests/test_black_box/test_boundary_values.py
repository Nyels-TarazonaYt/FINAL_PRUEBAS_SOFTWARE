import unittest
from app import app

class TestBoundaryValues(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_detalle_producto_limite_superior(self):
        # Realiza una solicitud al producto con el ID más alto
        response = self.app.get('/producto/2')  # Asegúrate de que el ID 2 exista en tu aplicación
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pantalones', response.data)

    def test_detalle_producto_limite_inferior(self):
        # Realiza una solicitud al producto con el ID más bajo
        response = self.app.get('/producto/1')  # Asegúrate de que el ID 1 exista en tu aplicación
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa', response.data)

    def test_detalle_producto_fuera_limite(self):
        # Realiza una solicitud al producto con un ID que no exista
        response = self.app.get('/producto/999')  # Asegúrate de que este ID no exista en tu aplicación
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
