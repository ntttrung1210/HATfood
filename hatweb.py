from flask import Flask, render_template,request, redirect, url_for, session
from hfdb import*
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html',data=get_all_food())

@app.route('/trangmieng')
def trangmieng():
    return render_template('trangmieng.html',data=get_trangmieng())
  
# @app.route('/search/food')
# def func_name(foo):
#     return render_template('expression')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 