import unittest
from create_app import create_app
from fill_db import UpdateDb
from databases.sql_db import db
from models.category import Category
from models.vacancy import Vacancy


class ModelMethodsTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

        with self.app_context:
            update = UpdateDb(xml_file_path='data/test_feed.xml')
            update.recreate_db()

    def test_get_category_by_name(self):
        with self.app_context:
            category = Category.find_by_name('Medizin')
            self.assertEqual('Medizin', category.name)

    def test_get_jobs_by_category(self):
        with self.app_context:
            category = Category.find_by_name('Medizin')
            jobs = category.get_vacancies(3)
            self.assertEqual(3, len(list(jobs)))
            for job in jobs:
                category_names = [category.name for category in job.categories]
                self.assertIn('Medizin', category_names)

    def test_get_job_by_id(self):
        with self.app_context:
            job = Vacancy.find_by_id(3)
            self.assertEqual(3, job.id)

    def test_get_job_data(self):
        with self.app_context:
            job = Vacancy.find_by_id(3).dict()
            self.assertEqual(dict, type(job))
            self.assertIn('id', job)
            self.assertIn('title', job)
            self.assertIn('location', job)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app_context:
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
