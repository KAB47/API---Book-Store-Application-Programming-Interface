# API---Book-Store-Application-Programming-Interface

A bookstore API that allows users to view, add, update, and delete books in a catalogue by sending requests from a web interface (`index.html`) to the backend (`flask_task.py`). The backend processes these actions and returns the updated data or success messages.

---

## **Introduction**
My idea of an API is an entity that enables two applications to communicate with each other. For example, a client (such as Postman, a web app, or JavaScript in a browser) sends requests to the API (Flask app), which processes these requests and returns appropriate responses.

In this project, the `index.html` app (client) communicates with the `flask_task.py` app (API). The API handles requests like fetching the list of books, adding new ones, or deleting existing ones, then sends responses such as updated data or success messages.

### **Project Overview**
This bookstore app allows users to:
- View a catalogue of books.
- Add new books.
- Update or delete books from the catalogue.

Both the `index.html` (frontend) and `flask_task.py` (backend API) files can be opened in an IDE like PyCharm or Visual Studio Code for further exploration.  
The API was tested using **Postman**.

### **Prerequisites**
- Python 3.x (Download [here](https://www.python.org/downloads/release/python-3130/), and ensure to check "Add to PATH" during installation.)
- Flask library (Install via `pip install flask`).

---

## **Features**
- **Get Books**: View all books in the store, including their ISBN and price.
- **Add a New Book**: Add a new book by providing its name, price, and ISBN.
- **Get Book by ISBN**: Fetch the details of a specific book by entering its ISBN.
- **Replace a Book**: Replace an existing book by specifying its ISBN and new details (name and price).
- **Update Book Info**: Update specific details (name, price, or both) of a book using its ISBN.
- **Delete Book by ISBN**: Remove a book from the catalogue by entering its ISBN.

---

## **Logic**
The `index.html` frontend sends requests to the `flask_task.py` backend each time you perform an action. For example:
- **Delete Book by ISBN**:
  - Entering an ISBN triggers a DELETE request to `flask_task.py`.
  - The backend locates and deletes the book from the catalogue.
  - After deletion, clicking "Get Books" will show the updated list without the removed book.

---

## **Setup Instructions**
1. **Download the Project**:
   - Download and unzip the `app.py` folder.

2. **Prepare the Environment**:
   - Install Python 3.x (if not already installed).
   - Install Flask by running:
     ```bash
     pip install flask
     ```

3. **Run the API Server**:
   - Open the `app.py` folder in your file explorer and copy the folder path.
   - Open Command Prompt as an administrator and navigate to the folder:
     ```bash
     cd <path-to-folder>
     ```
   - Start the server:
     ```bash
     python flask_task.py
     ```

4. **Access the Web Interface**:
   - Open a browser and enter the server address displayed in the terminal (e.g., `http://127.0.0.1:5000`).

---

## **API Endpoints**
- **GET** `/books`: Retrieve all books in the catalogue.
- **POST** `/books`: Add a new book (requires `name`, `price`, and `ISBN` as JSON payload).
- **GET** `/books/<ISBN>`: Retrieve details of a specific book by ISBN.
- **PUT** `/books/<ISBN>`: Replace a book’s details (requires `name` and `price` as JSON payload).
- **PATCH** `/books/<ISBN>`: Update specific book details (e.g., just the `price` or `name`).
- **DELETE** `/books/<ISBN>`: Remove a book by its ISBN.

---

## **Testing**
- The API can be tested using tools like **Postman** or directly from the browser for GET requests.
- Example:
  - **POST** `/books`: Use JSON payload to add a book:
    ```json
    {
      "name": "New Book Title",
      "price": 29.99,
      "ISBN": "1234567890"
    }
    ```

---

