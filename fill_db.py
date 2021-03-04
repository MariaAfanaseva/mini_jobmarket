from xml.dom import minidom
from databases.sql_db import db
from models.category import Category
from models.vacancy import Vacancy
from create_app import create_app
import datetime


class UpdateDb:

    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    @staticmethod
    def clear_db():
        db.drop_all()
        db.create_all()

    def _parse_xml(self):
        data = minidom.parse(self.xml_file_path)
        records = data.getElementsByTagName('record')
        return records

    def fill_categories(self):
        records = self._parse_xml()
        categories = set()

        for record in records:
            category_names = record.getElementsByTagName('category')[0].firstChild.data
            for name in category_names.split(', '):
                if name not in categories:
                    categories.add(name)
                    category = Category(name=name)
                    category.save_to_db()

    def fill_vacancies(self):
        records = self._parse_xml()

        for record in records:
            vacancy_id = record.getElementsByTagName('id')[0].firstChild.data
            title = record.getElementsByTagName('titel')[0].firstChild.data
            firm = record.getElementsByTagName('firma')[0].firstChild.data
            text = record.getElementsByTagName('volltext')[0].firstChild.data
            postcode = record.getElementsByTagName('plz_arbeitsort')[0].firstChild.data
            workplace = record.getElementsByTagName('arbeitsort')[0].firstChild.data
            from_date = record.getElementsByTagName('vondatum')[0].firstChild.data
            job_link = record.getElementsByTagName('stellenlink')[0].firstChild.data
            job_type = record.getElementsByTagName('jobtype')[0].firstChild.data
            category_names = record.getElementsByTagName('category')[0].firstChild.data

            day, month, year = from_date.split('-')
            from_date = datetime.date(int(year), int(month), int(day))
            vacancy = Vacancy(vacancy_id=vacancy_id, title=title, firm=firm, description=text,
                              workplace_postcode=postcode, workplace=workplace,
                              from_date=from_date, job_link=job_link, job_type=job_type)
            vacancy.save_to_db()
            for name in category_names.split(', '):
                category = Category.find_by_name(name=name)
                category.vacancies.append(vacancy)
                category.save_to_db()

    def recreate_db(self):
        self.clear_db()
        self.fill_categories()
        self.fill_vacancies()


if __name__ == '__main__':
    app = create_app("development")
    with app.app_context():
        update = UpdateDb(xml_file_path='data/jobs_feed.xml')
        update.recreate_db()
