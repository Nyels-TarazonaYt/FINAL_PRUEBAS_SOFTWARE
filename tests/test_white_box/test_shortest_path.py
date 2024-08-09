#Camino más corto

import unittest
from app import app

class TestShortestPath(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_camino_mas_corto(self):
        response = self.app.get('/camino_mas_corto')  # Verifica que la URL es correcta
        self.assertEqual(response.status_code, 200)
        # Aquí puedes agregar más verificaciones según el contenido esperado de la respuesta

if __name__ == '__main__':
    unittest.main()
