from flask import send_from_directory
from . import main
import os

@main.route('/images/<path:filename>')
def download_file(filename):
    return send_from_directory("../../images/", filename, as_attachment=True)