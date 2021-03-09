from flask import render_template, jsonify, request, redirect, url_for
from create_app import create_app
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
    search_lst = Vacancy.search_vacancies(page, 10, keywords)
    pages = [page for page in search_lst.iter_pages(left_edge=2, left_current=2, right_current=3, right_edge=2)]
    return jsonify(jobs=[vacancy.dict() for vacancy in search_lst.items], totalPages=pages)


@app.route('/jobs/<int:job_id>')
def job(job_id):
    vacancy = Vacancy.find_by_id(job_id)
    if vacancy:
        return render_template('job.html', job=vacancy)
    else:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0')
