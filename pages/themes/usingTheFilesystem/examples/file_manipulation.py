import os

# filename = "test_file.txt"

# fh = open(filename, "r")
# print(dir(fh))

# for line in fh.readlines():
#  	print(line, end="")


# while line=fh.readline():
# 	print(line)


# print(os.getcwd())

# os.chdir("/media/nemsys/data/projects/courses/ProgressBG/ProgressBG-Python/ProgressBG-Python-Slides/pages/themes/usingTheFilesystem")
# print(os.getcwd())


# filename = "test_file.txt"

# fh = open('test_file.txt', 'r')
# # for l in fh:
# # 	print(l, end='')

# for l in fh.readlines():
# 	print(l, end='')


# os.remove('test_file.txt')

# with open('test_file.txt', 'r') as fh:
# 	for l in fh:
# 		print(l, end='')


data = ['Hello, world!', 'This is a new line.']
lines = [f"{line}\n" for line in data]

with open("test_file.txt", mode="w", encoding="utf-8") as fh:
    fh.writelines(lines)