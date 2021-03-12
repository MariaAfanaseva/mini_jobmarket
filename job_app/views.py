from flask import Blueprint, render_template, redirect, url_for

from models.vacancy import Vacancy

job_page = Blueprint('job_page', __name__,
                     url_prefix='/jobs',
                     static_folder='static',
                     static_url_path='/',
                     template_folder='templates')


@job_page.route('/<int:job_id>')
def job(job_id):
    vacancy = Vacancy.find_by_id(job_id)
    if vacancy:
        return render_template('job.html', job=vacancy)
    else:
        return redirect(url_for('search_page.index'))
