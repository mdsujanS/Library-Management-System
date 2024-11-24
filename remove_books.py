
def remove_books(all_books):
    if all_books == []:
        print("No Books Available to Remove")
        return all_books 
    isbn_number = int(input("Enter the ISBN Number: "))
    
    for book in all_books:
        if isbn_number == book['isbn']:
            all_books.remove(book)
            print(f'Book Remove Successfully')
            return all_books 
    
    print("No Book Available with this ISBN Number")
    return all_books 