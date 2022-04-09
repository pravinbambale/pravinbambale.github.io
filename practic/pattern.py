print("-------------------------\nSimple Number Triangle Pattern")  
rows = 6
for num in range(rows):
    for i in range(num):
        print( num, end=" ")
    print(" ")
    
print("-------------------------\nInverted Pyramid of Numbers")  

rows = 6
for num in range(rows):
    cols = rows-num
    for i in range(cols):
        print(num+1, end=" ")
    print(" ")


##same with another logic
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=" ")
    print("\r")

print("-------------------------\nHalf Pyramid Pattern of Numbers")  

rows = 6
for num in range(rows):
    for i in range(num):
        print(i+1, end=" ")
    print(" ")


print("-------------------------\nInverted Pyramid of Descending Numbers")  

rows = 6
for num in range(rows):
    cols = rows-num
    for i in range(cols):
        print(cols, end=" ")
    print(" ")

print("-------------------------\n Inverted Pyramid of the Same Digit")  

rows = 6
for num in range(rows):
    cols = rows-num
    for i in range(cols):
        print(5, end=" ")
    print(" ")

print("-------------------------\n Reverse Pyramid of Numbers")  

rows = 6
for num in range(rows+1):
    for i in range(num):
        print(num-i, end=" ")
    print(" ")


##Inverted Half Pyramid Number Pattern

rows = 6
for num in range(rows):
    cols = rows-num
    for i in range(cols):
        print(5, end=" ")
    print(" ")

##Pyramid of Natural Numbers Less Than 10


