lst = []
num = int(input("Enter total number of students: "))
print("Enter number of the students: ")
for i in range (0, num):
    number = int(input())
    lst.append(number)
lst.sort()
print(lst)
