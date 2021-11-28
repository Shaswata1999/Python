students = ["Shaswata", "Sayan", "Samrat", "Soumik"]
name = input("Enter thew name to search: ")
if name in students:
    print(name+" is present in the list")
else:
    print(name+" is not present in the list")