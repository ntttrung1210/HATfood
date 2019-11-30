import pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb://dbNTT:123456A@cluster0-shard-00-00-4ghnr.mongodb.net:27017,cluster0-shard-00-01-4ghnr.mongodb.net:27017,cluster0-shard-00-02-4ghnr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.NTTRUNG


def insert_food(name, pic, address, duong, quan, tinh):
    db.hatfood.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh})

def insert_doc(name,pic,link):
    db.document.insert_one({'name':name,'pic':pic,'link':link})

def insert_content(content):
    db.content.insert_one({'content':content})

def get_all_content():
    return list(db.content.find())

def get_all_food():
    return list(db.hatfood.find())

def get_all_doc():
    return list(db.document.find())

def get_trangmieng():
    return list(db.trangmieng.find())

def get_sang():
    return list(db.sang.find())

def get_khuya():
    return list(db.khuya.find())

def get_trua():
    return list(db.trua.find())

def get_toi():
    return list(db.toi.find())


def get_doan():
    return list(db.doan.find())


def get_monlau():
    return list(db.monlau.find())


def get_hot():
    return list(db.hot.find())


def get_viahe():
    return list(db.viahe.find())


def get_mipho():
    return list(db.mipho.find())


def search_by_addr(tinh, quan, duong):
    ls = []
    ls_food = get_all_food()
    for i in range(len(ls_food)):
        if ls_food[i]['tinh'] == tinh and ls_food[i]['quan'] == quan and ls_food[i]['duong'] == duong:
            ls.append(ls_food[i])
    return ls


def search_by_key(food):
    ls = []
    ls_f = get_all_food()
    for i in range(len(ls_f)):
        if ls_f[i]['name'].find(food) != -1:
            ls.append(ls_f[i])
    return ls


def check_food(ad):
    kt = 0
    ls_f = get_all_food()
    for i in range(len(ls_f)):
        if ls_f[i]['address'] == ad:
            kt = 0
            break
        else:
            kt = 1
    return kt


def insert_trangmieng(name, pic, address):
    db.trangmieng.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_doan(name, pic, address):
    db.doan.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_monlau(name, pic, address):
    db.monlau.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_viahe(name, pic, address):
    db.viahe.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_mipho(name, pic, address):
    db.mipho.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_sang(name, pic, address):
    db.sang.insert_one({'name': name, 'pic': pic, 'address': address})

def insert_khuya(name, pic, address):
    db.khuya.insert_one({'name': name, 'pic': pic, 'address': address})


def insert_trua(name, pic, address):
    db.trua.insert_one({'name': name, 'pic': pic, 'address': address})



def insert_toi(name, pic, address):
    db.toi.insert_one({'name': name, 'pic': pic, 'address': address})

def insert_hot(name, pic, address):
    db.hot.insert_one({'name': name, 'pic': pic, 'address': address})

