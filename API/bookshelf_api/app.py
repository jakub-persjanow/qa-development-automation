from flask import Flask, request
from flask import jsonify
from data import books
from models import Book

app = Flask(__name__)

# Architektura

# Landing page, zeby nie bylo errora na wstepie
@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <title>Welcome to bookshelf API</title>
        </head>
        <body>
            <h1>Welcome to bookshelf API</h1>
            <h2>Here's the list of endpoints:</h2>
            <p>GET — all books: <i>Visit /books</i></p>
            <p>GET — books by ID: <i>Visit /books/[book_id]</i></p>
            <p>POST — new book: <i>Example: curl -X POST -H "Content-Type: application/json" \
     -d '{"title": "Solaris", "author": "Stanislaw Lem", "year": 1961}' \</i></p>
            <p>PUT - edit book by ID: <i>Example: curl -X PUT -H "Content-Type: application/json" \
     -d '{"title": "New title", "year": 2020}' \
     http://127.0.0.1:5000/books/2</i></p>
            <p>DELETE — book by ID: <i>Example: curl -X DELETE http://127.0.0.1:5000/books/4</i></p>
        </body>
    </html>
    """

# GET — wszystkie książki
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([b.to_dict() for b in books])

# GET — konkretna książka po ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.to_dict())

# POST — dodaj nową książkę
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_id = max(b.id for b in books) + 1 if books else 1
    new_book = Book(new_id, data['title'], data['author'], data['year'])
    books.append(new_book)
    return jsonify(new_book.to_dict()), 201


# PUT — edytuj książkę
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)
    return jsonify(book.to_dict())

# DELETE — usuń książkę
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b.id != book_id]
    return jsonify({"message": "Book deleted"}), 200

# Use case'y:

# Pobierz wszystkie książki
# Dodaj nową książkę
# Zaktualizuj książkę
# Usuń książkę