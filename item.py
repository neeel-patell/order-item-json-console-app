import json

class Item:
    
    def __init__(self):
        # Get existing json data from file and also assigned 'items' json array to variable for append data, access data and convert to file operations
        self.data = json.load(open('items.json', 'r'))['items']

    def get_all_item(self):
        # will return all items
        return self.data

    def get_latest_id(self):
        # Adding Length with 1 to get latest id as existing id + 1
        return (len(self.data)+1)

    def add(self):
        # Infinite loop will break when user enters apart from 'Yes' or 'Y'
        while(1):

            print("Enter 'Yes' or 'Y' to add item")
            choice = input("Do you want to Add item : ")
            if choice.lower() in ['y', 'yes']:

                # Entering details about Item
                name = input("Enter name : ")
                item_type = input("Specify type (addon / base) : ").lower()
                
                # Checking whether price is numeric or not if it's such string value which can not be converted to numeric then skipping code and go again to start of loop
                try:                
                    price = float(input("Enter Price (in decimal) : "))
                except Exception:
                    print("Price must have numerical value")
                    continue 

                try:
                    available_quantity = int(input("Enter available quantity : "))
                except Exception:
                    print("Available Quantity must have numerical value")
                    continue
                
                # If item_type is neither 'addon' nor 'base' then skipping below code 
                if item_type not in ['addon', 'base']:
                    print("Values must be addon or base")
                    continue

                self.to_file(name, item_type, price, available_quantity)

            else:
                break

    def to_file(self, name, item_type, price, available_quantity):
        # generating new ID to append in json file
        id = self.get_latest_id()
        # appended varified and accurate user data
        self.data.append({'id':id, 'name':name, 'type':item_type, 'price':price, 'available_quantity':available_quantity})
        # Writing whole file with new json data
        json.dump({'items' : self.data}, open('items.json', 'w'))
        self.show_items()

    def space_generator(self, var, length):
        var = str(var)
        space = ""
        for i in range(len(var), length):
            space = space + " "
        return (var + space)

    def get_single_item(self, id):
        # function will return information about single item
        name = ""
        price = ""
        for item in self.data:
            if id == item['id']:
                name = item['name']
                price = item['price']
                break
        return {'name':name, 'price':price}

    def show_items(self):
        # show list of items in a specific format
        for i in range(0,59):
            print("-",end="")
        print("")
        print("| ID  | Name                     | Price     | Available |")
        for i in range(0,59):
            print("-",end="")
        print("")
        for item in self.data:
            id = str(item['id'])
            name = item['name']
            price = str(item['price'])
            quantity = str(item['available_quantity'])

            id = "|" + self.space_generator(id, 5)
            name = "| " + self.space_generator(name, 25)
            price = "| " + self.space_generator(price, 10)
            quantity = "| " + self.space_generator(quantity, 10) + "|"

            print(id + name + price + quantity)
            
        for i in range(0,59):
            print("-",end="")
        print("")