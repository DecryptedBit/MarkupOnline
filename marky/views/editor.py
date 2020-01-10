from flask import current_app, Blueprint, render_template, jsonify, send_from_directory, request
from marky.services.compiler import compile_md

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.route('/')
def index():
    return render_template('editor/index.html')

@editor.route('/<identifier>')
def ide(identifier):
    return render_template('editor/editor.html')

@editor.route('/serve')
def serve():
    """Function for testing purposes only..."""
    print('CURRENT APP FOLDER: ', current_app.static_folder)
    return send_from_directory(current_app.static_folder + '/uploads', 
                               'test.pdf', 
                               mimetype='application/pdf')

@editor.route('/compile', methods=['POST'])
def compile():
    """Function for testing purposes only..."""
    if request.method == 'POST':
        data = request.get_json()

        if data:
            md = data['markdown']
            compile_md(md, current_app.config['UPLOAD_FOLDER'] + 'test.pdf')

    return data