from flask import Flask, render_template, request, redirect, url_for, session
from models.hfdb import *
from datetime import date,datetime
app = Flask(__name__)


# @app.route('/')
# def main_page():
#     b=len(get_all_food())
#     return render_template('index.html', data=get_all_food(),a=b,data_doc=get_all_doc())

@app.route('/')
def goi_y():
    now=datetime.now()
    ctime=int(now.strftime("%H"))
    b=len(get_all_food())
    if ctime<4 or ctime>=23:
        c='Gợi ý ăn khuya'
        return render_template('index.html', data1=get_khuya(),a=b,d=c,data_doc=get_all_doc(),data=get_all_food())
    elif ctime<10:
        c='Gợi ý ăn sáng'
        return render_template('index.html', data1=get_sang(),a=b,d=c,data_doc=get_all_doc(),data=get_all_food())
    elif ctime<15:
        c='Gợi ý ăn trưa'
        return render_template('index.html', data1=get_trua(),a=b,d=c,data_doc=get_all_doc(),data=get_all_food())
    else:
        c='Gợi ý ăn tối'
        return render_template('index.html', data1=get_toi(),a=b,d=c,data_doc=get_all_doc(),data=get_all_food())

@app.route('/2')
def hot2():
    b=len(get_all_food())
    return render_template('hot2.html', data=get_all_food(),a=b,data_doc=get_all_doc())

@app.route('/search_address')
def sear_address1():
    return render_template("search_address.html")

@app.route('/search_values', methods=['POST'])
def sear_address():
    duong=request.form.get("duong")
    quan=request.form.get("quan")
    tinh=request.form.get("tinh")
    ls=search_by_addr(tinh,quan,duong)
    a=len(ls)
    return render_template('search.html', data=ls, b=a,data_doc=get_all_doc())

@app.route('/3')
def hot3():
    b=len(get_all_food())
    return render_template('hot3.html', data=get_all_food(),a=b,data_doc=get_all_doc())

@app.route('/trangmieng')
def trangmieng():
    b=len(get_trangmieng())
    return render_template('doan.html', data=get_trangmieng(),a=b,data_doc=get_all_doc())


@app.route('/search', methods=['POST'])
def search():
    key_word = request.form.get("key_word")
    ls = search_by_key(key_word)
    a = len(ls)
    return render_template('search.html', data=ls, b=a,data_doc=get_all_doc())


@app.route('/doan')
def doan():
    b=len(get_doan())
    return render_template('doan.html', data=get_doan(),a=b,data_doc=get_all_doc())

@app.route('/hot')
def hot():
    b=len(get_hot())
    return render_template('doan.html', data=get_hot(),a=b,data_doc=get_all_doc())


@app.route('/monlau')
def monlau():
    b=len(get_monlau())
    return render_template('doan.html', data=get_monlau(),a=b,data_doc=get_all_doc())


@app.route('/viahe')
def viahe():
    b=len(get_viahe())
    return render_template('doan.html', data=get_viahe(),a=b,data_doc=get_all_doc())

@app.route('/sang')
def sang():
    b=len(get_viahe())
    return render_template('doan.html', data=get_sang(),a=b,data_doc=get_all_doc())


@app.route('/trua')
def trua():
    b=len(get_trua())
    return render_template('doan.html', data=get_trua(),a=b,data_doc=get_all_doc())

@app.route('/toi')
def toi():
    b=len(get_toi())
    return render_template('doan.html', data=get_toi(),a=b,data_doc=get_all_doc())


@app.route('/mipho')
def mipho():
    b=len(get_mipho())
    return render_template('doan.html', data=get_mipho(),a=b,data_doc=get_all_doc())

@app.route('/post1')
def post1():
    return render_template('post1.html',data_doc=get_all_doc())

@app.route('/post2')
def post2():
    return render_template('post2.html',data_doc=get_all_doc())

@app.route('/post3')
def post3():
    return render_template('post3.html',data_doc=get_all_doc())

@app.route('/advice')
def advice():
    return render_template('advice.html',data_doc=get_all_doc())

@app.route('/story_pizza')
def pizza():
    return render_template('pizza.html',data_doc=get_all_doc())

@app.route('/coffee')
def coffee():
    return render_template('coffee.html',data_doc=get_all_doc())


@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/bmi/thin')
def index_thin():
    return render_template('thin.html')

@app.route('/bmi/normal')
def index_normal():
    return render_template('normal.html')

@app.route('/bmi/fat')
def index_fat():
    return render_template('fat.html')

@app.route('/search_by_food')
def search_by_food():
    ls=get_hot()
    return render_template('search_by_food.html',data=ls,data_doc=get_all_doc())

@app.route('/search_by_key_word',methods=['POST'])
def search_by_key_word():
    key_word = request.form.get("key_word")
    ls = search_by_key(key_word)
    a = len(ls)
    return render_template('search_by_key_word.html',data_doc=get_all_doc(),data=ls,b=a)

if __name__ == '__main__':
    # dev
    # app.run(host='127.0.0.1', port=8000, debug=True)
    # deploy
    app.run(debug=False)
