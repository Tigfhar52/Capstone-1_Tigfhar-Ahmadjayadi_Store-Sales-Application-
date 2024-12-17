# CAPSTONE 1.2
# By: Tigfhar Ahmadjayadi

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MASTER DATA

all_data = [
            {'brand': 'Nike',
             'series': 'Air Force 1',
             'price': 1299000,
             'stock': 28},
             
             {'brand': 'Adidas',
             'series': 'Superstar',
             'price': 1499000,
             'stock': 19},

             {'brand': 'Puma',
             'series': 'Suede Classic',
             'price': 899000,
             'stock': 20}
             ]

cart = []

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MAIN MENU
def mainMenu():
    while True:
        mainMenu = input('''
                        Welcome, Sepaters admin!
                        
                        1. Display Shoe Stock Data
                        2. Add Shoe Stock Data
                        3. Update Shoe Stock Data
                        4. Delete Shoe Stock Data
                        5. Calculate Shoe Purchase Transactions
                        6. Exit the program
                        
                        Enter the menu number you want to execute: ''')
        
        if mainMenu == '1':
            menu1()
        elif mainMenu == '2':
            menu2()
        elif mainMenu == '3':
            menu3()
        elif mainMenu == '4':
            menu4()
        elif mainMenu == '5':
            menu5()
        elif mainMenu == '6':
            print('Goodbye, Sepaters admin!')
            break
        else:
            print('The input you entered is incorrect, please enter the number 1/2/3/4/5/6')

# ------------------------------------------------------------------------------------------------------------------------------------------------

# IMPORT PRETTYTABLE/TABULAR
from prettytable import PrettyTable

# SHOE STOCK TABLE
def data_pretty():
    print('Current Sepaters shoe stock:')
    tab = PrettyTable()
    tab.field_names = ['ID', 'Brand', 'Series', 'Price', 'Stock']
    for i in range(len(all_data)): 
        tab.add_row([i+1, all_data[i]['brand'], all_data[i]['series'], all_data[i]['price'], all_data[i]['stock']])
    tab.align = 'l'
    print(tab)

# INPUT MUST BE AN INTEGER
def inputMustBeNumber(prompt):
    userInput = input(prompt)
    while not userInput.isdigit():
        print('The input you entered must be a positive number') 
        userInput = input(prompt)
    return int(userInput)

# INPUT SUBMENU 1
def inputSubmenu1(prompt):
    userInput = input(prompt)
    while not userInput.isdigit() or userInput not in ('1', '2', '3'):
        print('The input you entered is incorrect. Enter the number 1/2/3')
        userInput = input(prompt)
    return userInput

# INPUT SUBMENU 2, 3, AND 4
def inputSubmenu234(prompt):
    userInput = input(prompt)
    while not userInput.isdigit() or userInput not in ('1', '2'):
        print('The input you entered is incorrect. Enter the number 1/2')
        userInput = input(prompt)
    return userInput

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU READ
def menu1():
    while True:
        subMenuRead = inputSubmenu1('''
                                
                                    1. Display all shoe stock
                                    2. Display specific shoe stock by ID
                                    3. Return to main menu
                                    
                                    Enter the menu number you want to execute: ''')
            
        if subMenuRead == '1':
            if not all_data:
                print('Sorry, all shoe stock is currently empty.')
            else:
                data_pretty()
                
        elif subMenuRead == '2':
            while True:
                if all_data:
                    searchData = inputMustBeNumber('Enter the shoe ID you want to search for: ')
                    if searchData > len(all_data):
                        print('The shoe ID you entered does not exist.')
                        break
                    else:
                        tableRead = PrettyTable()
                        tableRead.field_names = ['ID', 'Brand', 'Series', 'Price', 'Stock']
                        tableRead.add_row([searchData, all_data[searchData-1]['brand'], all_data[searchData-1]['series'], all_data[searchData-1]['price'], all_data[searchData-1]['stock']])
                        print(tableRead)
                        break
                else:
                    print('Sorry, all shoe stock is currently empty.')
                    break

        elif subMenuRead == '3':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU CREATE
def menu2():
    while True:
        subMenuCreate = inputSubmenu234('''
                                
                                1. Add new data
                                2. Return to main menu
                                
                                Enter the menu number you want to execute: ''')

        if subMenuCreate == '1':
            # New Brand
            newBrand = input('Enter the new shoe brand to add: ')
            while not newBrand:
                print('Input cannot be empty')
                newBrand = input('Enter the new shoe brand to add: ')
            while len(newBrand) > 20:
                print('The input you entered is too long. Max input is 20 characters: ')
                newBrand = input('Enter the new shoe brand to add: ')

            # New Series
            newSeries = input('Enter the new shoe series to add: ')
            while not newSeries:
                print('Input cannot be empty')
                newSeries = input('Enter the new shoe series to add: ')
            while len(newSeries) > 20:
                print('The input you entered is too long. Max input is 20 characters: ')
                newSeries = input('Enter the new shoe series to add: ')

            for data in all_data:
                if data['brand'] == newBrand and data['series'] == newSeries:
                    print('Data already exists')
                    break
            else:
                # New Price
                newPrice = inputMustBeNumber('Enter the new shoe price to add: ')
                while not newPrice:
                    print('Input cannot be empty')
                    newPrice = inputMustBeNumber('Enter the new shoe price to add: ')

                # New Stock
                newStock = inputMustBeNumber('Enter the new shoe stock to add: ')
                while not newStock:
                    print('Input cannot be empty')
                    newStock = inputMustBeNumber('Enter the new shoe stock to add: ')
                while newStock == 0:
                    print('Input cannot be 0')
                    newStock = inputMustBeNumber('Enter the new shoe stock to add: ')

                # Displaying data to add
                print('The new data has been added:')
                newTable = PrettyTable()
                newTable.field_names = ["Brand", "Series", "Price", "Stock"]
                newTable.add_row([newBrand, newSeries, newPrice, newStock])
                print(newTable)

                # Checker
                while True:
                    saveData = input('Are you sure you want to save the above data? (yes/no): ')
                    checker = saveData.lower()
                    if checker == 'yes':
                        all_data.append({
                            'brand': newBrand,
                            'series': newSeries,
                            'price': newPrice,
                            'stock': newStock
                        })
                        print('New data has been saved')
                        data_pretty()
                        break 
                    elif checker == 'no':
                        print('The new data was not saved')
                        data_pretty()
                        break 
                    else:
                        print('Sorry, the input you entered is incorrect. Enter yes or no.')
                
        elif subMenuCreate == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU UPDATE

def menu3():
    while True:
        subMenuUpdate = inputSubmenu234('''
                            
                            1. Update data 
                            2. Return to main menu
                            
                            Enter the menu number you want to execute: ''')

        if subMenuUpdate == '1':
            data_pretty()
            idUpdate = inputMustBeNumber('Enter the ID of the shoe you want to update: ')
            if idUpdate > len(all_data) or idUpdate == 0:
                print('Sorry, the ID you entered is invalid.')
                continue  
            
            # Displaying details of the shoe to be updated
            print('Details of the shoe to be updated:')
            detail_item = PrettyTable()
            detail_item.field_names = ["ID", "Brand", "Series", "Price", "Stock"]
            detail_item.add_row([idUpdate, all_data[idUpdate-1]['brand'], all_data[idUpdate-1]['series'], all_data[idUpdate-1]['price'], all_data[idUpdate-1]['stock']])
            print(detail_item)

            columnUpdate = input('Enter the column name you want to update (Brand/Series/Price/Stock): ').lower()
            while columnUpdate not in ['brand', 'series', 'price', 'stock']:
                print('The column does not exist.')
                columnUpdate = input('Enter the column name you want to update (Brand/Series/Price/Stock): ').lower()

            # Temporary input for changes from the user
            tempChange = input(f'Enter the updated {columnUpdate}: ')

            # Validating input for price or stock
            if columnUpdate in ['price', 'stock']:
                while not tempChange.isdigit() or int(tempChange) <= 0:
                    print('The input must be a positive integer.')
                    tempChange = input(f'Enter the updated {columnUpdate}: ')
            
            # Creating and displaying a temporary change table
            print('Temporary changes:')
            tempTable = PrettyTable()
            tempTable.field_names = ["ID", "Brand", "Series", "Price", "Stock"]
            tempData = all_data[idUpdate-1].copy()  
            if columnUpdate in ['brand', 'series']:
                tempData[columnUpdate] = tempChange
            else: 
                tempData[columnUpdate] = int(tempChange)
            tempTable.add_row([idUpdate, tempData['brand'], tempData['series'], tempData['price'], tempData['stock']])
            print(tempTable)

            # Checker
            while True:
                saveData = input('Save the data? (yes/no): ').lower()
                if saveData == 'yes':
                    all_data[idUpdate-1].update(tempData)
                    print('The data has been updated.')
                    data_pretty()
                    break 
                elif saveData == 'no':
                    print('Data update was canceled.')
                    data_pretty()
                    break  
                else:
                    print('Sorry, the input you entered is invalid. Enter yes or no.')

        elif subMenuUpdate == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU DELETE

def menu4():
    while True:
        subMenuDelete = inputSubmenu234('''
                            
                            1. Delete data
                            2. Return to main menu
                            
                            Enter the menu number you want to execute: ''')
        
        if subMenuDelete == '1':

            data_pretty()

            idDelete = inputMustBeNumber('Enter the ID of the shoe you want to delete: ')

            if idDelete <= 0 or idDelete > len(all_data):
                print('The ID you entered is invalid.')

            else:
                idIndex = idDelete - 1 

                # Displaying the data to be deleted
                print('Data to be deleted:')
                deleteTable = PrettyTable()
                deleteTable.field_names = ["ID", "Brand", "Series", "Price", "Stock"]
                deleteTable.add_row([idIndex+1, all_data[idIndex]['brand'], all_data[idIndex]['series'], all_data[idIndex]['price'], all_data[idIndex]['stock']])
                print(deleteTable)

                # Checker
                confirmDelete = input('Are you sure you want to delete this data? (yes/no): ').lower()
                if confirmDelete == 'yes':
                    del all_data[idIndex] 
                    print('The data has been deleted.')
                    data_pretty()
                elif confirmDelete == 'no':
                    print('The data was not deleted.')
                    continue
                else:
                    print('Sorry, the input you entered is invalid. Enter yes or no.')

        elif subMenuDelete == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# EXTRA MENU

def menu5():
    while True:
        subMenuExtra = inputSubmenu234('''
                                    
                                    1. Add new purchase
                                    2. Return to main menu
                                    
                                    Enter the menu number you want to execute: ''')

        if subMenuExtra == '1':
            if not all_data:
                print('Sorry, all shoe stock is currently empty.')
            else:
                while True:
                    data_pretty()
                    idOrder = inputMustBeNumber('Enter the ID of the shoe to purchase: ')
                    if idOrder < 1 or idOrder > len(all_data):
                        print("Sorry, the ID you entered is invalid.")
                        continue  
                    
                    qtyOrder = inputMustBeNumber('Enter the quantity you want to purchase: ')
                    if qtyOrder > all_data[idOrder-1]['stock']:
                        print(f"Not enough stock. The stock of {all_data[idOrder-1]['brand']} {all_data[idOrder-1]['series']} is only {all_data[idOrder-1]['stock']}")
                        continue  

                    cart.append({'index': idOrder-1,
                                'brand': all_data[idOrder-1]['brand'], 
                                'series': all_data[idOrder-1]['series'], 
                                'qty': qtyOrder, 
                                'total price': all_data[idOrder-1]['price'] * qtyOrder
                                })            

                    # Displaying the cart
                    print("Cart contents:")
                    cartTable = PrettyTable()
                    cartTable.field_names = ["Brand", "Series", "Qty", "Total Price"]
                    for item in cart:
                        cartTable.add_row([item['brand'], item['series'], item['qty'], item['total price']])
                    cartTable.align = 'l'
                    print(cartTable)

                    # Checker
                    while True:
                        addMore = input('Add another purchase? (yes/no): ').lower()  
                        if addMore == 'no':
                            break
                        elif addMore == 'yes':
                            break
                        else:
                            print("Sorry, the input you entered is invalid. Enter yes or no.")
                            continue

                    if addMore == 'no':
                        break

                # Displaying purchase summary
                print("Shopping List:")
                purchaseTable = PrettyTable(["Index", "Brand", "Series", "Qty", "Total Price"])
                for i in range(len(cart)):
                    item = cart[i]
                    purchaseTable.add_row([i+1, item['brand'], item['series'], item['qty'], item['total price']])
                print(purchaseTable)

                # Calculating transaction total
                totalPrice = sum(item['total price'] for item in cart)

                while True:
                    print(f'Total amount to pay = {totalPrice}')
                    paymentAmount = inputMustBeNumber('Enter payment amount: ')
                    if paymentAmount > totalPrice:
                        change = paymentAmount - totalPrice
                        print(f'Thank you!\nYour change: {change}')
                        for item in cart:
                            all_data[item['index']]['stock'] -= item['qty']
                        cart.clear() 
                        break
                    elif paymentAmount == totalPrice:
                        print(f'Thank you!')
                        for item in cart:
                            all_data[item['index']]['stock'] -= item['qty']
                        cart.clear() 
                        break
                    else:
                        shortage = totalPrice - paymentAmount
                        print(f'You are short by {shortage}')

        elif subMenuExtra == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# RUN  
mainMenu()
