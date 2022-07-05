from flask import Blueprint, request, jsonify
from . import models

bp = Blueprint('reptile',__name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        body = request.get_json()
        print(body)
        new_reptile = models.Reptile(reptile= body['reptile'], description=body['reptile_discription'])
        models.db.session.add(new_reptile)
        models.db.sesson.commit()

    results = models.Reptile.query.all()

    return jsonify([results.to_json() for reptile in results])


@bp.route('/<int:id>')
def show(id): 
    reptile = models.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'Name': reptile.reptile,
        'Description': reptile.reptile_dscription
        
    }

    return reptile_dict


# @bp.route('/<int:id>')
# def show(id):
#     reptile = reptiles[id -1 ]