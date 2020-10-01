import re

file_path = "./data/sentences.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        validity_string = "-: "

        # re.match see if 2nd argument starts by 1st argument
        # this 1st argument matches string that starts by "There is" or "There are"(There (is|are)),
        # continues some characters or not(.*) and ends by "."(\.)
        match = re.match(r"There (is|are).*\.", line)

        if match is None:
            validity_string = "F: "
        else:
            validity_string = "T: "
        
        print(validity_string + line)

