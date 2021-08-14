import json
from item import Item

class Order:
    def __init__(self):
        # load current data available in orders.json
        self.data = json.load(open('orders.json','r'))['orders']
        # blank list to add dictionary of item and quantity to it
        self.order_items = []

    def get_latest_id(self):
        # retrieval of latest id
        return (len(self.data) + 1)

    def make(self):
        while 1:
            choice = input("Do you want to add item(Y/N) ? : ")
            if choice.lower() in ['yes','y']:
                
                # will show items in a format
                Item().show_items()

                # check that number is entered or not for id
                try:
                    item = int(input("Enter item ID to add in order : "))
                except:
                    print("ID should be numeric")
                    continue

                # checking whether id exists or not
                if not self.validate_id(item):
                    print("No such item ID exists")
                    continue

                # checking quantity is in format of number or not 
                try:
                    quantity = int(input("Enter quantity (Max : 3) : "))
                except:
                    print("Quantity should be numeric")
                    continue

                # checking for max and min quantity that it must be in range of 1 - 3
                if quantity < 1 or quantity > 3:
                    print("Quantity should be in range of 1-3 you entered {} \nItem not added".format(quantity))
                    continue

                # adding item and quantity to dictionary
                self.add_order(item, quantity)
                
            else:
                self.summery()
                break

    def add_order(self, item, quantity):
        # function to append id and quantity of item added for order
        self.order_items.append({"item":item, 'quantity':quantity})

    def summery(self):
        # show summery of order in a particular format
        self.show_summery()
        choice = input("Do you want to add more items(Y/N) : ")
        if choice.lower() in ['y','yes']:
            # if user want to add more item in order then redirect to make again
            self.make()
        else:
            # will update items.json file with new available quantity
            self.update_items()
            # will update orders.json file with new order items and quantity
            self.update_orders()
            print("Order Placed...") 

    def update_items(self):
        items = Item().get_all_item()
        for item in self.order_items:
            for data in items:
                if data['id'] == item['item']:
                    # data['id'] is id which is from json file and item['id'] is selected in orders 
                    data['available_quantity'] = data['available_quantity'] - item['quantity']
                    break

        # updating items.json with updated data
        json.dump({'items' : items}, open('items.json', 'w'))

    def update_orders(self):
        # getting new ID
        id = self.get_latest_id()
        # appending new order details in existing data
        self.data.append({'id':id, 'items':self.order_items})
        # writting file with new data 
        json.dump({'orders':self.data}, open('orders.json','w'))

    def show_summery(self):
        # showing order summery in specific format
        for i in range(52):
            print("-",end="")
        print("")

        print("| Name                     | Price     | Quantity  |")

        for i in range(52):
            print("-",end="")
        print("")
            
        total = 0
        for item in self.order_items:
            info = Item().get_single_item(item['item'])
            name = info['name']
            total = total + (info['price'] * item['quantity'])
            price = str(info['price'])
            quantity = str(item['quantity'])

            name = '| ' + self.space_generator(name, 25)
            price = '| ' + self.space_generator(price, 10)
            quantity = '| ' + self.space_generator(quantity, 10) + "|"

            print(name + price + quantity)

            for i in range(52):
                print("-",end="")
            print("")          
        
        total = str(total)
        space = ""
        for i in range(len(total), 21):
            space = space + " "
        
        print("| Total                    | {} |".format(total+space))
        
        for i in range(52):
            print("-",end="")
        print("")   

    def validate_id(self, id):
        # checking id for order that exist in data storage or not
        items = Item().get_all_item()
        found = False
        for item in items:
            if item['id'] == id:
                found = True
                break

        return found

    def space_generator(self, var, length):
        # will convert string to length passed by adding spaces 
        var = str(var)
        space = ""
        for i in range(len(var), length):
            space = space + " "
        return var + space