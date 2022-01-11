# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

# Create function to list all items in the store
def list_item(item_dict):
    """
    This function is used to list all of items in the store
    :param item_dict: Dictionary of items
    """
    print('List of all items')
    for item_id, item_list in item_dict.items():
        print(item_id + '\t' + item_list[0])


# Create function to list all information of a specific item
def list_item_info(item_dict, item_id):
    """
    This function is used to list all information of a specìic item
    :param item_dict: Dictionary of items in the store
    :param item_id: ID of a specific item
    """
    print(f'Name: {item_dict[item_id][0]} \nQuantity: {item_dict[item_id][1]} \nGenre: {item_dict[item_id][2]} \n'
          f'Price: {item_dict[item_id][3]} VND')
    print("* " * 10)
