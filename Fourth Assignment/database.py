products = []
def read_file():
    f = open("database.txt", "r")
    for line in f:
        result = line.split(", ")
        my_dictionary = {"id": result[0], "name": result[1], "price": result[2], "amount": result[3]}
        products.append(my_dictionary)
        print(result)

def show_menu():
    print("1- Add")
    print("2- remove")
    print("3- search")
    print("4- edit")
    print("5- show list")
    print("6- Buy")
    print("7- exit")
    
def add():
    id = input("id")
    name = input("name")
    price = input("price")
    amount = input("amount")
    new_dic = {"id":id, "name": name, "price":price, "amount":amount}
    products.append(new_dic)
    print(products)
def remove():
    ...
def search():
    key = input("Enter your key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break
    else: #this is for and else loop.
        print("Not found")

def edit():
    ...
def showlist():
    print("id\tname\tprice\tamount")
    for product in products:
        print(product["id"],"\t", product["name"],"\t",  product["price"],"\t",  product["amount"])
def buy():
    ...

def save_to_database():
    ...

read_file()
while True:
    show_menu()
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        add() 
    elif user_choice == 2:
        remove()
    elif user_choice == 3:
        search()
    elif user_choice == 4:
        edit()
    elif user_choice == 5:
        showlist()
    elif user_choice == 6:
        buy()
    elif user_choice == 7:
        save_to_database()
        exit(0)

    
    # elif user_choice == 7:
    #     ... #this ... prevents from error and wait for adding commands. or you can type "pass"
    else:
        print("Please select a number: ")

#print(products)