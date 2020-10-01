file_path = "./data/hoge_single_line.txt"
file = open(file_path, "r")
# it's ok to use file.readline() instead 
print(file.read())
file.close()

# by using `with`, it automatically closes the file out of the block.
with open(file_path, "r") as file:
    print(file.read())