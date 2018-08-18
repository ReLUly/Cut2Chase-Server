#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from server import app
from mkcloud.main import mkcloud
from flask import request, url_for
from image2text.statement import url_to_full_text
import os, urllib.request

@app.route('/')
def summarize():
    try: 
        request_json = request.get_json()
        image_url = request_json['image_url'] # image URL
        # user_id = request_json['user_id'] # hashed user key

        basedir = os.path.dirname(os.path.realpath(__file__))
        upload_path = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        
        # urllib.request.urlretrieve(image_url, os.path.join(upload_path, userid)) # save current file

        full_text = url_to_full_text(image_url, 'ko') # OCR 

        # PageRank

        # return '' # return summarized text
        return full_text

    except: 
        return 'Error' # maybe?

@app.route('/wordcloud', methods=['GET', 'POST'])
def wordcloud():
    # receive text & app theme as JSON
    request_json = request.get_json()
    
    frequency = request_json['frequency']
    gradient_start = request_json['theme_start']
    gradient_end = request_json['theme_end']
    user_id = request_json['user_id'] # hashed user key

    filename = 'clouds/' + user_id + '.png'
    # get word frequency -> mkcloud with theme colors
    mkcloud('./server/static/' + filename, frequency, gradient_start, gradient_end)

    return url_for('static', filename=filename)
