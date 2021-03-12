from databases.sql_db import db


class Vacancy(db.Model):
    __tablename__ = "vacancies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    firm = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    location_postcode = db.Column(db.Integer())
    location = db.Column(db.String(128))
    from_date = db.Column(db.Date())
    job_link = db.Column(db.String(128))
    job_type = db.Column(db.String(80))

    def __init__(self, title, firm, description,
                 location_postcode, location,
                 from_date, job_link, job_type):
        self.title = title
        self.firm = firm
        self.description = description
        self.location_postcode = location_postcode
        self.location = location
        self.from_date = from_date
        self.job_link = job_link
        self.job_type = job_type

    def __repr__(self):
        return f'{self.title}'

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location
        }

    @classmethod
    def find_by_id(cls, vacancy_id):
        return cls.query.filter_by(id=vacancy_id).first()

    @classmethod
    def _create_keywords_conditions(cls, keywords):
        conditions = []
        for keyword in keywords:
            conditions.append(cls.title.ilike(f'%{keyword}%'))
            conditions.append(cls.description.ilike(f'%{keyword}%'))
            conditions.append(cls.firm.ilike(f'%{keyword}%'))
        return conditions

    @classmethod
    def _create_location_conditions(cls, locations):
        conditions = []
        for location in locations:
            conditions.append(cls.location.ilike(f'%{location}%'))
        return conditions

    @classmethod
    def search_vacancies(cls, page, quantity, keywords, locations):
        data = cls.query
        if locations:
            locations_conditions = cls._create_location_conditions(locations)
            data = data.filter(db.and_(*locations_conditions))
        if keywords:
            keywords_conditions = cls._create_keywords_conditions(keywords)
            data = data.filter(db.or_(*keywords_conditions))
        return data.order_by(cls.from_date.desc()).paginate(page, quantity, error_out=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
