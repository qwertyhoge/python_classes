file_path = "./data/numbers.csv"

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        number_list = [int(num) for num in line.split(",")]
        print(sum(number_list))