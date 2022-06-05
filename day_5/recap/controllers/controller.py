from flask import redirect, request, render_template

from app import app
from models.books import * 
from models.book import Book, get_books, add_book


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books_index():
    books = get_books()
    return render_template("books/index.html", books=books)

@app.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_book(new_book)
    redirect("/books")

@app.route("/books/new")
def add_new_book():
    return render_template("books/new.html")

