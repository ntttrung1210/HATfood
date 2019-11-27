from flask import Flask, render_template, request, redirect, url_for, session
from hfdb import*
app = Flask(__name__)


@app.route('/')
def main_page():
    b=len(get_all_food())
    return render_template('index.html', data=get_all_food(),a=b)


@app.route('/trangmieng')
def trangmieng():
    b=len(get_trangmieng())
    return render_template('doan.html', data=get_trangmieng(),a=b)


@app.route('/search', methods=['POST'])
def search():
    key_word = request.form.get("key_word")
    ls = search_by_key(key_word)
    a = len(ls)
    return render_template('search.html', data=ls, b=a)


@app.route('/doan')
def doan():
    b=len(get_doan())
    return render_template('doan.html', data=get_doan(),a=b)


@app.route('/monlau')
def monlau():
    b=len(get_monlau())
    return render_template('doan.html', data=get_monlau(),a=b)


@app.route('/viahe')
def viahe():
    b=len(get_viahe())
    return render_template('doan.html', data=get_viahe(),a=b)


@app.route('/mipho')
def mipho():
    b=len(get_mipho())
    return render_template('doan.html', data=get_mipho(),a=b)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
