from flask import Blueprint, render_template

list_blueprint = Blueprint('list', __name__)

@list_blueprint.route('/list')
def list():
    return render_template('/list.html')