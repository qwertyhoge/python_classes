file_path = "./data/hoge_multi_line.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        print("{0:d}: {1}".format(i + 1, lines[i]))