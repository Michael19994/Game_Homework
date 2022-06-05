from models.book import Book

book1 = Book("The Lord of the Rings", "J R R Tolkien", "fantasy")
book2 = Book("The Hobbit", "J R R Tolkien", "fantasy")
book3 = Book("Clean Code", "Robert Martin", "software development")
books = [book1, book2, book3]

def get_books():
    return books

def add_book(book):
    books.append(book)

def delete_book(index):
    pass
