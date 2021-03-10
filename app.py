from flask import render_template, jsonify, request, redirect, url_for
from create_app import create_app
from models.category import Category
from models.vacancy import Vacancy

app = create_app('development')


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('search_page.index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
