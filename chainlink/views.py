#!/usr/bin/python2.7
__author__ = 'Matthew Smith'
#Standard libraries
import json


import operator
#supported 3rd party packages
from chainlink import app
from flask import render_template
import bitly_api

#project sprecific imports
import BitlyConf
import chainlink_util


@app.route('/')
def index():
    return render_template('chain.html')

@app.route('/owf')
def owf():
    return render_template('owf.html')


@app.route('/search/<keyword>/<int:number>')
def search(keyword,number):
    print keyword

    try:
        b = bitly_api.Connection(access_token=BitlyConf.get_access_token())
        links = b.search(keyword,limit=number)
    except bitly_api.BitlyError as e:
        print e
        return e
    print len(links)
    #build the return elements
    frequencies = chainlink_util.get_freqs(links)
    #calculate metadata
    top_word = max(frequencies.iteritems(), key=operator.itemgetter(1))[0]
    ret = {'words':frequencies,
           'top_word':top_word,
           'title':keyword or "No Term Given",
           }
    return json.dumps(ret)

@app.route('/searchTest')
def searchTest():
    s = ''
    with open('/opt/bitly_test_data') as f:
        for line in f:
            s += line
    d = json.loads(s)
    links = d['data']['results']
    frequencies = chainlink_util.get_freqs(links)
    top_word = max(frequencies.iteritems(), key=operator.itemgetter(1))[0]
    ret = {'words':frequencies,
       'top_word':top_word,
       'title': 'cybersecurity',
       }
    return json.dumps(ret)

##########NOT COMPLETED YET!!! ############
@app.route('/hot')
def hot():
    b = bitly_api.Connection(access_token=BitlyConf.get_access_token())
    try:
        phrases = b.realtime_bursting_phrases()
    except Exception as e:
        ret = {"chainlink_error":'Error on bitly side, try again later.'}
        return json.dumps(ret)

    top_phrase = max(phrases.iteritems(), key=operator.itemgetter(1))[0]
    ret = chainlink_util.process_phrase(top_phrase)

###########################################
