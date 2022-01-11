# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

import add_info


# Create a function for user to check the rank
def promote(customer_dict):
    """
    This function is used to check the rank
    :param customer_dict: Dictionary of customers
    """
    customer_id = input('Enter your customer ID: ')

    # If the customer id is not in dict, let the customer register
    if customer_id not in customer_dict:
        print('Your ID is not in the database. PLease register')
        add_info.add_customers(customer_dict, customer_id)

    # Check if customer meet the requirement to be promoted to silver or not
    if customer_dict[customer_id][2] == 'Bronze':
        if customer_dict[customer_id][1] >= 5000000:
            if customer_dict[customer_id][3] >= 50:
                print('You are accepted to promote to Silver')
                customer_dict[customer_id][2] = 'Silver'
            else:
                print('You have not reach the number of order to promote to Silver')
        else:
            print('You have not reach the minimum of cost to promote to Silver')

    # Check if customer meet the requirement to be promoted to gold or not
    elif customer_dict[customer_id][2] == 'Silver':
        if customer_dict[customer_id][1] >= 10000000:
            if customer_dict[customer_id][3] >= 100:
                print('You are accepted to promote to Gold')
                customer_dict[customer_id][2] = 'Gold'
            else:
                print('You have not reach the number of order to promote to Gold')
        else:
            print('You have not reach the minimum of cost to promote to Gold')

    else:
        print('You are in the highest rank: Gold')
