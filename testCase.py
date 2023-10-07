import unittest
import requests
import json

class APITestCase(unittest.TestCase):
    def test_get_word(self):
        response = requests.get('http://localhost:5000/api/word')
        data = json.loads(response.text)

        self.assertEqual(response.status_code, 200)
        self.assertIn('word', data)
        self.assertEqual(data['word'], 'Admin')

if __name__ == '__main__':
    unittest.main()
