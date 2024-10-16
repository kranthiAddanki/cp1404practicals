"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subject_information(data)
#    print(data)


def load_data():
    subjects_information = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        #      print(line)  # See what a line looks like
        #        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    #        print(parts)
        subjects_information.append(parts)
#    print(subjects_information)
    #        print("----------")

    input_file.close()
    return subjects_information

def print_subject_information(subjects_information):
    for subject in subjects_information:
        subject_name = subject[0]
        teacher_name = subject[1]
        no_of_students = subject[2]
        print(f"{subject_name} is taught by {teacher_name} and has {no_of_students} students.")




main()
