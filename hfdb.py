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

