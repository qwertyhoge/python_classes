import re

file_path = "./data/id_links.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        usernames = re.findall(r"@[a-zA-Z]+", line)
        
        for un in usernames:
            print(un)

