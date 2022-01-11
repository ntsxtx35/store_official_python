# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SG-G01-11 (s3878340, s3819342, s3715305, s3872104)
# Created date: 10/12/2021
# Last modified date: 11/01/2022

# Create function to read data and create dictionary
def read_file_create_dict(infile_name):
    """
    This function is used to read data from file and create a dictionary
    :param infile_name: Input file name
    :return: Return the dictionary of the data to use
    """
    dictionary = {}
    values = []
    with open(infile_name, 'r') as infile:

        # Read data by line
        lines = infile.readlines()

        # Loop through each line
        for line in lines:
            current_line = line.split(',')

            # Loop through each word after splitting the line
            for pos in range(1, len(current_line)):

                # Remove the \n character at the end and blank space
                current_line[pos] = current_line[pos].replace('\n', '')
                current_line[pos] = current_line[pos].strip()
                values.append(current_line[pos])

            # Change the data type from string to int
            values[1] = int(values[1])
            values[3] = int(values[3])

            dictionary[current_line[0]] = values
            values = []

    return dictionary


# Create function to update data after run
def write_to_file(dictionary, outfile_name):
    """
    This function is used to update data after each run
    :param dictionary: The dictionary of data to write to output file
    :param outfile_name: Output file name
    :return:
    """
    lst = []
    with open(outfile_name, 'w') as outfile:

        # Loop through the dictionary to change the data type of the value at index 1 and 3
        for key, values in dictionary.items():
            dictionary[key][1] = str(dictionary[key][1])
            dictionary[key][3] = str(dictionary[key][3])

        # Loop through the dictionary and append the infos into a list and write to file
        for key, values in dictionary.items():
            lst.append(key)
            for value in values:
                lst.append(value)
            line = ','.join(lst)
            outfile.write(line + '\n')
            lst = []
            line = ''

