import unittest
from app import app

class TestStateTransitions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_estado_inicial_y_final(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa', response.data)

        response = self.app.get('/producto/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Camisa de algod\xc3\xb3n', response.data)

if __name__ == '__main__':
    unittest.main()
