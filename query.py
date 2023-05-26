"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

#################### Functions and operations #############################

username = "Simon Smith" # remove when finished 

#get username
def get_user():
    "Get the username(str) and return it to a global variable" 
    
    global username
    username = input("Please input a username: ")
    return username 


# Greet the user
def greet():
    "Greet the user and print the operation menu"

    print(f"Hello,{username}\nWhat would you like to do?")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")

#input operation 
def get_operation():
    "creates a GLOBAL variable of type int, range(1-3) named 'operation' with error handling for anything else"
    
    global operation 
    operation = input("Type the number of the operation: ") #Takes the user input as string
    try:
        operation = int(operation) 
    except ValueError:
        raise ValueError("Incorrect input value type. Please enter an integer.")
    
    if operation >= 1 and operation <= 3:
        return operation
    else:
        raise ValueError("Incorrect input value. Please enter an integer between 1 and 3.")


#greet(get_user()) ## testing purposes
#input_operation() ## testing purposes

#operation 1 - List items in both warehouses
def operation_1():
    "Lists items in each of the warehouses"
    
    print("*******************")
    print("*You have picked option 1.)*")
    print("*******************")
    print("Items in warehouse 1 are as follows:")
    for item in warehouse1:
        print(f" -{item}")
    print("*******************")

    print("*******************")
    print("Items in warehouse 2 are as follows:")
    for item in warehouse2:
        print(f" -{item}")
    print("*******************")
    print(f"Thankyou for your visit today, {username}!")

# operation 2 - search 
def operation_2():
    "Returns 3 global variables typ int, containing individual as well as combined warehouse stock for matching search term."

    global stock1, stock2, total_stock
    stock1 = 0
    stock2 = 0
    search_term = input("What is the name of the item you're searching for: ")
    
    for item in warehouse2:
        if search_term in item:
            stock1 += 1

    for item in warehouse1:
        if search_term in item:
            stock1 += 1
    
    total_stock = stock1 + stock2

    return  stock1, stock2, total_stock


#operation_2()  ##testing purposes
#print(stock1, stock2, total_stock)  ##testing purposes

 # operation 3 Quit
def operation_3():
    "Thanks the user and closes the program"

    print(f"Thankyou for your visit, {username} have a nice day :) !")
    quit()

#operation_3()  ## for testing purposes

#################  END OF FUNCTIONS AND OPERATIONS ########################

#logic
get_user()
greet()
get_operation()

## could use a while loop here to make the program return to the get operation menu 

if operation == 1:
    operation_1()

elif operation == 2:
    operation_2()

elif operation == 3:
    operation_3()
