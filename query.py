"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

#################### Functions and operations #############################

# username = "Simon Smith" ## testing

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
    try:
        operation = input("Type the number of the operation: ") #Takes the user input as string
        operation = int(operation) 
        if operation not in [1,2,3]:
            raise ValueError
   
    except ValueError:
            print(f"""*************************************************************\n'{operation}' is not a valid operation\n*************************************************************""")
            operation_3()

    return operation
        
    
        


#greet(get_user()) ## testing purposes
#input_operation() ## testing purposes

 # operation 3 Quit - is placed here so it can be used throughout other functions
def operation_3():
    "Thanks the user and closes the program"

    print(f"Thank you for your visit, {username} have a nice day :) !")
    quit()

#operation_3()  ## for testing purposes


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
# operation_1()  ## testing purposes



# operation 2 - search 
def operation_2_search():
    "Returns 3 global variables typ int, containing individual as well as combined warehouse stock for matching search term."

    global stock1, stock2, total_stock, search_term
    stock1 = 0
    stock2 = 0
    search_term = input("What is the name of the item you're searching for: ") # NEED TO MAKE IT MATCH ONLY FULL WORDS OR PRINT ERROR
    
    for item in warehouse1: # loop to obtain amount of stock in warehouse2
        if search_term in item:
            stock1 += 1

    for item in warehouse2: # loop to obtain amount of stock in warehouse1
        if search_term in item:
            stock2 += 1
    
    #loops to obtain location of stock

    total_stock = stock1 + stock2
    location = ""

    if stock1:
        location = "Warehouse 1"
    if stock2:
        location = "Warehouse 2"
    if stock1 and stock2:
        location = "Both warehouses" 
        
    # print statments for options 
    if total_stock == 0:
        print("Item not found")
        operation_3()
    else:
        print(f"Amount available: {stock1, stock2, total_stock}") #REMBEMBER to remove "stock1 and stock2" after testing
        print(f"Location: {location}")
    
def operation_2_selection():
    "Promts user for order selection and processes that order, setting (int)quantity global var to an int value to be used outside of function"
    global quantitiy

    order_selection = input("Would you like to order this item (y/n): ")
    
    if order_selection in ["y", "Y"]:
        quantitiy = int(input("How many would you like to order?: "))


    elif order_selection in ["n", "N"]:
        operation_3()

    else:
        print("you have entered an invalid selection please try again")
        operation_2_selection()  # go back to the begning of selection loop.

def operation_2_ordering():
    "confirmation of order and overstock handling using order_max global var to confirm maximum availibility order"
    global order_max

    if quantitiy <= total_stock:
        print(f"You have chosen to order:\n{quantitiy} {search_term}")
        print(f"order confirmed, have a nice day {username}!")
        quit()
    else:
        print(f"""
    ******************************************************* 
    There are not this many available. The maximum amount that can be ordered are: {total_stock}
    please try again
    *******************************************************
    """)
        
    order_max = input("Would you like to order the maximum available amount (y/n): ")
         
    
    
def operation_2_confirmation():
    "Confirmation of sub maximal and maximum availibility of stock"
    if order_max in ["y", "Y"]:
        print(f"{total_stock} {search_term} successfully ordered")
        print()
        operation_3()

    elif order_max in ["n", "N"]:
        operation_3()

    else:
        print("you have entered an incorrect value pleaste try again ")
        operation_2_confirmation()
        




    

  
   




#operation 2 testing
# operation_2_search() ##testing purposes
# operation_2_selection() ##testing purposes
# operation_2_ordering()  ##testing purposes
# operation_2_confirmation()  ## testing purposes


#print(stock1, stock2, total_stock)  ##testing purposes



#################  END OF FUNCTIONS AND OPERATIONS ########################


############################ LOGIC  #######################################

get_user()
greet()
get_operation()

if operation == 1:
    operation_1()

elif operation == 2:
    operation_2_search()
    operation_2_selection() 
    operation_2_ordering()  
    operation_2_confirmation()  

elif operation == 3:
    operation_3()



##############################################################################