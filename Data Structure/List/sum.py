lst = []
num = int(input("Eter the total number of digits: "))
sum = 0
print("Enter digits: ")
for i in range (0,num):
    digit = int(input())
    lst.append(digit)
print(lst)
for j in range (0, len(lst)):
    sum = sum+lst[j]
print("Sum of the list elements is : ", sum)