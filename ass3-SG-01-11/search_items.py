# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

import placing_order


# Function to search item by name
def search_name(item_dict):
    """
    THis function is used for customer to search for an item by name
    :param item_dict:
    """
    name = input("Input the name of the item: ").lower()
    name_lst = []

    # Loop through the list and append the item name if it meet the condition
    for k, v in item_dict.items():
        if name == item_dict[k][0].lower() or item_dict[k][0].lower().find(name) != -1:
            name_lst.append([item_dict[k][0], k])

    # Check if the store has the items the customer looking for or not
    if len(name_lst) == 0:
        print('Sorry we dont have what you are looking for in the store')
    else:
        for item in name_lst:
            print(f'ID: {item[1]}      Name: {item[0]}')


# Function to search item by ID
def search_id(item_dict):
    """
    This function is used to search items by ID
    :param item_dict: Dictionary of items in the store
    """
    item_id = input("Enter the item's ID you want to search for: ")

    # Check user input
    item_id = placing_order.check_user_item_input(item_id, item_dict)

    print(f'ID: {item_id}  Name: {item_dict[item_id][0]}')
