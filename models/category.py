from databases.sql_db import db

vacancy_categories = db.Table('vacancy_categories',
                              db.Column('vacancy_id',
                                        db.String,
                                        db.ForeignKey('vacancies.id'),
                                        primary_key=True),
                              db.Column('category_id',
                                        db.Integer,
                                        db.ForeignKey('categories.id'),
                                        primary_key=True)
                              )


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    vacancies = db.relationship('Vacancy', secondary=vacancy_categories, lazy='subquery',
                                backref=db.backref('categories', lazy=True))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
