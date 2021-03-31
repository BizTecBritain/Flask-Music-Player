import os
from flask import render_template, request, flash, redirect, url_for, jsonify, make_response
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from . import main
from manage import app


home_visit = False

@main.route('/healthcheck')
def healthcheck():
    return "200"


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    global home_visit
    home_visit = True
    return render_template('music/home.html')

@main.route('/play', methods=['GET', 'POST'])
def player():
    if home_visit:
        music_folder = app.config['MUSIC_FOLDER']
        music_list = os.listdir(music_folder)
        return render_template('music/play.html', music_list = music_list)
    else:
        home()