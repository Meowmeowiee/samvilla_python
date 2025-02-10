file = open("Hello.txt", "r")
# a-append r-read w-write

numbers = file.readlines()
for number in numbers:
    print(number.strip())
file.close()