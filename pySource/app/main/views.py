import os
from flask import render_template, request, flash, redirect, url_for, jsonify, make_response
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from . import main
from manage import app




@main.route('/healthcheck')
def healthcheck():
    return "200"


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('music/home.html', music_list = music_list)

@main.route('/play', methods=['GET', 'POST'])
def player():
    music_folder = app.config['MUSIC_FOLDER']
    music_list = os.listdir(music_folder)
    return render_template('music/play.html', music_list = music_list)
