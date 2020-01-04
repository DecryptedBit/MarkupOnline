from flask import current_app, Blueprint, render_template, jsonify, send_from_directory

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.route('/')
def index():
    return render_template('editor/index.html')

@editor.route('/<identifier>')
def ide(identifier):
    return render_template('editor/editor.html')

@editor.route('/serve')
def serve():
    return send_from_directory(current_app.static_folder, 
                               'sample.pdf', 
                               mimetype='application/pdf')