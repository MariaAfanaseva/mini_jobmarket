from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from databases.sql_db import db

"""

To create migrations folder: python manage.py db init
To make migrations: python manage.py db migrate
To update database: python manage.py db upgrade

"""

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
