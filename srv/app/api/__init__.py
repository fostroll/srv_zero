# -*- coding: utf-8 -*-

from flask import Blueprint, send_from_directory

from app import app


bp = Blueprint('api', __name__)

@bp.route('/<path:path>', methods=['GET'])
def static(path):
    return send_from_directory('static', path)
