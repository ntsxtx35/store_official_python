# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

# Create function to list all information of a specific customer
def list_cus(customers, customer_id):
    """
    :param customers: dictionary of customer
    :param customer_id: the id of the customer (integer)
    :return: none
    """
    # print customer information
    print("Customer id: {}".format(customer_id))
    print("Customer name: {}".format(customers[str(customer_id)][0]))
    print("Total accumulated budget: {}".format(customers[str(customer_id)][1]))
    print("Promotion: {}".format(customers[str(customer_id)][2]))
    print("Total bills: {}".format(customers[str(customer_id)][3]))
    print("Address: {}".format(customers[str(customer_id)][4]))
