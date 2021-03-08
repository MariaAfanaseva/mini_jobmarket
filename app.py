from create_app import create_app
from flask import render_template, jsonify, request
from models.category import Category
from models.vacancy import Vacancy

app = create_app('development')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    page = request.args.get('page', 1, type=int)
    keywords = request.args.getlist('keyword')
    search_lst = Vacancy.search_vacancies(page, 5, keywords)
    return jsonify(jobs=[vacancy.dict() for vacancy in search_lst])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
