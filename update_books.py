
def update_books(all_books):
    if all_books == []:
        print("No Books Available to Update!")
        return all_books
    
    isbn_number = int(input("Enter the ISBN Number to Update: "))
    
    for book in all_books:
        if book['isbn'] == isbn_number:
            print(f"Book Title {book['title']}")
            print("Enter New Details to Update: ")
            book['title'] = input("Enter New Title: ")
            book['author'] = input("Author Name: ")
            book['year'] = int(input("Update New Year: "))
            book['price'] =int(input("Enter the Update Proce: "))
            book['quantity'] = int(input("Entr the update quantity: "))
            print("Book Update Successfully!")
            
            return all_books 
        print("No Books Found to Update")
        return all_books