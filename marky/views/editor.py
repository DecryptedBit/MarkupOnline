from flask import current_app, Blueprint, render_template, jsonify

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.route('/')
def index():
    return render_template('editor/index.html')

@editor.route('/<identifier>')
def ide(identifier):
    return render_template('editor/editor.html')

@editor.route('/test')
def ide_test():
    return render_template('editor/tmp.html')