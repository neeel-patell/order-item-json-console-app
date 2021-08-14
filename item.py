import json

class Item:
    
    def __init__(self):
        temp = json.load(open('items.json', 'r'))
        self.data = list(temp['items'])

    def get_latest_id(self):
        return (len(self.data)+1)

    def add(self):
        while(1):

            print("Enter 'Yes' or 'Y' to add item")
            choice = input("Do you want to Add item : ")
            if choice.lower() in ['y', 'yes']:
                name = input("Enter name : ")
                item_type = input("Specify type (addon / base) : ").lower()
                
                try:                
                    price = float(input("Enter Price (in decimal) : "))
                except Exception:
                    print("Price must have numerical value")
                    break 

                if type(name).__name__ != 'str' or type(item_type).__name__ != 'str':
                    print(type(name))
                    print("Type of Variable isn't as recommended")
                    break
                
                if item_type not in ['addon', 'base']:
                    print("Values must be addon or base")
                    break

                self.to_file(name, item_type, price)

            else:
                break

    def to_file(self, name, item_type, price):
        id = self.get_latest_id()
        self.data.append({'id':id, 'name':name, 'type':item_type, 'price':price})
        json.dump({'items' : self.data}, open('items.json', 'w'))