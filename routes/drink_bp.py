from flask import Blueprint
from controllers.DrinkController import index, create, read, update, destroy

drink_bp = Blueprint('drink_bp', __name__)
drink_bp.route('/', methods=['GET'])(index)
drink_bp.route('/', methods=['POST'])(create)
drink_bp.route('/<int:id>', methods=['GET'])(read)
drink_bp.route('/<int:id>', methods=['PUT'])(update)
drink_bp.route('/<int:id>', methods=['DELETE'])(destroy)
