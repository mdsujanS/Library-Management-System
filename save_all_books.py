def save_all_books(all_books):
    with open("all_books.csv", "w") as book:
        for book in all_books:
            details = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quantity']}\n"
            book.write(details)
            
            

            
            
            