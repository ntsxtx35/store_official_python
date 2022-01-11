# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

# Create function to let customer filter item by genre
def choose_genre(item_dict):
    """
    This function is used to filter the items in the store by genre
    :param item_dict: Dictionary of items in the store
    """
    print(f'1. Mystery\n'
          f'2. Romance\n'
          f'3. Fiction\n'
          f'4. Memoir\n'
          f'5. Novel\n'
          f'6. Contemporary\n'
          f'7. Thriller\n'
          f'8. Historical Fiction\n'
          f'9. History\n'
          f'10. Fantasy\n'
          f'11. Detective\n'
          f'12. Horror\n'
          f'13. Novel\n'
          f'14. Adventure')

    # Ask for user input
    choose = int(input("Choose your genre by input a number: "))

    # Dictionary of genre
    genre = {1: 'Mystery',
             2: 'Romance',
             3: 'Fiction',
             4: 'Memoir',
             5: 'Novel',
             6: 'Contemporary',
             7: 'Thriller',
             8: 'Historical Fiction',
             9: 'History',
             10: 'Fantasy',
             11: 'Detective',
             12: 'Horror',
             13: 'Novel',
             14: 'Adventure'}

    # While loop to check if user input is valid or not
    while choose not in genre:
        choose = int(input("Choose your genre in the menu again: "))
    else:
        if choose in genre:
            print(genre[choose])

            # For loop to search for items based on the customer input of genre
            for item_id in item_dict:
                if genre[choose] == item_dict[item_id][2]:
                    print(f'Name: {item_dict[item_id][0]}')

