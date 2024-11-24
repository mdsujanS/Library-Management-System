import add_books
import view_all_books
import update_books 
import remove_books 

all_books = []

while True:
    print("---- Welcome to Library Management System----")
    print("0. Exit. ")
    print("1. Added Books. ")
    print("2. View All Books. ")
    print("3. Update Books. ")
    print("4. remove Books. ")
    
    option = input("Select an option: ")
    
    if option == "0":
        print("----- Thanks for using Library Management System -----")
        break
    elif option == "1":
        all_books = add_books.add_books(all_books)
    elif option == "2":
        view_all_books.view_all_books(all_books)
    elif option == "3":
        all_books = update_books.update_books(all_books)
    elif option == "4":
        all_books = remove_books.remove_books(all_books)
    else:
        print("Choose a valid option")
        
        
