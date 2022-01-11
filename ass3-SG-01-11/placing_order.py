# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

import add_info
from list_customer_info import list_cus
from list_item_info import list_item


# This is our main file
# Create a dictionary of order using the order list
def get_order_dict(order_lst):
    """
    This function is used to create a dictionary of customer order
    :param order_lst: A list of customer order
    :return: A dictionary of customer order
    """
    order_dict = {}
    # Loop through each order in the order list
    for sub_order in order_lst:
        if sub_order[0] in order_dict:
            order_dict[sub_order[0]] += sub_order[1]
        else:
            order_dict[sub_order[0]] = sub_order[1]
    return order_dict


# Calculate total cost for an order
def cal_total_cost(order_dict, store_dict):
    """
    This function is used to calculate the total cost of customer order
    :param order_dict: A dictionary of customer order
    :param store_dict: A dictionary of items in the store
    :return: Total cost of customer order (int)
    """
    total_cost = 0
    # Loop through the order dictionary to calculate the total cost
    for k, v in order_dict.items():
        total_cost += (v * int(store_dict[k][3]))
    return int(total_cost)


# Create function to check if user item ID input is valid or not
def check_user_item_input(item_id, store_dict):
    """
    This function is used to check the user item ID input is valid or not
    :param item_id: ID of the items
    :param store_dict: Dictionary of items in the store
    :return: item_id (str)
    """
    # While loop to ask for input until the input is valid
    while item_id not in store_dict:
        item_id = input('Enter valid item ID again: ')
    else:
        return item_id


# Create function to check if user item customer input is valid or not
def check_user_customer_input(customer_id, customer_dict):
    """
    This function is used to check the user item ID input is valid or not
    :param customer_dict: Dictionary of customer
    :param customer_id: Customer ID
    :return: item_id (str)
    """
    # While loop to ask for input until the input is valid
    while customer_id not in customer_dict:
        customer_id = input('Enter other ID again: ')
    else:
        return customer_id


# Create a function to calculate and print out bill for customer
def bill(orders, ls_cus, items, total, cus_id):
    """
    This function is used to calculate and print out bill for customer
    :param ls_cus: list customer (list)
    :param cus_id: customer id (string)
    :param orders: list product customer order (list)
    :param total: total of money to pay the books (integer)
    :param items: dictionary of all items in the store (dictionary)
    :return: none
    """
    # Call function to print the customer info
    print("* " * 10)
    list_cus(ls_cus, cus_id)
    print("* " * 10)

    # Call function to print the product info
    print("product: ")
    for key in orders.keys():
        print("ID book: ", key)
        print("Name: ", items[key][0])
        print("Quantity: ", orders[key])  # print the quantity of the book that the customer orders
        print("Genre: ", items[key][2])
        print("Price: ", int(items[key][3]) * orders[key])  # calculation the total price of order book
        print("* " * 10)

    # Calculate and print shipping fee based on the customer address
    print("ship: {}".format(int(ls_cus[cus_id][-1]) * 15000))

    # Calculate and print the total price customer have to pay include the ship price
    print("total price: {}".format(total + int(ls_cus[cus_id][-1]) * 15000))

    # Check the discount amount based on the customer rank (not include the ship price)
    discount = 0
    if ls_cus[cus_id][2] == "Gold":
        discount = total * 0.2
    if ls_cus[cus_id][2] == "Silver":
        discount = total * 0.1
    print("discount: {}".format(discount))

    # Calculate the final price customer have to pay
    print("pay: {}".format(total - discount + int(ls_cus[cus_id][-1]) * 15000))


# Create a function to auto promote customer's rank when they meet the condition
def auto_promote(customer_id, customer_dict):
    """
    This function is used to auto promote the customer account when they meet the conditions
    :param customer_id: ID of customer
    :param customer_dict: Dictionary of customers
    """
    # Check if the customer meets the condition to be auto promoted to silver
    if customer_dict[customer_id][2] == 'Bronze':
        if customer_dict[customer_id][1] >= 5000000:
            if customer_dict[customer_id][3] >= 50:
                customer_dict[customer_id][2] = 'Silver'

    # Check if the customer meets the condition to be auto promoted to gold
    elif customer_dict[customer_id][2] == 'Silver':
        if customer_dict[customer_id][1] >= 10000000:
            if customer_dict[customer_id][3] >= 100:
                customer_dict[customer_id][2] = 'Gold'


# Create a function to place order, calculate total cost and update the data of items and customers and promote
def placing_order(store_dict, customer_dict):
    """
    This function is used to place order, calculate total cost and update the data of items and customers
    and promote
    :param store_dict: A dictionary of items in the store
    :param customer_dict: A dictionary of customer
    :return: final_order(dict), total_cost(int), customer_id(str)
    """
    orders_list = []

    register = input('Have you registered to our store (Y for Yes and N for No): ')
    customer_id = ''
    # If the customer id is not in dict, let the customer register
    if register == "N":
        register_id = input('Enter your customer ID to register: ')
        while register_id in customer_dict:
            register_id = input('Enter other ID again: ')
        else:
            customer_id = register_id
            add_info.add_customers(customer_dict, customer_id)
    elif register == "Y":
        customer_id = input('Enter your customer ID: ')
        customer_id = check_user_customer_input(customer_id, customer_dict)

    list_item(store_dict)
    # Loop to let the customers to enter the items ID that they want to buy
    while True:
        item_id = input('Enter item ID to order and N to stop: ')
        if item_id == 'N' or item_id == 'n':
            break
        else:
            item_id = check_user_item_input(item_id, store_dict)
            item_quantity = int(input('Enter quantity: '))
            orders_list.append([item_id, item_quantity])

    # Create the dictionary of order
    orders_dict = get_order_dict(orders_list)

    # Update the store dictionary
    for k, v in orders_dict.items():
        if v <= store_dict[k][1]:
            store_dict[k][1] -= v
        else:
            # Loop to check for the remaining item in the store and ask for valid input again
            while True:
                print(f'Sorry we only have {store_dict[k][1]} items {k} ')
                quantity = int(input('Please input the quantity again: '))
                if quantity <= store_dict[k][1]:
                    store_dict[k][1] -= quantity
                    break
            orders_dict[k] = quantity

    # Update number of orders
    customer_dict[customer_id][3] += 1

    # Update number of total_money
    total_cost = cal_total_cost(orders_dict, store_dict)
    customer_dict[customer_id][1] += total_cost

    # Promote the customer rank if it meet the condition
    auto_promote(customer_id, customer_dict)

    return orders_dict, int(total_cost), customer_id
