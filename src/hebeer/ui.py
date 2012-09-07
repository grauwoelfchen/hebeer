# encoding: utf-8

from flask import g, request, render_template
from hebeer import app

@app.before_request
def before_filter():
    g.name = app.config['USERNAME'].title()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<int:repo_id>', methods=['GET'])
def show(repo_id):
    return render_template('show.html', repo_id=repo_id)

@app.route('/<int:repo_id>', methods=['POST', 'PUT'])
def run(repo_id):
    return render_template('show.html', repo_id=repo_id)
