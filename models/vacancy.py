from databases.sql_db import db


class Vacancy(db.Model):
    __tablename__ = "vacancies"

    id = db.Column(db.String(128), primary_key=True, unique=True)
    title = db.Column(db.String(255), nullable=False)
    firm = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    workplace_postcode = db.Column(db.Integer())
    workplace = db.Column(db.String(128))
    from_date = db.Column(db.Date())
    job_link = db.Column(db.String(128))
    job_type = db.Column(db.String(80))

    def __init__(self, vacancy_id, title, firm, description,
                 workplace_postcode, workplace,
                 from_date, job_link, job_type):
        self.id = vacancy_id
        self.title = title
        self.firm = firm
        self.description = description
        self.workplace_postcode = workplace_postcode
        self.workplace = workplace
        self.from_date = from_date
        self.job_link = job_link
        self.job_type = job_type

    def __repr__(self):
        return f'{self.title}'

    @classmethod
    def find_by_id(cls, vacancy_id):
        return cls.query.filter_by(id=vacancy_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
