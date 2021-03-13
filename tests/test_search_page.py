import unittest
import json
from create_app import create_app
from fill_db import UpdateDb
from databases.sql_db import db
from models.category import Category


class SearchPageTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.test_data = 5
        self.app_context = self.app.app_context()

        with self.app_context:
            update = UpdateDb(xml_file_path='data/test_feed.xml')
            update.recreate_db()

    def test_get_jobs(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(list, type(data['totalPages']))
            self.assertEqual(self.test_data, len(data['jobs']))
            self.assertEqual(1, len(data['totalPages']))

    def test_get_jobs_with_location(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'where': 'Schwerin'})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(1, len(data['jobs']))
            self.assertEqual(1, len(data['totalPages']))

    def test_get_jobs_with_keyword(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'keyword': 'Oberarzt'})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(4, len(data['jobs']))
            self.assertEqual(1, len(data['totalPages']))

    def test_get_jobs_with_keyword_and_location(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'where': 'Schwerin',
                                                'keyword': 'Oberarzt',
                                                'page': 1})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(1, len(data['jobs']))
            self.assertEqual(1, len(data['totalPages']))

    def test_get_jobs_with_wrong_page(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'page': 2})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(0, len(data['jobs']))
            self.assertEqual(1, len(data['totalPages']))

    def test_get_jobs_with_wrong_location(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'where': 'dddddddd'})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(0, len(data['jobs']))
            self.assertEqual(0, len(data['totalPages']))

    def test_get_jobs_with_wrong_keyword(self):
        with self.app_context:
            res = self.client.get('/search',
                                  headers={"Content-Type": "application/json"},
                                  query_string={'keyword': 'aaaaaaa'})
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertEqual(list, type(data['jobs']))
            self.assertEqual(0, len(data['jobs']))
            self.assertEqual(0, len(data['totalPages']))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app_context:
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
