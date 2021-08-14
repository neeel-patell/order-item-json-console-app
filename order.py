import json
from item import Item

class Order:
    def __init__(self):
        self.data = json.load(open('orders.json','r'))['orders']
        self.order_items = []

    def get_latest_id(self):
        return (len(self.data) + 1)

    def make(self):
        while 1:
            choice = input("Do you want to add item(Y/N) ? : ")
            if choice.lower() in ['yes','y']:
                self.show_items()
                try:
                    item = int(input("Enter item ID to add in order : "))
                except:
                    print("ID should be numeric")
                    continue

                if not self.validate_id(item):
                    print("No such item ID exists")
                    continue

                try:
                    quantity = int(input("Enter quantity (Max : 3) : "))
                except:
                    print("Quantity should be numeric")
                    continue

                if quantity < 1 or quantity > 3:
                    print("Quantity should be in range of 1-3 you entered {} \nItem not added".format(quantity))
                    continue

                self.add_order(item, quantity)
                
            else:
                self.summery()
                break

    def add_order(self, item, quantity):
        self.order_items.append({"item":item, 'quantity':quantity})

    def summery(self):
        self.show_summery()
        choice = input("Do you want to add more items(Y/N) : ")
        if choice.lower() in ['y','yes']:
            self.make()
        else:
            print("Order Placed...") 

    def show_summery(self):
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
            price = str(info['price'])
            quantity = str(item['quantity'])

            total = total + (int(price) * int(quantity))

            space = ""
            for i in range(len(name),25):
                space = space + " "
            name = '| ' + name + space

            space = ""
            for i in range(len(price),10):
                space = space + " "
            price = '| ' + price + space

            space = ""
            for i in range(len(quantity),10):
                space = space + " "
            quantity = '| ' + quantity + space + "|"

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
        items = Item().get_all_item()
        found = False
        for item in items:
            if item['id'] == id:
                found = True
                break

        return found

    def show_items(self):
        for i in range(0,59):
            print("-",end="")
        print("")
        print("| ID   | Name                     | Price     | Available |")
        for i in range(0,59):
            print("-",end="")
        print("")
        items = Item().get_all_item()
        for item in items:
            id = str(item['id'])
            name = item['name']
            price = str(item['price'])
            quantity = str(item['available_quantity'])

            space = ""
            for i in range(len(id), 5):
                space = space + " "
            id = "| " + id + space

            space = ""
            for i in range(len(name), 25):
                space = space + " "
            name = "| " + name + space

            space = ""
            for i in range(len(price), 10):
                space = space + " "
            price = "| " + price + space

            space = ""
            for i in range(len(quantity), 10):
                space = space + " "
            quantity = "| " + quantity + space + "|"

            print(id + name + price + quantity)
            
        for i in range(0,59):
            print("-",end="")
        print("")