num = int(input("Enter a number: "))
prime = False
for i in range (2,num):
    if(num%i == 0):
        prime = True
        break

if prime:
    print("Number is not prime")
else:
    print("Number is prime")