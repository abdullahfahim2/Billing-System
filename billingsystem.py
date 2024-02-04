#Simple Billing System Without GUI in Python
class Item:
    def __init__(self, id, itemName, price):
        self.id = id
        self.itemName = itemName
        self.price = price

# Create bill display function
def display(item_list, customer_name, customer_address):
    total = 0
    print("\n\n\n")
    print("\t           Swapno Super Shop           ")
    print("\t    Rahimanagar , Kachua , Chandpur    ")
    print("\t              Bill Voucher             ")
    print("\t   ----------------------------------    ")
    print(f"Name : {customer_name} \t Address : {customer_address}\n")
    for obj in item_list:
        print(f"Id : {obj.id} \t ItemName : {obj.itemName}\tPrice : {obj.price}")
        #print("-----------------------------------------------------")
        total += obj.price
    print("-----------------------------------------------------")
    print(f"\t\tTotal : {total}")
    print("\n")
    print("\t  Thanks for visiting!             ")
    print("Electronically Generated,No Need To Signature!")
    print("\n\n")

# Store Item In List
item_list = []

print("\n\n")
print("Hello Everyone.Welcome to Our Grocery Management System!......")
customer_name = input("Enter your name       ")
customer_address = input("Enter your address    ")
total_items = int(input("Enter total items    "))
print("\n")

# Take input item details
for i in range(0, total_items):
    item_id = (i + 1)
    item_name = input("Enter item name     ")
    item_price = int(input("Enter price    "))
    item_list.append(Item(item_id, item_name, item_price))

# Call display function
display(item_list, customer_name, customer_address)