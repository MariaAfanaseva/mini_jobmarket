from flask import Blueprint, render_template, request, jsonify

from models.vacancy import Vacancy

search_page = Blueprint('search_page', __name__,
                        static_folder='static/search/dist/',
                        static_url_path='/')


@search_page.route('/')
def index():
    return search_page.send_static_file('index.html')


@search_page.route('/search')
def search():
    page = request.args.get('page', 1, type=int)
    keywords = request.args.getlist('keyword')
    search_lst = Vacancy.search_vacancies(page, 10, keywords)
    pages = [page for page in search_lst.iter_pages(left_edge=2, left_current=2, right_current=3, right_edge=2)]
    return jsonify(jobs=[vacancy.dict() for vacancy in search_lst.items], totalPages=pages)
