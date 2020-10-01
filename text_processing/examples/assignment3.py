file_path = "./data/new_hoge.txt"

hogefuga_list = ["hoge", "fuga"]
# BBK pattern array
pattern = [0, 0, 1, 1, 0, 1, 1]

with open(file_path, "w") as file:
    for p in pattern:
        file.write(hogefuga_list[p] + "\n")
