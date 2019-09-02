import re

if __name__ == "__main__":
    filename = 'C:\\Users\\Camer\\Documents\\Python_Tests\\pi_birthday\\pi_million_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    birthday = input("Enter your birthday in the form mmddyy: ")
    if birthday in pi_string:
        reg_birthday = 'r"' + birthday + '"'
        print("Your birthday appears in the first million digits of pi!")
        print("Below is the result with 3 numbers on either end of your birthday!")
        for x in re.finditer(birthday, pi_string):
            print(pi_string[x.start()-3:x.end()+3])
            print(f"Found at position {x.start()} and {x.end()}.")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
