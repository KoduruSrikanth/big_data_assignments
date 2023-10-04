import json
from random import randint

# I am generating the data of an inventory will be having the fields like product_id, product, description, warehouse and quantity.

id = []
for i in range(1, 9):
    id.append(i)

# I created a list of products, desctiption, warehouse numbers which will be assigned to each document randomly using the random package that is imported.

products = ['chocolate', 'biscuits', 'ice cream',
            'waffles', 'beans', 'spinach', 'chicken', 'fish']

desc = ['manufactured by melody', 'made by parle', 'manufacturer: coldstone',
        'made by yummy inc', 'black beans', 'fresh leafy vegetable', 'chicken breasts', 'frozen salmon']

warehouse_nums = [1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241]

qty = [5 ,6 ,8, 9, 1, 3, 7, 4]

data_json_final = []

# The below for loop creates a jsno structure having 8 documents
for i in range(0, 8):
    data_json = {
        'product_id': id[i],
        'product': products[randint(0, len(products) - 1)], # creating the products randomly
        'description': desc[randint(0, len(desc) - 1)],
        'warehouse': warehouse_nums[randint(0, len(warehouse_nums) - 1)],
        'quantity': qty[i]
    }
    data_json_final.append(data_json)

print(data_json_final)

# Now i wrote the output of the jsnon to another file -- inventory_json.jsno 

with open("inventory_json.json", 'w') as json_file:
    json.dump(data_json_final, json_file, indent=4)