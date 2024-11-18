from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for book storage
books = []

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a single book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Endpoint to update a book by id
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book['book_name'] = data.get('book_name', book['book_name'])
        book['author'] = data.get('author', book['author'])
        book['publisher'] = data.get('publisher', book['publisher'])
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Endpoint to delete a book by id
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
