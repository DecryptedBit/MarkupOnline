from flask import current_app, Blueprint, render_template, jsonify, send_from_directory, request
from flask_login import login_required, current_user
from mark_one.services.compiler import compile_md
from mark_one.models import Project

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.route('/')
@login_required
def index():
    projects = Project.query.filter(Project.user_id == current_user.id).all()
    return render_template('editor/index.html', projects=projects)

@editor.route('/<pid>')
@login_required
def ide(pid):
    return render_template('editor/editor.html')

@editor.route('/write/<pid>', methods=['POST'])
@login_required
def write_markdown(pid):
    """Write current Markdown project
       to the database.
    """
    project = Project.query.get_or_404(pid)

    if request.method == 'POST':
        data = request.get_json()

        if data:
            md = data['markdown']
            
            project.markdown = md
            db.session.commit()

    return data

@editor.route('/read/<pid>', methods=['GET'])
@login_required
def read_markdown(pid):
    """Read current stored Markdown project
       from the database.
    """
    project = Project.query.get_or_404(pid)

    if request.method == 'GET':
        data = None

    return data


@editor.route('/serve')
@login_required
def serve_md():
    """Function for testing purposes only..."""
    # print('CURRENT APP FOLDER: ', current_app.static_folder)
    # return send_from_directory(current_app.static_folder + '/uploads', 
    #                            'test.pdf', 
    #                            mimetype='application/pdf')
    pass

@editor.route('/serve_pdf')
@login_required
def serve_pdf():
    """Function for testing purposes only..."""
    print('CURRENT APP FOLDER: ', current_app.static_folder)
    return send_from_directory(current_app.static_folder + '/uploads', 
                               'test.pdf', mimetype='application/pdf')

@editor.route('/compile_pdf', methods=['POST'])
@login_required
def compile_to_pdf():
    """Function for testing purposes only..."""
    if request.method == 'POST':
        data = request.get_json()

        if data:
            md = data['markdown']
            compile_md(md, current_app.config['UPLOAD_FOLDER'] + 'test.pdf')

    return data
