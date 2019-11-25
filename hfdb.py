import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://dbNTT:123456A@cluster0-shard-00-00-4ghnr.mongodb.net:27017,cluster0-shard-00-01-4ghnr.mongodb.net:27017,cluster0-shard-00-02-4ghnr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.NTTRUNG


def insert_food(name,pic,address,duong,quan,tinh):
    db.hatfood.insert_one({'name': name,'pic':pic,'address':address,'duong':duong,'quan':quan,'tinh':tinh})


# def find_food_by_id(food_id):
#     return db.hatfood.find_one({'_id': ObjectId(food_id)})


# def update_by_id(food_id, new_name, new_price):
#     food = find_food_by_id(food_id)
#     food['name'] = new_name
#     food['price'] = new_price
#     db.foods.save(food)


# def delete_by_id(food_id):
#     db.foods.delete_one({'_id': ObjectId(food_id)})
def get_all_food():
    return list(db.hatfood.find())
def search_by_addr(tinh,quan,duong):
    ls=[]
    ls_food=get_all_food()
    for i in range(len(ls_food)):
        if ls_food[i]['tinh']==tinh and ls_food[i]['quan']==quan and ls_food[i]['duong']==duong:
            ls.append(ls_food[i])
    return ls
def search_by_key(food):
    ls=[]
    ls_f=get_all_food()
    for i in range(len(ls_f)):
        if ls_f[i]['name'].find(food)!=-1:
            ls.append(ls_f[i])
    return ls
def check_food(ad):
    kt=0
    ls_f=get_all_food()
    for i in range(len(ls_f)):
        if ls_f[i]['address']==ad:
            kt=0
            break
        else:
            kt=1
    return kt
# print(check_food("314 Bà Triệu, Quận Hai Bà Trưng, Hà Nội"))
# print(get_all_food())

