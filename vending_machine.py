# Simple Vending Machine Program
from datetime import datetime
import random

items = {
    1: ["Coke", 40, 10],
    2: ["Pepsi", 35, 8],
    3: ["Water", 20, 5],
    4: ["Chips", 30, 10],
    5: ["Gems", 15, 8],
    6: ["Banana Chips", 30, 5],
    7: ["Fanta", 40, 6],
    8: ["Dairy Milk",20, 10],
    9: ["Amul Lassi",20, 6],
    10: ["Amul Cheese", 50, 5]
}

print(" =============================================== ")
print("                VENDING MACHINE                  ")
print(" =============================================== ")
print("                 AVAILABE ITEMS                                    ")
print("------------------------------------------------")
print(" S.No.       ITEMS         PRICE        QUANTITY")
print(" 01.          Coke         Rs. 40           8   ")
print(" 02.         Pepsi         Rs. 35           8   ")
print(" 03.         Water         Rs. 20           10   ")
print(" 04.         Chips         Rs. 20           10   ")
print(" 05.          Gems         Rs. 15           5   ")
print(" 06.      Banana Chips     Rs. 35           6   ")
print(" 07.         Fanta         Rs. 20           8   ")
print(" 08.      Dairy Milk       Rs. 20           10   ")
print(" 09.      Amul Lassi       Rs. 20           8   ")
print(" 10.      Amul Cheese      Rs. 20           5   ")
print("------------------------------------------------")

while True:
    for key, value in items.items():
        print(f"{key}.  {value[0]}  Rs.{value[1]}  {value[2]}")

    choice = int(input("\nEnter item number: "))
    quantity=int(input("\nEnter the number of items you want: "))

    if choice in items:
        item_name, price, quant = items[choice]

        if quantity <= quant:
            total_price = price * quantity
            print(f"You selected {quantity} {item_name}")
            print(f"Total amount: Rs.{total_price}")
            money = int(input("Insert money (Rs): "))

            if money == total_price:
                print("Dispensing item...")

            elif money > total_price :
                change = money - total_price
                items[choice][2] -= quantity
                print("Dispensing item...")
                print(f"Collect your change: Rs.{change}")

            else:
                print("Insufficient money. Transaction cancelled.")

            id=random.randint(100000,999999)
            now=datetime.now()
            print()
            print("***************************************")
            print("               RECIEPT             ")
            print("---------------------------------------")
            print(f"Unique ID: {id}")
            print(f"Date & Time:" , now)
            print(f"Item id purchased: {choice}")
            print(f"Number of items purchased: {quantity}")
            print(f"Amount required: {price*quantity}")
            print(f"Amount paid: {money}")
            if money>(price*quantity):
                print(f"Change: {money-(price*quantity)}")
            elif money<(price*quantity):
                print(f"Insufficient amount paid")
            else:
                print(f"Change: Rs.0")
            print("----------------------------------------")
            print("THANK YOU FOR USING THIS VENDING MACHINE")
            print("****************************************")
            print()
            print()
            print()

        elif quantity>quant:
            print(f"Oops! Only {quant} {item_name} available, and you ordered for {quantity}, so the order can't be placed.")

        else:
            print("Invalid Input.")

    else:
        print("Invalid selection.")


