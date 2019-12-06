import pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb://dbNTT:123456A@cluster0-shard-00-00-4ghnr.mongodb.net:27017,cluster0-shard-00-01-4ghnr.mongodb.net:27017,cluster0-shard-00-02-4ghnr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.NTTRUNG


def insert_food(name, pic, address, duong, quan, tinh,link):
    db.hatfood.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})

def insert_doc(name, pic, address, duong, quan, tinh,link):
    db.document.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})

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

def check_name(ls,name):
    dk=1
    for i in range(len(ls)):
        if ls[i]['name']==name:
            dk=0
            break
        else:
            dk=1
    return dk
s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s

def search_by_addr(tinh, quan, duong):
    ls = []
    tinh=remove_accents(tinh).lower()
    quan=remove_accents(quan).lower()
    duong=remove_accents(duong).lower()
    ls_food = get_all_food()
    ls_f=get_all_food()
    for i in range(len(ls_food)):
        ls_food[i]['duong']=remove_accents(ls_food[i]['duong']).lower()
        ls_food[i]['quan']=remove_accents(ls_food[i]['quan']).lower()
        ls_food[i]['tinh']=remove_accents(ls_food[i]['tinh']).lower()
    for i in range(len(ls_food)):
        if ls_food[i]['tinh'] == tinh and ls_food[i]['quan'] == quan and ls_food[i]['duong'] == duong and check_name(ls,ls_f[i]['name'])==1:
            ls.append(ls_f[i])
    return ls

def search_by_key(food):
    ls = []
    ls_f = get_all_food()
    ls_f1= get_all_food()
    food=food.lower()
    for i in range(len(ls_f)):
        ls_f[i]['name']=ls_f[i]['name'].lower()
    for i in range(len(ls_f)):
        if ls_f[i]['name'].find(food)!=-1 and check_name(ls,ls_f1[i]['name'])==1:
            ls.append(ls_f1[i])
    for i in range(len(ls_f)):
        ls_f[i]['name']=ls_f[i]['name'].lower()
        ls_f[i]['name']=remove_accents(ls_f[i]['name'])
    food=remove_accents(food).lower()
    for i in range(len(ls_f)):
        if ls_f[i]['name'].find(food)!=-1 and check_name(ls,ls_f1[i]['name'])==1:
            ls.append(ls_f1[i])
    dem=0
    for i in range(len(ls_f)):
        new1=ls_f[i]['name'].split()
        new2=food.split()
        for j in range(len(new2)):
            for k in range(len(new1)):
                if new1[k]==new2[j] and check_name(ls,ls_f1[i]['name'])==1:
                    dem=dem+1
                    break  
        if float(dem/len(new2))>0.9 and check_name(ls,ls_f1[i]['name'])==1:
                ls.append(ls_f1[i])
        if float(dem/len(new2))>0.8 and check_name(ls,ls_f1[i]['name'])==1:
                ls.append(ls_f1[i])
        if float(dem/len(new2))>0.75 and check_name(ls,ls_f1[i]['name'])==1:
                ls.append(ls_f1[i])
        if float(dem/len(new2))>0.5 and check_name(ls,ls_f1[i]['name'])==1:
                ls.append(ls_f1[i])
        
        dem=0
    return ls


def check_food(ad):
    kt = 0
    ls_f = get_all_food()
    for i in range(len(ls_f)):
        if ls_f[i]['address'] != ad:
            kt = 1
        else:
            kt=0
            break
    return kt


def insert_trangmieng(name, pic, address, duong, quan, tinh,link):
    db.trangmieng.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_doan(name, pic, address, duong, quan, tinh,link):
    db.doan.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_monlau(name, pic, address, duong, quan, tinh,link):
    db.monlau.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_viahe(name, pic, address, duong, quan, tinh,link):
    db.viahe.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_mipho(name, pic, address, duong, quan, tinh,link):
    db.mipho.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_sang(name, pic, address, duong, quan, tinh,link):
    db.sang.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})

def insert_khuya(name, pic, address, duong, quan, tinh,link):
    db.khuya.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})


def insert_trua(name, pic, address, duong, quan, tinh,link):
    db.trua.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})



def insert_toi(name, pic, address, duong, quan, tinh,link):
    db.toi.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})

def insert_hot(name, pic, address, duong, quan, tinh,link):
    db.hot.insert_one({'name': name, 'pic': pic, 'address': address,
                           'duong': duong, 'quan': quan, 'tinh': tinh,'link':link})

