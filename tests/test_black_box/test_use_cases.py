import unittest
from app import app

class TestUseCases(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ver_detalle_producto(self):
        response = self.app.get('/producto/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa', response.data)  # Ajusta el texto para que coincida con el nombre real del producto

if __name__ == '__main__':
    unittest.main()
