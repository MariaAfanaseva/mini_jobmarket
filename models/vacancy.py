from databases.sql_db import db


class Vacancy(db.Model):
    __tablename__ = "vacancies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    firm = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    workplace_postcode = db.Column(db.Integer())
    workplace = db.Column(db.String(128))
    from_date = db.Column(db.Date())
    job_link = db.Column(db.String(128))
    job_type = db.Column(db.String(80))

    def __init__(self, title, firm, description,
                 workplace_postcode, workplace,
                 from_date, job_link, job_type):
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

    def dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

    @classmethod
    def find_by_id(cls, vacancy_id):
        return cls.query.filter_by(id=vacancy_id).first()

    @classmethod
    def _create_conditions(cls, keywords):
        conditions = []
        for keyword in keywords:
            conditions.append(cls.title.ilike(f'%{keyword}%'))
            conditions.append(cls.description.ilike(f'%{keyword}%'))
        return conditions

    @classmethod
    def search_vacancies(cls, page, quantity, keywords):
        if keywords:
            conditions = cls._create_conditions(keywords)
            return cls.query.filter(
                db.or_(*conditions)
            ).paginate(page, quantity, False)
        return cls.query.paginate(page=page, per_page=quantity, error_out=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
