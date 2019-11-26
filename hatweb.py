from flask import Flask, render_template,request, redirect, url_for, session
from hfdb import*
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html',data=get_all_food())
@app.route('/templates/abouthat.html')
def bmi():
    return render_template('abouthat.html')
# @app.route('/templates/abouthat.html',methods=['POST'])
# # def bmi1():
# #   return render_template('abouthat.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 