import json

item = ["book", "pen", "pencil", "paper", "notebook"]
quantity = [100, 200, 300, 400, 500]
price = [500, 400, 300, 200, 100]
buyer = ["Masha", "Dasha", "Sasha", "Glasha", "Misha"]
date = ["01.01.2019", "02.01.2019", "03.01.2019", "04.01.2019", "05.01.2019"]
parameters = [item, quantity, price, buyer, date]
def list_to_dict(lst_name):
    dictionary={}
    for i in range (len(lst_name)):
        dictionary[i] = lst_name[i]
    return dictionary

def write_order_to_json():
    for param in parameters:
        dict_to_json = list_to_dict(param)
        print(dict_to_json)
        
        with open ("orders.json", 'a') as f_n:
            json.dump(dict_to_json, f_n, sort_keys=True, indent=2)
        with open ("orders.json") as f_n:
            print(f_n.read())
        

write_order_to_json()
