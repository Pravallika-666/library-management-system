
books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book Added!")

    elif choice == "2":
        print("\nBooks List:")
        for b in books:
            print(b)

    elif choice == "3":
        name = input("Enter book name to search: ")

        if name in books:
            print("Book Found!")
        else:
            print("Book Not Found!")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
