print("----------------------------")
print("Welcome to TC Contact Book")
print("----------------------------")
print("What do you want to do? ")
print("1. Add Contact")
print("2. List Contact")
print("3. Delete Contact")
print("4. Update Contact")
print("5. Search Contact")
print("6. Exit")
print("----------------------------")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Add Contact")
elif choice == 2:
    print("List Contact")
elif choice == 3:
    print("Delete Contact")
elif choice == 4:
    print("Update Contact")
elif choice == 5:
    print("Search Contact")
elif choice == 6:
    print("Exit")
else:
    print("Invalid choice")