#!/usr/bin/python
import sys
import html
import werkzeug
from flask import g
from flask import Flask
from flask import abort
from flask import request
from flask import render_template
from classes.series import Series
from classes.seriesmanager import SeriesManager
from classes.statusenum import Status
from config import global_config as config

app = Flask(__name__)
manager = SeriesManager()

@app.route('/')
@app.route('/edit', methods=['GET'])
@app.route('/edit/', methods=['GET'])
@app.route('/search', methods=['GET'])
@app.route('/search/', methods=['GET'])
@app.route('/list', methods=['GET'])
@app.route('/list/', methods=['GET'])
@app.route('/list/<filter>', methods=['GET'])
def list(filter='all'):
    if filter == 'all':
        list_items=manager.get_all()
    else:
        list_items=manager.get_by_status(filter)
    g.cfg = config
    return render_template('listing.html'
            , filter_name=filter.title()
            , list_items=list_items)

@app.route('/download', methods=['GET'])
def downloads():
    return 'downloads'

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    item=manager.get_by_id(id)
    if not item: return not_found(404)
    g.cfg = config
    return render_template('details.html'
            , item=item
            , all_status=Status.get_all())

@app.route('/search/<term>', methods=['GET'])
def search(term):
    list_items=manager.get_by_name(term)
    if not list_items: return not_found(404, term)
    g.cfg = config
    return render_template('listing.html'
            , filter_name=term
            , list_items=list_items)

@app.route('/test', methods=['GET'])
@app.route('/test/<testvar>', methods=['GET'])
def test(testvar=None):
    s = Series()
    s.name = 'Ore no Imouto ga Konnani Kawaii Wake ga Nai'
    s.add_alt_name = 'OreImo'
    s.add_alt_name = 'My Little Sister Can\'t Be This Cute'
    s.season = 2
    s.episode = 16
    s.status = 'finished'
    s.add_genre = 'Comedy'
    s.add_genre = 'Seinen'
    s.nsfw = 'sfw'
    s.type = 'TV'
    s.year = 2010
    s.notes = 'notes here'
    s.url = 'http://myanimelist.net/anime/8769/Ore_no_Imouto_ga_Konnani_Kawaii_Wake_ga_Nai'
    manager.add_series(s)
    return str(s)

@app.errorhandler(404)
@app.errorhandler(werkzeug.exceptions.NotFound)
def not_found(code, search_term=None):
    g.cfg = config
    return render_template('not-found.html'
            , search_term=search_term), 404

