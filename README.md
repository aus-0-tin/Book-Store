# BOOK HAVEN
Book Haven is a charming independent bookstore nestled in the heart of downtown. With its cozy atmosphere and a curated selection of books, it caters to readers of all ages and interests. Book Haven offers a diverse range of titles. The store also features a cozy reading nook, perfect for immersing yourself in a new book, and a friendly, knowledgeable staff ready to offer personalized recommendations. If you're searching for your next great read, Book Haven is the perfect destination.

## Features
## Book Management
- Add a book
- Look up a book
- Display all books
- Exit program

## Requirements

- Python 3.x
- SQLAlchemy

 
## Installation
To install and set up the Book store, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://https://github.com/your-username/Book-Store


2. pip install sqlalchemy


## Usage
Run the program:
- cd into 'book-store'
- Run "python main.py" in your terminal
Follow the on-screen menu:

Select 1 to add a new book.
Select 2 to look up a book by name.
Select 3 to display all books.
Select 4 to quit the program.
Example
css
Copy code
*** Books Manager ***
1) Add a book
2) Lookup a book
3) Display books
4) Quit


## Database
The program uses SQLite to store book information in a database named books.db. The database schema is defined using SQLAlchemy ORM.

### Schema
The books table has the following columns:

- id: Integer, primary key
- name: Text, not null
- author: Text, not null
- pages: Integer, not null

### Viewing the Database
To view the books directly from the database outside of the program, you can use an SQLite database browser or the command-line tool.

#### Using SQLite Browser
1. Download and install SQLite Browser from sqlitebrowser.org.
2. Open books.db using SQLite Browser.
3. Browse the data in the books table.
#### Using SQLite Command Line Tool
1. Open a terminal and navigate to the directory containing books.db.
2. Run sqlite3 books.db.
3. Execute SQL queries to view the data:

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- SQLAlchemy for ORM support
- SQLite for the database engine





