# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

from os import system, name


def clear():
    """
    This function is used to clear the terminal in order for customer to use easier
    :return:
    """
    # for windows
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')
