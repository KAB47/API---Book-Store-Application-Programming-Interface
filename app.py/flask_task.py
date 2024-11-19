from flask import Flask, jsonify, request, Response, send_from_directory
import json

# Initialise the Flask application
app = Flask(__name__)
print(__name__)

# Sample book data to serve as an in-memory database
books = [
    {
        'name': 'Avatar: The Last Airbender (Book 3: Fire)',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 9782371000193
    },
    {
        'name': 'Harry Potter and the Goblet of Fire',
        'price': 17.99,
        'isbn': 1295680405932
    },
    {
        'name': "Tom Clancy's Splinter Cell: Checkmate",
        'price': 14.99,
        'isbn': 9458049859423
    },
    {
        'name': '50 Shades of Grey: (Deluxe Edition)',
        'price': 34.99,
        'isbn': 74839138403054
    }
]


# Route to serve the home page
@app.route("/")
def home():
    """
    Serve the index.html file as the home page.
    """
    return send_from_directory("", "index.html")


# Route to get the list of all books
@app.route('/books')
def get_books():
    """
    Return a JSON response with a list of all books.
    """
    return jsonify({'books': books})


# Utility function to check if a book object is valid
def validBookObject(bookObject):
    """
    Check if the book object has the required keys: name, price, and isbn.

    Parameters:
    - bookObject (dict): A dictionary representing a book.

    Returns:
    - bool: True if the book object is valid, False otherwise.
    """
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False


# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    """
    Add a new book to the list. Expects a JSON payload with 'name', 'price', and 'isbn'.

    Returns:
    - Response: A '201' Created response if the book is successfully added.
                A '400' Bad Request response if the book data is invalid.
    """
    request_data = request.get_json()
    if (validBookObject(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Pass data similar to this: {'name': 'Bookname', 'price': 7.99, 'isbn': 978039400165}"
        }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json')
    return response


# Route to get a book by its ISBN
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    """
    Get details of a specific book by its ISBN.

    Parameters:
    - isbn (int): The ISBN number of the book to retrieve.

    Returns:
    - JSON: A JSON object containing the book's 'name' and 'price' if found, empty JSON if not found.
    """
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)


# Route to replace a book with a new one by ISBN
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    """
    Replace an existing book with new data. Expects a JSON payload with 'name' and 'price'.

    Parameters:
    - isbn (int): The ISBN number of the book to replace.

    Returns:
    - Response: A '204 No Content' response if the replacement is successful.
    """
    request_data = request.get_json()
    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response


# Route to update a book's attributes by ISBN
@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    """
    Update specified attributes of an existing book by its ISBN. Partial updates are allowed.

    Parameters:
    - isbn (int): The ISBN number of the book to update.

    Returns:
    - Response: A '204 No Content' response if the update is successful.
    """
    request_data = request.get_json()
    updated_book = {}
    if ("name" in request_data):
        updated_book["name"] = request_data['name']
    if ("price" in request_data):
        updated_book["price"] = request_data['price']
    for book in books:
        if book["isbn"] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response


# Route to delete a book by its ISBN
@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    """
    Delete a book from the list by its ISBN.

    Parameters:
    - isbn (int): The ISBN number of the book to delete.

    Returns:
    - Response: A '204 No Content' response if deletion is successful.
                A '404 Not Found' response if the ISBN is incorrect or book not found.
    """
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            response = Response("", status=204)
            return response
        i += 1
    invalidBookObjectErrorMsg = {
        "error": "Cannot delete - Incorrect ISBN number. Use the correct ISBN number that is provided in the books list."
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='application/json')
    return response


# Run the application
app.run(port=5000)

# Check if the module is executed as the main program and run the app
__name__ == "__main__"
