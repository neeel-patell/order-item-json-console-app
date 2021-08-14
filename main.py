from order import Order
from item import Item

def main():
    while 1:
        print("1. Add Order")
        print("2. Add Item")
        print("3. Quit")
        choice = int(input("Enter Your Choice : "))
        if choice not in [1,2]:
            break
        else:
            if choice == 1:
                Order().make()
            else:
                Item().add()

main()