from flask import current_app, Blueprint, render_template, jsonify, send_from_directory, request
from flask_login import login_required
from mark_one.services.compiler import compile_md

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.route('/')
@login_required
def index():
    return render_template('editor/index.html')

@editor.route('/<identifier>')
@login_required
def ide(identifier):
    return render_template('editor/editor.html')

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
                               'test.pdf', 
                               mimetype='application/pdf')

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
