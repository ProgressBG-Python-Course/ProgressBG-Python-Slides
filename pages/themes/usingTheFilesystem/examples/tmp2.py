with open("./test_file.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() to remove trailing newline
