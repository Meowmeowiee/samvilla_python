file = open("Hello.txt", "r")
# a-append r-read w-write
numbers = file.readlines()

sum = 0
for number in numbers:
   sum = sum + int(number.strip())
print(sum)
file.close()