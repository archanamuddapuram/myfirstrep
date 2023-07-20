with open("hello.txt",'r') as reader:
    con=reader.readlines()

with open("hello.txt",'w') as file:
    for line in reversed(con):
        file.write(line)

        arr=[1,2,3,4]
        arr.